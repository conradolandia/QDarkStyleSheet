# -*- coding: utf-8 -*-
"""Test the qtsass is compiling the SCSS files to QSS."""

# Standard library imports
import shutil
from pathlib import Path

# Local imports
from qdarkstyle import QSS_PATH, STYLES_SCSS_FILE
from qdarkstyle.colorsystem import Blue, Gray
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette
from qdarkstyle.palette import Palette
from qdarkstyle.utils.scss import create_qss


def test_create_qss_dark():
    # Should not raise a CompileError
    create_qss(DarkPalette)


def test_create_qss_light():
    # Should not raise a CompileError
    create_qss(LightPalette)


def test_create_custom_qss(tmp_path):
    # Should not raise: CompileError, FileNotFoundError
    custom_palette = Palette.from_dict(
        {
            "ID": "custom",
            "COLOR_BACKGROUND_1": "#ff0000",
            "COLOR_BACKGROUND_2": "#cc0000",
            "COLOR_BACKGROUND_3": "#aa0000",
            "COLOR_BACKGROUND_4": "#00ff00",
            "COLOR_BACKGROUND_5": "#00cc00",
            "COLOR_BACKGROUND_6": "#00aa00",
            "COLOR_TEXT_1": "#0000ff",
            "COLOR_TEXT_2": "#0000cc",
            "COLOR_TEXT_3": "#0000aa",
            "COLOR_TEXT_4": "#0000aa",
            "OPACITY_TOOLTIP": 230,
            "SIZE_BORDER_RADIUS": "0px",
            "COLOR_ACCENT_1": Blue.B20,
            "COLOR_ACCENT_2": Blue.B40,
            "COLOR_ACCENT_3": Blue.B50,
            "COLOR_ACCENT_4": Blue.B70,
            "COLOR_ACCENT_5": Blue.B80,
            "COLOR_DISABLED": Gray.B70,
        },
        class_name="CustomPalette",
    )

    tmp_custom_path = tmp_path / "custom"
    tmp_custom_path.mkdir()
    main_scss = tmp_custom_path / "main.scss"
    main_scss.write_text(
        f"""
/* {custom_palette.ID} Style - QDarkStyleSheet ------------------------------------------ */

@import '_variables';
@import '../qss/_styles';

"""
    )
    qss_path = tmp_path / "qss"
    qss_path.mkdir()
    styles_scss_path = qss_path / STYLES_SCSS_FILE
    base_styles_scss_path = Path(QSS_PATH) / STYLES_SCSS_FILE
    shutil.copy(base_styles_scss_path, styles_scss_path)

    # Should not raise a CompileError/FileNotFoundError
    create_qss(
        custom_palette,
        base_path=tmp_path,
    )
