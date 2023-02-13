# Changes in Jupyter Console {#changelog}

<!-- <START NEW CHANGELOG ENTRY> -->

## 6.5.1

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/v6.5.0...25fe1d530cefe22596fc2aa9694cdcded14c0af3))

### Bugs fixed

- Fix completion handling [#278](https://github.com/jupyter/jupyter_console/pull/278) ([@blink1073](https://github.com/blink1073))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2023-02-09&to=2023-02-13&type=c))

[@blink1073](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Ablink1073+updated%3A2023-02-09..2023-02-13&type=Issues)

<!-- <END NEW CHANGELOG ENTRY> -->

## 6.5.0

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/v6.4.4...7bcb1c61c709d033d5b24ecaea3cc6161ff69f5a))

### Bugs fixed

- Fix client 7 and 8 compat [#276](https://github.com/jupyter/jupyter_console/pull/276) ([@blink1073](https://github.com/blink1073))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2022-06-22&to=2023-02-09&type=c))

[@blink1073](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Ablink1073+updated%3A2022-06-22..2023-02-09&type=Issues)

## 6.4.4

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/v6.4.3...18cb350dc05c903d541f30de18fcf53943ec0e3f))

### Merged PRs

- Use asyncio.create_task and asyncio.get_running_loop with interact(). Drop Python 3.6. [#270](https://github.com/jupyter/jupyter_console/pull/270) ([@encukou](https://github.com/encukou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2022-03-07&to=2022-06-22&type=c))

[@davidbrochart](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Adavidbrochart+updated%3A2022-03-07..2022-06-22&type=Issues) | [@encukou](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Aencukou+updated%3A2022-03-07..2022-06-22&type=Issues)

## 6.4.3

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/v6.4.2...6e8f29e0a90804badda75c60c5eb50046544eb49))

### Merged PRs

- Require jupyter_client>=7.0.0 [#266](https://github.com/jupyter/jupyter_console/pull/266) ([@davidbrochart](https://github.com/davidbrochart))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2022-03-06&to=2022-03-07&type=c))

[@davidbrochart](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Adavidbrochart+updated%3A2022-03-06..2022-03-07&type=Issues)

## 6.4.2

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/v6.4.1...b3ff8fcd24fe22dfbd66518dc8e6a646f460a671))

### Merged PRs

- Don't pass loop to asyncio.wait() [#264](https://github.com/jupyter/jupyter_console/pull/264) ([@davidbrochart](https://github.com/davidbrochart))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2022-03-06&to=2022-03-06&type=c))

[@davidbrochart](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Adavidbrochart+updated%3A2022-03-06..2022-03-06&type=Issues)

## 6.4.1

([Full Changelog](https://github.com/jupyter/jupyter_console/compare/6.4.0...2d0b6aec59bde7499995d929ded4d23d7bb585f6))

### Merged PRs

- Prepare for use with Jupyter Releaser [#261](https://github.com/jupyter/jupyter_console/pull/261) ([@davidbrochart](https://github.com/davidbrochart))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyter/jupyter_console/graphs/contributors?from=2021-03-24&to=2022-03-06&type=c))

[@davidbrochart](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Adavidbrochart+updated%3A2021-03-24..2022-03-06&type=Issues) | [@emuccino](https://github.com/search?q=repo%3Ajupyter%2Fjupyter_console+involves%3Aemuccino+updated%3A2021-03-24..2022-03-06&type=Issues)

## 6.4.0

## 5.3.0

- Highlight matching parentheses [#147](https://github.com/jupyter/jupyter_console/pull/147)
- The config option `JupyterConsoleApp.confirm_exit` replaces `ZMQTerminalInteractiveShell.confirm_exit`, to avoid redundancy [#141](https://github.com/jupyter/jupyter_console/pull/141)

## 5.2

- When using a kernel that the console did not start, exiting with Ctrl-D now leaves it running [#127](https://github.com/jupyter/jupyter_console/pull/127)
- Added Ctrl-\\ shortcut to quit the console [#130](https://github.com/jupyter/jupyter_console/pull/130)
- Input prompt numbers are now updated when another frontend has executed code in the same kernel [#119](https://github.com/jupyter/jupyter_console/pull/119)
- Fix setting next input with newer versions of prompt_toolkit [#123](https://github.com/jupyter/jupyter_console/pull/123)
- Ensure history entries are unicode, not bytes, on Python 2 [#122](https://github.com/jupyter/jupyter_console/pull/122)

## 5.1

- New `ZMQTerminalInteractiveShell.true_color` config option to use 24-bit colour
- New `ZMQTerminalInteractiveShell.confirm_exit` config option to turn off asking 'are you sure' on exit
- New `--simple-prompt` flag to explicitly use the fallback mode without prompt_toolkit
- Fixed executing an empty input
- Fixed formatting for code and outputs from other frontends executing code
- Avoid using functions which will be removed in IPython 6

## 5.0

## 5.0.0

### Interactive Shell architecture

- Disinherit shell class from IPython Interactive Shell. This separates jupyter_console's `ZMQTerminalInteractiveShell` from IPython's `TerminalInteractiveShell` and `InteractiveShell` classes [#68](https://github.com/jupyter/jupyter_console/pull/68)
- Update SIGINT handler to not use the old interactive API shell [#80](https://github.com/jupyter/jupyter_console/pull/80)

### Image Handling improvement

- use PIL as default image handler [#79](https://github.com/jupyter/jupyter_console/pull/79)
- better indication of whether image data was handled [#77](https://github.com/jupyter/jupyter_console/pull/77)

### Prompts improvement

- use prompt_toolkit 1.0 [#74](https://github.com/jupyter/jupyter_console/pull/74)
- don't use prompt_manager [#75](https://github.com/jupyter/jupyter_console/pull/75)
- remove `colors_force` flag that have no effects [#88](https://github.com/jupyter/jupyter_console/pull/88)

## 4.1

## 4.1.1

- fix for readline history
- don't confuse sys.path with virtualenvs

## 4.1.0

- readline/completion fixes
- use is_complete messages to determine if input is complete (important for non-Python kernels)
- fix: 4.0 was looking for jupyter_console_config in IPython config directories, not Jupyter

## 4.0

## 4.0.3

- fix `jupyter console --generate-config`

## 4.0.2

- setuptools fixes for Windows

## 4.0.0

- First release as a standalone package.
