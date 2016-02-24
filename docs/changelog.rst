Changes in Jupyter console
==========================

A summary of changes in Jupyter console releases.

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
