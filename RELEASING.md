# Releasing

## Prerequisites

- Install `bump2version`
- Install `twine`

## Push to GitHub

Change from patch to minor or major for appropriate version updates.

```bash
# Commit, test, publish, tag release
bump2version minor # CHECK FIRST: If the patch version currently set is not sufficient
git commit -am "Prepared <release-id>"
bump2version suffix  # Remove the .dev
git commit -am "Generated release <release-id>"
git tag <release_version_here>
git push && git push --tags
```

## Push to PyPI

```bash
rm -rf dist/*
rm -rf build/*
python setup.py sdist bdist_wheel
# Double check the dist/* files have the right verison (no `.dev`) and install the wheel to ensure it's good
pip install dist/*
twine upload dist/*
```

## Prep repo for development

- `bumpversion patch # Resets the patch and dev versions`
- `git commit -am "Resumed patch dev"; git push`
