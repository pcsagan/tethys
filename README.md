# Tethys: Python package template with testing, documentation, and publishing

[![Tests](https://github.com/pcsagan/tethys/actions/workflows/tests.yml/badge.svg)](https://github.com/pcsagan/tethys/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/tethys-template.svg?label=PyPI)](https://pypi.org/project/tethys-template/)
[![Code of conduct](https://img.shields.io/badge/Code%20of%20conduct-welcoming-blue)](https://github.com/pcsagan/tethys/blob/main/CODE_OF_CONDUCT.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/pcsagan/tethys/blob/main/LICENSE)

Tethys is modern python package template. It demonstrates automation, configuration, environment orchestration, code validation, and Github actions. It comes with a [command line interface](), and it also contains an example [readme](), [security policy](), and [code of conduct]().

# Features

- Package configuration confined to `pyproject.toml` and `tox.ini`
- Command line interface with [click](https://click.palletsprojects.com/)
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/reference/customize.html#tox-ini) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/tox.html)
- Documentation with [sphinx](https://www.sphinx-doc.org/en/master) supporting [markdown](https://coderefinery.github.io/sphinx-lesson/md-and-rst) with [myst](https://myst-parser.readthedocs.io/en/latest)
- Publishing to [PyPI](https://pypi.org) and [TestPyPI](https://test.pypi.org)
- Environment orchestration with [Tox](https://github.com/tox-dev/tox)
- Code validation with [black](https://github.com/psf/black), [flake8](https://github.com/PyCQA/flake8), [mypy](https://github.com/python/mypy), [pycodestyle](https://github.com/PyCQA/pycodestyle), [pydocstyle](https://github.com/PyCQA/pydocstyle)
- Configuration validation with [validate-pyproject](https://github.com/abravalheri/validate-pyproject)
- Github actions for [testing](https://github.com/pcsagan/tethys/blob/main/.github/workflows/tests.yml), [documentation](https://github.com/pcsagan/tethys/blob/main/.github/workflows/docs.yml), and [publishing](https://github.com/pcsagan/tethys/blob/main/.github/workflows/publish.yml) to [PyPI](https://pypi.org) and [TestPyPI](https://test.pypi.org)

# Documentation

See the [documentation](https://validate-pyproject.readthedocs.io/en/latest/) for more details on this package template.
