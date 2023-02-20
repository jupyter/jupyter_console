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


### Release build:

```bash
$ pip install pep517
$ python -m pep517.build .
```


## Resources
- [Project Jupyter website](https://jupyter.org)
- [Documentation for Jupyter Console](https://jupyter-console.readthedocs.io/en/latest/) [[PDF](https://media.readthedocs.org/pdf/jupyter-console/latest/jupyter-console.pdf)]
- [Documentation for Project Jupyter](https://jupyter.readthedocs.io/en/latest/index.html) [[PDF](https://media.readthedocs.org/pdf/jupyter/latest/jupyter.pdf)]
- [Issues](https://github.com/jupyter/jupyter_console/issues)
- [Technical support - Jupyter Google Group](https://groups.google.com/forum/#!forum/jupyter)

## About the Jupyter Development Team

The Jupyter Development Team is the set of all contributors to the Jupyter project.
This includes all of the Jupyter subprojects.

The core team that coordinates development on GitHub can be found here:
https://github.com/jupyter/.

## Our Copyright Policy

Jupyter uses a shared copyright model. Each contributor maintains copyright
over their contributions to Jupyter. But, it is important to note that these
contributions are typically only changes to the repositories. Thus, the Jupyter
source code, in its entirety is not the copyright of any single person or
institution.  Instead, it is the collective copyright of the entire Jupyter
Development Team.  If individual contributors want to maintain a record of what
changes/contributions they have specific copyright on, they should indicate
their copyright in the commit message of the change, when they commit the
change to one of the Jupyter repositories.

With this in mind, the following banner should be used in any source code file
to indicate the copyright and license terms:

```
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
```
