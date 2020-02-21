Jupyter console |version|
=========================

The Jupyter console is a terminal frontend for kernels using the Jupyter protocol.
The console can be installed with::

    pip install jupyter-console

If you want to use conda instead to perform your installation::

    conda install -c conda-forge jupyter_console

And started with::

    jupyter console

To see configuration options::

    jupyter console -h

To start the console with a particular kernel, ask for it by name::

    jupyter console --kernel=julia-0.4

A list of available kernels can be seen with::

    jupyter kernelspec list

You can connect to a live kernel (e.g. one running in a notebook) with its ID::

    jupyter console --existing KERNEL_ID

or even connect to the most recently started kernel by default::

    jupyter console --existing


Contents:

.. toctree::
   :maxdepth: 2

   config_options
   release
   changelog

