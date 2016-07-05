Changes in Jupyter console
==========================

A summary of changes in Jupyter console releases.

5.0
---

Interactive Shell architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- disinherit shell class from IPython Interactive Shell `#68 <https://github.com/jupyter/jupyter_console/pull/68>`_
  This separates jupyter_console's ZMQTerminalInteractiveShell from IPython's TerminalInteractiveShell and InteractiveShell classes.
- update SIGINT handler to not use the old interactive API shell `#80 <https://github.com/jupyter/jupyter_console/pull/80>`_

Image Handling improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^
- use PIL as default image handler `#79 <https://github.com/jupyter/jupyter_console/pull/79>`_
- better indication of whether image data was handled `#77 <https://github.com/jupyter/jupyter_console/pull/77>`_

Prompts improvement
^^^^^^^^^^^^^^^^^^^
- use prompt_toolkit 1.0 `#74 <https://github.com/jupyter/jupyter_console/pull/74>`_
- don't use prompt_manager `#75 <https://github.com/jupyter/jupyter_console/pull/75>`_
- remove ``colors_force`` flag that have no effects: `#88 <https://github.com/jupyter/jupyter_console/pull/88>`_

4.1
---

4.1.1
~~~~~

- fix for readline history
- don't confuse sys.path with virtualenvs

4.1.0
~~~~~

- readline/completion fixes
- use is_complete messages to determine if input is complete (important for non-Python kernels)
- fix: 4.0 was looking for jupyter_console_config in IPython config directories, not Jupyter


4.0
---

4.0.3
~~~~~

-  fix ``jupyter console --generate-config``

4.0.2
~~~~~

-  setuptools fixes for Windows

4.0.0
~~~~~

First release as a standalone package.
