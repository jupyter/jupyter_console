#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

# the name of the project
name = 'jupyter_console'

#-----------------------------------------------------------------------------
# Minimal Python version sanity check
#-----------------------------------------------------------------------------

import sys


if sys.version_info < (3, 6):
    pip_message = 'This may be due to an out of date pip. Make sure you have pip >= 9.0.1.'
    try:
        import pip
        pip_version = tuple([int(x) for x in pip.__version__.split('.')[:3]])
        if pip_version < (9, 0, 1) :
            pip_message = 'Your pip version is out of date, please install pip >= 9.0.1. '\
            'pip {} detected.'.format(pip.__version__)
        else:
            # pip is new enough - it must be something else
            pip_message = ''
    except Exception:
        pass


    error = """
Jupyter_Console 6.2+ supports Python 3.6 and above.
When using Python 2.7, please install and older version of Jupyter Console
Python 3.3 and 3.4 were supported up to Jupyter Console 5.x.
Python 3.5 was supported up to Jupyter Console 6.1.0.

Python {py} detected.
{pip}
""".format(py=sys.version_info, pip=pip_message )

    print(error, file=sys.stderr)
    sys.exit(1)


#-----------------------------------------------------------------------------
# get on with it
#-----------------------------------------------------------------------------

import os

from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
pkg_root = pjoin(here, name)

packages = []
for d, _, _ in os.walk(pjoin(here, name)):
    if os.path.exists(pjoin(d, '__init__.py')):
        packages.append(d[len(here)+1:].replace(os.path.sep, '.'))


setup_args = dict(
    name            = name,
    packages        = packages,
    description     = "Jupyter terminal console",
    long_description= "An IPython-like terminal frontend for Jupyter kernels in any language.",
    long_description_content_type='text/markdown',
    author          = 'Jupyter Development Team',
    author_email    = 'jupyter@googlegroups.com',
    url             = 'https://jupyter.org',
    license         = 'BSD',
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers     = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'jupyter_client>=7.0.0',
        'ipython',
        'ipykernel',  # bless IPython kernel for now
        'prompt_toolkit>=2.0.0,<3.1.0,!=3.0.0,!=3.0.1',
        'pygments',
    ],
    extras_require={
        'test:sys_platform != "win32"': ['pexpect'],
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'jupyter-console = jupyter_console.app:main',
        ]
    }
)


if __name__ == '__main__':
    setup(**setup_args)
