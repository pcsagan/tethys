<div align="center">

<img src="https://i.imgur.com/jjnYRTV.png" title="tethys">

[![Tests](https://github.com/pcsagan/tethys/actions/workflows/tests.yml/badge.svg)](https://github.com/pcsagan/tethys/actions/workflows/tests.yml)
[![Code of conduct](https://img.shields.io/badge/Code%20of%20conduct-welcoming-blue)](CODE_OF_CONDUCT.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/pcsagan/tethys/blob/main/LICENSE)

</div>

## Using this template

1. Create a new repository using Github's template interface, or run the following commands:
    ```shell
    git clone https://github.com/pcsagan/tethys <your_package_name>
    cd <your_package_name>
    rm -rf .git
    git init .
    ```
2. Find and replace all instances of `tethys` and `tethys-template` with your package name
    - Your project name can match your package name. The name `tethys-template` was required because of a clash with an existing `tethys` on PyPI
3. Update `pyproject.toml` to reflect its new author and requirements
    - Set the version to new value before publishing to [PyPI](https://pypi.org) (and [TestPyPI](https://test.pypi.org))
    - List of [Classifiers](https://pypi.org/classifiers/)
    - Configuration for [mypy](https://mypy.readthedocs.io/en/stable/config_file.html)
4. Update `tox.ini` to build the desired testing environments
    - Configuration for [black](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html)
    - Configuration for [flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)    
    - Configuration for [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration)
    - Configuration for [pydocstyle](http://www.pydocstyle.org/en/stable/usage.html#configuration-files)    
    - Configuration for [pytest](https://docs.pytest.org/en/7.1.x/reference/customize.html#tox-ini)
    - Configuration for [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/tox.html)
5. Update `cli.py` to customize the command line interface
    - Documentation for [click](https://click.palletsprojects.com/)
    - The entry point is defined in the project.scripts table in the `pyproject.toml` file
6. Update `.git/workflows/tests.yaml` to specify the various operating systems and python versions used for testing
7. Add your code to the package while regularly committing your changes to your Github repository
    - Use the `tox` command to test your changes locally. This is what the `Tests` action on Github does.
8. Add your tests to the `tests` directory
9. Test your package using `tox`
    - Run all tests in their own environments using the command:
        ```shell
        tox
        ```
    - Run specific tests using `tox` with the `-e` flag:
        ```shell
        tox -e pytest
        tox -e flake8
        ```
    - Install all the tools used by `tox` into your local environment using the command:
        ```shell
        pip install -r requirements.txt
        ```
10. Set the version attribute of the project table in the `pyproject.toml` file to a unique value in order to satisfy [PyPI](https://pypi.org) (and [TestPyPI](https://test.pypi.org))
11. Register on [PyPI](https://pypi.org) (and [TestPyPI](https://test.pypi.org)) and generate [API tokens](https://pypi.org/help/#apitoken)
12. Add your tokens as a [secret variable](https://docs.github.com/en/actions/security-guides/encrypted-secrets) named `pypi_api_token` and `testpypi_api_token` to your Github repository
13. Manually run the `Publish Test` action to verify that your token and package version are accepted using TestPyPI
14. Manually run the `Publish` action to publish your package on PyPI

## Help

```
Usage: tethys [OPTIONS] COMMAND [ARGS]...

  Tethys is a moon of Saturn.

Options:
  --version  Show the version and exit.
  --debug    Run the command in debug mode.
  --help     Show this message and exit.

Commands:
  data  Print the shared context data to the screen.
  foo   Print the result of calling the foo function to the screen.
```

