""" For beta/alpha/rc releases, the version number for a beta is X.Y.ZbN
**without dots between the last 'micro' number and b**. N is the number of
the beta released i.e. 1, 2, 3 ...

See PEP 440 https://www.python.org/dev/peps/pep-0440/
"""

version_info = (6, 1, 1, 'dev')

# unlike `.dev`, alpha, beta and rc _must not_ have dots,
# or the wheel and tgz won't look to pip like the same version.

__version__ = (
    ".".join(map(str, version_info))
    .replace(".b", "b")
    .replace(".a", "a")
    .replace(".rc", "rc")
)
assert ".b" not in __version__
assert ".a" not in __version__
assert ".rc" not in __version__
