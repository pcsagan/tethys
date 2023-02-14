# Quickstart

```python
def function(param: int) -> bool:
    """ Fail because do."""
    return False
```

There are two ways to use this template:

- Click <a href="https://github.com/pcsagan/tethys/generate"><img src="https://img.shields.io/badge/-Use%20this%20template-brightgreen?style=flat" /></a>
- Run the following commands:

  ```shell
  git clone https://github.com/pcsagan/tethys <your_package_name>
  cd <your_package_name>
  rm -rf .git
  git init .
  ```

## Install the package locally

- Install the package locally in editable mode using the command:

  ```shell
  pip install -e .
  ```

- Install the package locally along with testing, documentation, and building tools using the command:

  ```shell
  pip install -r requirements.txt
  ```

## Run the tools

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
