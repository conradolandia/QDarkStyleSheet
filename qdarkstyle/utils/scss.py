#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilities for compiling SASS files."""

# Standard library imports
import logging
import os
import sys

# Third party imports
import qtsass

# Local imports
from qdarkstyle import (
    MAIN_SCSS_FILE,
    PACKAGE_PATH,
    QSS_FILE_SUFFIX,
    VARIABLES_SCSS_FILE,
)

# Constants
HEADER_SCSS = '''// ---------------------------------------------------------------------------
//
//    WARNING! File created programmatically. All changes made in this file will be lost!
//
//    Created by the qtsass compiler v{}
//
//    The definitions are in the "qdarkstyle.palette" module
//
//----------------------------------------------------------------------------
'''

HEADER_QSS = '''/* ---------------------------------------------------------------------------

    WARNING! File created programmatically. All changes made in this file will be lost!

    Created by the qtsass compiler v{}

    The definitions are in the "qdarkstyle.qss._styles.scss" module

--------------------------------------------------------------------------- */
'''

_logger = logging.getLogger(__name__)


def _dict_to_scss(data):
    """Create a scss variables string from a dict."""
    lines = []
    template = "${}: {};"
    for key, value in data.items():
        line = template.format(key, value)
        lines.append(line)

    return '\n'.join(lines)


def _scss_to_dict(string):
    """Parse variables and return a dict."""
    data = {}
    lines = string.split('\n')

    for line in lines:
        line = line.strip()

        if line and line.startswith('$'):
            key, value = line.split(':')
            key = key[1:].strip()
            key = key.replace('-', '_')
            value = value.split(';')[0].strip()

            data[key] = value

    return data


def _create_scss_variables(variables_scss_filepath, palette,
                           header=HEADER_SCSS):
    """Create a scss variables file."""

    scss = _dict_to_scss(palette.to_dict())
    data = header.format(qtsass.__version__) + scss + '\n'

    _logger.info("Generating SCSS variables file ...")
    _logger.info(f"File path: {variables_scss_filepath}")

    with open(variables_scss_filepath, 'w') as f:
        f.write(data)


def _create_qss(main_scss_path, qss_filepath, header=HEADER_QSS):
    """Create a styles.qss file from qtsass."""

    data = ''

    _logger.info("Generating QSS file ...")
    _logger.info(f"SCSS path: {main_scss_path}")
    _logger.info(f"QSS path: {qss_filepath}")

    qtsass.compile_filename(main_scss_path, qss_filepath,
                            output_style='expanded')

    with open(qss_filepath, 'r') as f:
        data = f.read()

    data = header.format(qtsass.__version__) + data

    with open(qss_filepath, 'w') as f:
        f.write(data)

    return data


def create_qss(palette, base_path=PACKAGE_PATH):
    """Create variables files and run qtsass compilation.

    This function will use the structure that must contain::

        base_path
            [palette.ID]
                main.scss
            qss
                _styles.scss

    The structure after the execution will contain::

        base_path
            [palette.ID]
                _variables.scss
                [palette.ID]style.qss
                main.scss
            qss
                _styles.scss

    Args:
        palette (Palette): Palette class.
        base_path (str): Base path for the palette directory, required for
            custom palettes. Defaults to `PACKAGE_PATH`.

    Returns:
        str: Stylesheet in string format.
    """

    if palette.ID is None:
        _logger.error("A QDarkStyle palette requires an ID!")
        sys.exit(1)

    if not base_path:
        base_path = PACKAGE_PATH

    palette_path = os.path.join(base_path, palette.ID)
    _logger.info(f"Creating QSS for palette: '{palette.ID} ...")
    _logger.info(f"Palette path: {palette_path}")

    variables_scss_filepath = os.path.join(palette_path, VARIABLES_SCSS_FILE)
    main_scss_filepath = os.path.join(palette_path, MAIN_SCSS_FILE)
    qss_filepath = os.path.join(palette_path, palette.ID + QSS_FILE_SUFFIX)

    _create_scss_variables(variables_scss_filepath, palette)

    stylesheet = _create_qss(main_scss_filepath, qss_filepath)

    return stylesheet
