# tethys

A template for a python module with tox, pytest, flake8, and mypy.

## Dependencies

The `dependencies` attribute in the `[project]` table within `pyproject.toml` determines which dependencies are installed along with the module. The `requirements.txt` file is used to initialize your development environment. The `requirements_dev.txt` file is used to initialize the testing virtual environments. The testing modules `pytest`, `flake8`, and `mypy` are only installed in the testing environment.

## Usage

To test the module run the `tox` command

```
tox
```

To test the module scripts defined in `[project.scripts]` in `pyproject.toml` run the `foobar` command

```
foobar
```

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
