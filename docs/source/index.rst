Welcome to Tethys's documentation!
==================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   modules
   tethys


How to add a data folder to your package
----------------------------------------

Data directories can be added to the package by specifying them in the ``pyproject.toml`` file.

See `Data Files Support <https://setuptools.pypa.io/en/latest/userguide/datafiles.html#subdirectory-for-data-files>`_ for more details.

.. code-block:: toml
   :caption: pyproject.toml

   [tool.setuptools.package-data]
   "tethys.templates" = ["**/*.jpeg"]

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
