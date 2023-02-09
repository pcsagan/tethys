# tethys

A template for a python module with tox, pytest, flake8, and mypy.

## Dependencies

The `pyproject.toml` file determines which dependencies are installed along with the module. The `requirements.txt` file is used to initialize your development environment. The `requirements_dev.txt` file is used to initialize the testing virtual environments. The testing modules are only installed in the testing environment.

## Usage

To test the module run the `tox` command

```
tox
```

To test the module scripts run the `foobar` command

```
foobar
```

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
