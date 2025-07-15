QDarkStyle Utils CLI
====================

Command-line interface for processing QRC files, generating stylesheets, and creating custom palettes.

Usage
-----

.. code-block:: bash

    python -m qdarkstyle.utils [OPTIONS]

The tool converts ``.qrc`` files to ``_rc.py`` and ``.rcc`` files, generates images from SVG sources, and compiles SCSS to QSS stylesheets.

Basic Examples
--------------

Generate default resources:

.. code-block:: bash

    python -m qdarkstyle.utils

Generate for specific Qt binding:

.. code-block:: bash

    python -m qdarkstyle.utils --create pyqt5

Generate for all bindings:

.. code-block:: bash

    python -m qdarkstyle.utils --create all

Watch mode for development:

.. code-block:: bash

    python -m qdarkstyle.utils --watch

Custom palette:

.. code-block:: bash

    python -m qdarkstyle.utils \
        --custom-palette-file my_palette.py \
        --custom-palette-class-name MyPalette

API Reference
-------------

.. automodule:: qdarkstyle.utils.__main__
   :members: main
   :noindex: 