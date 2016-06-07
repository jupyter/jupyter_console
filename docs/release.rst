.. _jupyter_console_release:

Making a release as a maintainer
================================

This document guides a maintainer through creating a release of the Jupyter
console.

Check installed tools
---------------------

Review ``CONTRIBUTING.rst``. Make sure all the tools needed are properly
installed.

Clean the repository
--------------------

Remove all non-tracked files with:

.. code:: bash

    git clean -xfdi

This will ask you for confirmation before removing all untracked files. Make
sure the ``dist/`` folder is clean and does not contain any stale builds from
previous attempts.

Create the release
------------------

#. Set Environment variables

    Set environment variables to document current release version, and git tag:

    .. code:: bash

        VERSION=4.1.0

#.  Update version number in ``jupyter_console/_version.py``. Make sure that
    a valid `PEP 440 <https://www.python.org/dev/peps/pep-0440/>`_ version is
    being used.

#.  Commit and tag the release with the current version number:

    .. code:: bash

        git commit -am "release $VERSION"
        git tag $VERSION

#.  You are now ready to build the ``sdist`` and ``wheel``:

    .. code:: bash

        python setup.py sdist --formats=zip,gztar
        python setup.py bdist_wheel

#.  You can now test the ``wheel`` and the ``sdist`` locally before uploading
    to PyPI. Make sure to use `twine <https://github.com/pypa/twine>`_ to
    upload the archives over SSL.

    .. code:: bash

        twine upload dist/*

#.  If all went well, change the ``jupyter_console/_version.py`` to the next
    release.

#.  Push directly on master, not forgetting to push ``--tags`` too.
