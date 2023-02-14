# Tethys

```{toctree}
---
caption: Contents
maxdepth: 1
---

quickstart.md
```

This template package is designed to be an easy starting point for your next python package.

## Create your repository

Create a new repository using Github's template interface, or run the following commands:

```shell
git clone https://github.com/pcsagan/tethys <your_package_name>
cd <your_package_name>
rm -rf .git
git init .
```

## Update package attribution

Find and replace all instances of `tethys` and `tethys-template` with your package name

- Your project name can match your package name. The name `tethys-template` was required because`tethys` already exists on PyPI

## Configure your package

### pyproject.toml

- Update the author and package dependencies
- Update the [Security Policy](https://github.com/pcsagan/tethys/blob/main/SECURITY.md) and the [Code of Conduct](https://github.com/pcsagan/tethys/blob/main/CODE_OF_CONDUCT.md) with your e-mail address

### Validators

- Configuration for [mypy](https://mypy.readthedocs.io/en/stable/config_file.html)
- Configuration for [black](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html)
- Configuration for [flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)
- Configuration for [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration)
- Configuration for [pydocstyle](http://www.pydocstyle.org/en/stable/usage.html#configuration-files)
- Configuration for [pytest](https://docs.pytest.org/en/7.1.x/reference/customize.html#tox-ini)
- Configuration for [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/tox.html)

### Github Actions

### Development Environment

Install your package dependencies into your development environment

    - Install the package locally in editable mode using the command:

        ```shell
        pip install -e .
        ```
    - Install the package locally along with all testing libraries used by `tox` with the command:

        ```shell
        pip install -r requirements.txt
        ```

## Command Line Interface

- Documentation for [click](https://click.palletsprojects.com/)
- The entry point is defined in the project.scripts table in the `pyproject.toml` file

## Coding and Testing

- Add your code to the package while regularly committing your changes to your Github repository
- Add your tests to the `tests` directory

## Using Tox

- Run all tasks in their own environments using the command:

  ```shell
  tox
  ```

- Run specific tasks using `tox` with the `-e` flag:

  ```shell
  tox -e black
  tox -e docs
  tox -e flake8
  tox -e mypy
  tox -e pycodestyle
  tox -e pydocstyle
  tox -e pytest
  tox -e validate-pyproject
  ```

- If you installed the `requirements.txt` file then you can use testing packages in your local environment:

  ```shell
  black src
  sphinx-apidoc -f -o docs/source src/<my_package_name>
  sphinx-build -b html docs/source docs/build/html
  flake8 src tests
  mypy src
  pycodestyle src
  pydocstyle src
  pytest tests
  ```

## PyPI

### API Token

- Register on [PyPI](https://pypi.org) (and [TestPyPI](https://test.pypi.org)) and generate [API tokens](https://pypi.org/help/#apitoken)
- Add your tokens as a [secret variable](https://docs.github.com/en/actions/security-guides/encrypted-secrets) named `pypi_api_token` and `testpypi_api_token` to your Github repository

### TestPyPI

## Publish

Manually run the `Publish` action to publish your package on PyPI
