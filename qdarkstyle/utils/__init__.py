# -*- coding: utf-8 -*-
"""
Utilities for processing SASS and images from default and custom palette.
"""

# Standard library imports
import logging
import os
import shutil
import sys

# Local imports
from qdarkstyle import (
    PACKAGE_PATH,
    SVG_PATH,
    IMAGES_PATH,
    MAIN_SCSS_FILE,
    QSS_PATH,
    STYLES_SCSS_FILE,
)
from qdarkstyle.utils.images import (
    compile_qrc_file,
    create_images,
    create_palette_image,
    generate_qrc_file,
)
from qdarkstyle.utils.scss import create_qss

_logger = logging.getLogger(__name__)


def process_palette(
    palette,
    compile_for="qtpy",
    base_svg_path=SVG_PATH,
    palette_images=True,
    palette_images_path=IMAGES_PATH,
    base_path=PACKAGE_PATH,
    resource_prefix="qss_icons",
    style_prefix="qdarkstyle",
):
    """Process palette class to create a new palette file/folders.

    It generates all files below, in this order:
        - Palette files (svg/.png) under docs/images/[palette_id]
        - Image files (.png) under [palette_id]/rc folder.
        - QRC file in [palette_id]/[palette_id]style.qrc (C++).
        - SCSS variables in [palette_id]/_variables.scss file.
        - QSS file in [palette_id]/[palette_id]style.qss.
        - Compiled QRC file in [palette_id]/[palette_id]style_rc.py

    Args:
        palette (Palette): Palette.
        compile_for (list, optional): Prefix used in resources.
            Defaults to 'qtpy'. Possible values are 'qtpy', 'pyqtgraph',
            'pyqt', 'pyqt5', 'pyqt6',
            'pyside', 'pyside2', 'pyside6',
            'qt', 'qt5', qt6, 'all'.
        base_svg_path (str, optional): Base path for the `.svg` source files.
            Defaults to `SVG_PATH`.
        base_path (str): Base path for the palette directory, required for
            custom palettes. Defaults to `PACKAGE_PATH`.
        palette_images (bool): If the preview palette images should be generated
            or not. Default False. See `palette_images_path` to set the path
            were files will be created.
        palette_images_path (str): Path to save generated image files
            (`palette.svg` and `palette.png`). Defaults to `IMAGES_PATH`.
        resource_prefix (str, optional): Prefix used in resources.
            Defaults to 'qss_icons'.
        style_prefix (str, optional): Prefix used to this style.
            Defaults to 'qdarkstyle'.
    """

    if palette is None:
        _logger.error(
            "Please pass a palette class in order to create its "
            "associated images"
        )
        sys.exit(1)

    if palette.ID is None:
        _logger.error("A QDarkStyle palette requires an ID!")
        sys.exit(1)

    id_ = palette.ID
    _logger.info(f"-- PROCESSING THEME: {id_}")

    # Create base palette directory and files from id
    palette_path = os.path.join(base_path, id_)
    if not os.path.exists(palette_path):
        os.mkdir(palette_path)

    init_path = os.path.join(palette_path, "__init__.py")
    if not os.path.isfile(init_path):
        with open(init_path, mode="x"):
            pass

    palette_file_path = os.path.join(palette_path, "palette.py")
    if not os.path.isfile(palette_file_path):
        with open(palette_file_path, mode="w") as palette_file:
            palette_file.write("from qdarkstyle.palette import Palette\n\n\n")
            palette_file.write(f"class {palette.__name__}(Palette):\n")
            palette_file.write(f'    """{palette.__name__} palette variables."""\n\n')
            for attr, value in palette.to_dict().items():
                if attr in ["ID", "OPACITY_TOOLTIP"]:
                    palette_file.write(f"    {attr} = {value}\n")
                else:
                    palette_file.write(f'    {attr} = "{value}"\n')

    qss_path = os.path.join(base_path, "qss")
    if not os.path.exists(qss_path):
        os.mkdir(qss_path)

    main_scss_path = os.path.join(palette_path, MAIN_SCSS_FILE)
    if not os.path.exists(main_scss_path):
        # Create basic `main.scss` file for custom path
        with open(main_scss_path, "w") as main_scss:
            main_scss.write(f"""
/* {id_} Style - QDarkStyleSheet ------------------------------------------ */

@import '_variables';
@import '../qss/_styles';

""")

    styles_scss_path = os.path.join(qss_path, STYLES_SCSS_FILE)
    if not os.path.exists(styles_scss_path):
        # Copy `qss/_styles.scss` file to custom path
        base_styles_scss_path = os.path.join(QSS_PATH, STYLES_SCSS_FILE)
        shutil.copy(base_styles_scss_path, styles_scss_path)

    # TODO: delete/remove all files and folders to ensure that old files
    # are not used if required

    if palette_images:
        _logger.info(f"-- GENERATING PALETTE IMAGE FOR: {id_}")
        create_palette_image(
            palette=palette, base_svg_path=base_svg_path, path=palette_images_path
        )

    _logger.info(f"-- GENERATING IMAGE FILES (.svg > .png) FOR: {id_}")
    create_images(
        base_svg_path=base_svg_path, base_path=base_path, palette=palette
    )

    _logger.info(f"-- GENERATING QRC FILE FOR: {id_}")
    generate_qrc_file(
        resource_prefix=resource_prefix,
        style_prefix=style_prefix,
        palette=palette,
        base_path=base_path,
    )

    _logger.info(f"-- GENERATING QSS FILE (.scss > .qss) FOR: {id_}")
    create_qss(palette=palette, base_path=base_path)

    _logger.info(f"-- CONVERTING RESOURCE FILE (. qrc > _rc.py/.rcc) FOR: {id_}")
    compile_qrc_file(
        compile_for=compile_for,
        palette=palette,
        base_path=base_path,
    )
