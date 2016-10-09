# Jupyter Console
[![Build Status](https://travis-ci.org/jupyter/jupyter_console.svg?branch=master)](https://travis-ci.org/jupyter/jupyter_console)
[![Documentation Status](http://readthedocs.org/projects/jupyter-console/badge/?version=latest)](https://jupyter-console.readthedocs.io/en/latest/?badge=latest)

A terminal-based console frontend for Jupyter kernels.
This code is based on the single-process IPython terminal.

Install with pip:

    pip install jupyter-console

Install with conda:

    conda install -c conda-forge jupyter_console

Start:

    jupyter console

Help:

    jupyter console -h

Jupyter Console allows for console-based interaction with non-python 
Jupyter kernels such as IJulia, IRKernel.

To start the console with a particular kernel, ask for it by name::

    jupyter console --kernel=julia-0.4

A list of available kernels can be seen with::

    jupyter kernelspec list


## Resources
- [Project Jupyter website](https://jupyter.org)
- [Documentation for Jupyter Console](https://jupyter-console.readthedocs.io/en/latest/) [[PDF](https://media.readthedocs.org/pdf/jupyter-console/latest/jupyter-notebook.pdf)]
- [Documentation for Project Jupyter](https://jupyter.readthedocs.io/en/latest/index.html) [[PDF](https://media.readthedocs.org/pdf/jupyter/latest/jupyter.pdf)]
- [Issues](https://github.com/jupyter/jupyter_console/issues)
- [Technical support - Jupyter Google Group](https://groups.google.com/forum/#!forum/jupyter)
