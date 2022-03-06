# Changes in Jupyter Console {#changelog}

<!-- <START NEW CHANGELOG ENTRY> -->

## 6.4.0

<!-- <END NEW CHANGELOG ENTRY> -->

## 5.3.0

- Highlight matching parentheses [#147](https://github.com/jupyter/jupyter_console/pull/147)
- The config option `JupyterConsoleApp.confirm_exit` replaces `ZMQTerminalInteractiveShell.confirm_exit`, to avoid redundancy [#141](https://github.com/jupyter/jupyter_console/pull/141)

## 5.2

- When using a kernel that the console did not start, exiting with Ctrl-D now leaves it running [#127](https://github.com/jupyter/jupyter_console/pull/127)
- Added Ctrl-\\ shortcut to quit the console [#130](https://github.com/jupyter/jupyter_console/pull/130)
- Input prompt numbers are now updated when another frontend has executed code in the same kernel [#119](https://github.com/jupyter/jupyter_console/pull/119)
- Fix setting next input with newer versions of prompt_toolkit [#123](https://github.com/jupyter/jupyter_console/pull/123)
- Ensure history entries are unicode, not bytes, on Python 2 [#122](https://github.com/jupyter/jupyter_console/pull/122)

## 5.1

- New `ZMQTerminalInteractiveShell.true_color` config option to use 24-bit colour
- New `ZMQTerminalInteractiveShell.confirm_exit` config option to turn off asking 'are you sure' on exit
- New `--simple-prompt` flag to explicitly use the fallback mode without prompt_toolkit
- Fixed executing an empty input
- Fixed formatting for code and outputs from other frontends executing code
- Avoid using functions which will be removed in IPython 6

## 5.0

## 5.0.0

### Interactive Shell architecture

- Disinherit shell class from IPython Interactive Shell. This separates jupyter_console's `ZMQTerminalInteractiveShell` from IPython's `TerminalInteractiveShell` and `InteractiveShell` classes [#68](https://github.com/jupyter/jupyter_console/pull/68)
- Update SIGINT handler to not use the old interactive API shell [#80](https://github.com/jupyter/jupyter_console/pull/80)

### Image Handling improvement

- use PIL as default image handler [#79](https://github.com/jupyter/jupyter_console/pull/79)
- better indication of whether image data was handled [#77](https://github.com/jupyter/jupyter_console/pull/77)

### Prompts improvement

- use prompt_toolkit 1.0 [#74](https://github.com/jupyter/jupyter_console/pull/74)
- don't use prompt_manager [#75](https://github.com/jupyter/jupyter_console/pull/75)
- remove `colors_force` flag that have no effects [#88](https://github.com/jupyter/jupyter_console/pull/88)

## 4.1

## 4.1.1

- fix for readline history
- don't confuse sys.path with virtualenvs

## 4.1.0

- readline/completion fixes
- use is_complete messages to determine if input is complete (important for non-Python kernels)
- fix: 4.0 was looking for jupyter_console_config in IPython config directories, not Jupyter


## 4.0

## 4.0.3

- fix `jupyter console --generate-config`

## 4.0.2

- setuptools fixes for Windows

## 4.0.0

- First release as a standalone package.
