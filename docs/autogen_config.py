#!/usr/bin/env python

import os.path
from jupyter_console.app import ZMQTerminalIPythonApp

header = """\
Configuration options
=====================

These options can be set in ``~/.jupyter/jupyter_console_config.py``, or
at the command line when you start it.
"""

try:
    indir = os.path.dirname(__file__)
except NameError:
    indir = os.getcwd()
destination = os.path.join(indir, 'config_options.rst')

with open(destination, 'w') as f:
    f.write(header)
    f.write(ZMQTerminalIPythonApp().document_config_options())
