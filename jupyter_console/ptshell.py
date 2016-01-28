"""IPython terminal interface using prompt_toolkit in place of readline"""
from __future__ import print_function

import sys
import time
from warnings import warn

try:
    from queue import Empty  # Py 3
except ImportError:
    from Queue import Empty  # Py 2

from IPython.utils.py3compat import PY3, cast_unicode_py2
from traitlets import Bool, Integer, Unicode, Dict

from .interactiveshell import ZMQTerminalInteractiveShell

from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.filters import HasFocus, HasSelection
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.shortcuts import create_prompt_application
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.key_binding.vi_state import InputMode
from prompt_toolkit.key_binding.bindings.vi import ViStateFilter
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.lexers import PygmentsLexer
from prompt_toolkit.styles import PygmentsStyle

from pygments.styles import get_style_by_name
from pygments.lexers import find_lexer_class
from pygments.token import Token

def get_pygments_lexer(name):
    if name == 'ipython2':
        from IPython.lib.lexers import IPythonLexer
        return IPythonLexer
    elif name == 'ipython3':
        from IPython.lib.lexers import IPython3Lexer
        return IPython3Lexer
    else:
        cls = find_lexer_class(name)
        if cls is None:
            warn("No lexer found for language %r. Treating as plain text." % name)
            from pygments.lexers.special import TextLexer
            return TextLexer
        return cls


class IPythonPTCompleter(Completer):
    """Adaptor to provide IPython completions to prompt_toolkit"""
    def __init__(self, ipy_completer):
        self.ipy_completer = ipy_completer

    def get_completions(self, document, complete_event):
        if not document.current_line.strip():
            return

        used, matches = self.ipy_completer.complete(
                            line_buffer=document.current_line,
                            cursor_pos=document.cursor_position_col
        )
        start_pos = -len(used)
        for m in matches:
            yield Completion(m, start_position=start_pos)

class PTInteractiveShell(ZMQTerminalInteractiveShell):
    colors_force = True

    pt_cli = None

    vi_mode = Bool(False, config=True,
        help="Use vi style keybindings at the prompt",
    )

    highlighting_style = Unicode('', config=True,
        help="The name of a Pygments style to use for syntax highlighting"
    )

    highlighting_style_overrides = Dict(config=True,
        help="Override highlighting format for specific tokens"
    )

    history_load_length = Integer(1000, config=True,
        help="How many history items to load into memory"
    )

    def __init__(self, **kwargs):
        super(PTInteractiveShell, self).__init__(**kwargs)
        self.init_kernel_info()
        self.init_prompt_toolkit_cli()
        self.keep_running = True

    def get_prompt_tokens(self, cli):
        return [
            (Token.Prompt, 'In ['),
            (Token.PromptNum, str(self.execution_count)),
            (Token.Prompt, ']: '),
        ]

    def get_continuation_tokens(self, cli, width):
        return [
            (Token.Prompt, (' ' * (width - 2)) + ': '),
        ]

    kernel_info = {}
    def init_kernel_info(self):
        """Wait for a kernel to be ready, and store kernel info"""
        timeout = self.kernel_timeout
        tic = time.time()
        self.client.hb_channel.unpause()
        msg_id = self.client.kernel_info()
        while True:
            try:
                reply = self.client.get_shell_msg(timeout=1)
            except Empty:
                if (time.time() - tic) > timeout:
                    raise RuntimeError("Kernel didn't respond to kernel_info_request")
            else:
                if reply['parent_header'].get('msg_id') == msg_id:
                    self.kernel_info = reply['content']
                    return

    def init_prompt_toolkit_cli(self):
        kbmanager = KeyBindingManager.for_prompt(enable_vi_mode=self.vi_mode)
        insert_mode = ViStateFilter(kbmanager.get_vi_state, InputMode.INSERT)
        # Ctrl+J == Enter, seemingly
        @kbmanager.registry.add_binding(Keys.ControlJ,
                            filter=(HasFocus(DEFAULT_BUFFER)
                                    & ~HasSelection()
                                    & insert_mode
                                   ))
        def _(event):
            b = event.current_buffer
            d = b.document
            if not (d.on_last_line or d.cursor_position_row >= d.line_count
                                           - d.empty_line_count_at_the_end()):
                b.newline()
                return

            more, indent = self.check_complete(d.text)

            if (not more) and b.accept_action.is_returnable:
                b.accept_action.validate_and_handle(event.cli, b)
            else:
                b.insert_text('\n' + indent)

        @kbmanager.registry.add_binding(Keys.ControlC)
        def _(event):
            event.current_buffer.reset()

        # Pre-populate history from IPython's history database
        history = InMemoryHistory()
        last_cell = u""
        for _, _, cell in self.history_manager.get_tail(self.history_load_length,
                                                        include_latest=True):
            # Ignore blank lines and consecutive duplicates
            cell = cell.rstrip()
            if cell and (cell != last_cell):
                history.append(cell)

        style_overrides = {
            Token.Prompt: '#009900',
            Token.PromptNum: '#00ff00 bold',
        }
        if self.highlighting_style:
            style_cls = get_style_by_name(self.highlighting_style)
        else:
            style_cls = get_style_by_name('default')
            # The default theme needs to be visible on both a dark background
            # and a light background, because we can't tell what the terminal
            # looks like. These tweaks to the default theme help with that.
            style_overrides.update({
                Token.Number: '#007700',
                Token.Operator: 'noinherit',
                Token.String: '#BB6622',
                Token.Name.Function: '#2080D0',
                Token.Name.Class: 'bold #2080D0',
                Token.Name.Namespace: 'bold #2080D0',
            })
        style_overrides.update(self.highlighting_style_overrides)
        style = PygmentsStyle.from_defaults(pygments_style_cls=style_cls,
                                            style_dict=style_overrides)

        langinfo = self.kernel_info.get('language_info', {})
        lexer = langinfo.get('pygments_lexer', langinfo.get('name', None))
        app = create_prompt_application(multiline=True,
                            lexer=PygmentsLexer(get_pygments_lexer(lexer)),
                            get_prompt_tokens=self.get_prompt_tokens,
                            get_continuation_tokens=self.get_continuation_tokens,
                            key_bindings_registry=kbmanager.registry,
                            history=history,
                            completer=IPythonPTCompleter(self.Completer),
                            enable_history_search=True,
                            style=style,
        )

        self.pt_cli = CommandLineInterface(app)

    def init_io(self):
        if sys.platform not in {'win32', 'cli'}:
            return

        import colorama
        colorama.init()

    def check_complete(self, code):
        if self.use_kernel_is_complete:
            msg_id = self.client.is_complete(code)
            try:
                return self.handle_is_complete_reply(msg_id, timeout=self.kernel_is_complete_timeout)
            except SyntaxError:
                return False, ""
        else:
            more = (code.splitlines()[-1] != "")
            return more, ""

    def ask_exit(self):
        self.keep_running = False

    rl_next_input = None

    def pre_prompt(self):
        if self.rl_next_input:
            self.pt_cli.application.buffer.text = cast_unicode_py2(self.rl_next_input)
            self.rl_next_input = None

    def interact(self, display_banner=None):
        while self.keep_running:
            print('\n', end='')

            try:
                document = self.pt_cli.run(pre_run=self.pre_prompt)
            except EOFError:
                if self.ask_yes_no('Do you really want to exit ([y]/n)?','y','n'):
                    self.ask_exit()

            else:
                if document:
                    self.run_cell(document.text, store_history=True)

