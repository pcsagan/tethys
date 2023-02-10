<div align="center">

<img src="https://i.imgur.com/jjnYRTV.png" title="tethys">

[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-forestgreen.svg)](https://github.com/pcsagan/tethys/blob/main/tox.ini)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/pcsagan/tethys/blob/main/LICENSE)

</div>

## Dependencies

The `pyproject.toml` file determines which dependencies are installed along with the package:

```
pip install -e .
```

The `requirements.txt` file is used to initialize your development environment:

```
pip install -r requirements.txt
```

## Template

To use this package as a template simply do the following:

1. Find and replace all instances of `tethys` with your package name
2. Update `pyproject.toml` to reflect its new author and requirements
    - Set the version by changing the `__version__` value in the `__init__.py` file
    - List of [Classifiers](https://pypi.org/classifiers/)
    - Configuration for [mypy](https://mypy.readthedocs.io/en/stable/config_file.html)
3. Update `tox.ini` to build the desired testing environments
    - Configuration for [black](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html)
    - Configuration for [flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)    
    - Configuration for [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration)
    - Configuration for [pydocstyle](http://www.pydocstyle.org/en/stable/usage.html#configuration-files)    
    - Configuration for [pytest](https://docs.pytest.org/en/7.1.x/reference/customize.html#tox-ini)
    - Configuration for [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/tox.html)

4. Update `cli.py` to customize the command line interface
5. Test your module using `tox`
6. Use `pip freeze > requirements.txt` to preserve your development environment


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

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.
