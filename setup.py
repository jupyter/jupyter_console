#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

# the name of the project
name = 'jupyter_console'

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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'jupyter_client>=7.0.0',
        'jupyter_core>=4.12,!=5.0.*',
        'ipython',
        'ipykernel>=6.14',  # bless IPython kernel for now
        'prompt_toolkit>=3.0.30',
        'pygments',
        'pyzmq>=17',
        'traitlets>=5.4'
    ],
    extras_require={
        'test': ['pexpect', 'pytest'],
    },
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'jupyter-console = jupyter_console.app:main',
        ]
    }
)


if __name__ == '__main__':
    setup(**setup_args)
