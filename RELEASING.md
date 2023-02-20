# Releasing

## Using `jupyter_releaser`

The recommended way to make a release is to use [`jupyter_releaser`](https://github.com/jupyter-server/jupyter_releaser#checklist-for-adoption).

## Manual Release

### Prerequisites

- First check that the CHANGELOG.md is up to date for the next release version
- Install packaging requirements: `pip install hatch twine`

### Bump version

- `export version=<NEW_VERSION>`
- `hatch version ${version}`

### Push to GitHub

```bash
git push upstream && git push upstream --tags
```

### Push to PyPI

```bash
rm -rf dist/*
rm -rf build/*
hatch build .
twine upload dist/*
```
