# -*- coding: utf-8 -*-
"""Script to process QRC files (convert .qrc to _rc.py and .rcc).

The script will attempt to compile the qrc file using the following tools:

    - `pyside6-rcc` for PySide6 and QtPy (Python) (Official)
    - There is no specific rcc compiler for PyQt6, use `pyside6-rcc` (Python)
    - `pyrcc5` for PyQt5 (Python)
    - `pyside2-rcc` for PySide2 (Python)
    - `rcc` for Qt5/Qt6 (C++)

Delete the compiled files that you don't want to use manually after
running this script.

Links to understand those tools:

    - `pyside6-rcc`: https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html (Official)
    - `pyrcc5`: http://pyqt.sourceforge.net/Docs/PyQt5/resources.html#pyrcc5
    - `pyside2-rcc: https://doc.qt.io/qtforpython/overviews/resources.html (Documentation Incomplete)
    - `rcc` on Qt6: https://doc.qt.io/qt-6/resources.html
    - `rcc` on Qt5: http://doc.qt.io/qt-5/rcc.html

"""

# Standard library imports
import argparse
import importlib.util
import logging
import sys

# Third party imports
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Local imports
from qdarkstyle import PACKAGE_PATH, SVG_PATH, IMAGES_PATH
from qdarkstyle.palette import Palette
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette
from qdarkstyle.utils import process_palette

_logger = logging.getLogger(__name__)


class QSSFileHandler(FileSystemEventHandler):
    """QSS File observer."""

    def __init__(self, parser_args):
        """QSS File observer."""
        super(QSSFileHandler, self).__init__()
        self.args = parser_args

    def on_modified(self, event):
        """Handle file system events."""
        if event.src_path.endswith('.qss'):
            # TODO: needs implementation for new palettes
            for palette in [DarkPalette, LightPalette]:
                process_palette(palette=palette, compile_for=self.args.create)
            print('\n')


# Based on https://sumit-ghosh.com/posts/parsing-dictionary-key-value-pairs-kwargs-argparse-python/
class CustomPaletteParser(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value


def import_from_file(module_name, file_path):
    # Taken from: https://gist.github.com/mportesdev/afb2ec26021ccabee0f67d6f7d18be3f
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def main():
    """Process QRC files."""
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--base_path",
        default=PACKAGE_PATH,
        type=str,
        help="Base QRC file directory.",
    )
    parser.add_argument(
        "--base_svg_path",
        default=SVG_PATH,
        type=str,
        help="Base path were source .svg files are located.",
    )
    parser.add_argument(
        "--images_path",
        default=IMAGES_PATH,
        type=str,
        help="Path were documentation images are located.",
    )
    parser.add_argument(
        "--resource_prefix",
        default="qdarkstyle",
        type=str,
        help="Prefix used to this style.",
    )
    parser.add_argument(
        "--style_prefix",
        default="qss_icons",
        type=str,
        help="Prefix used in resources.",
    )
    parser.add_argument(
        "--custom_palette_key_value",
        nargs="*",
        action=CustomPaletteParser,
        help="List of `key=value` definitions for a custom palette. "
             "Alternative to `--custom_palette_file` + "
             "`--custom_palette_class_name` args.",
    )
    parser.add_argument(
        "--custom_palette_file",
        type=str,
        help="Path to a Python file with the custom Palette subclass "
             "definition. Alternative to `--custom_palette_key_value` arg. "
             "Needs to be used alongside `--custom_palette_class_name` "
             "to work.",
    )
    parser.add_argument(
        "--custom_palette_class_name",
        type=str,
        help="Class name importable from the given Python file with the custom "
             "Palette subclass definition. Alternative to "
             "`--custom_palette_key_value` arg. Needs to be used alongside "
             "`--custom_palette_file` to work.",
    )
    parser.add_argument(
        "--create",
        default="qtpy",
        choices=[
            "pyqt5",
            "pyqt6",
            "pyside2",
            "pyside6",
            "qtpy",
            "pyqtgraph",
            "qt",
            "qt5",
            "all",
        ],
        type=str,
        help="Choose which one would be generated.",
    )
    parser.add_argument(
        "--watch", "-w", action="store_true", help="Watch for file changes."
    )

    args = parser.parse_args()

    if args.watch:
        path = PACKAGE_PATH
        observer = Observer()
        handler = QSSFileHandler(parser_args=args)
        observer.schedule(handler, path, recursive=True)
        try:
            print("\nWatching QSS file for changes...\nPress Ctrl+C to exit\n")
            observer.start()
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif args.custom_palette_key_value:
        process_palette(
            palette=Palette.from_dict(
                args.custom_palette,
                class_name=f'{args.custom_palette["ID"].capitalize()}Palette',
            ),
            compile_for=args.create,
            base_svg_path=args.base_svg_path,
            images_path=args.images_path,
            base_path=args.base_path,
        )
    elif args.custom_palette_file and args.custom_palette_class_name:
        custom_palette_module = import_from_file(
            "palette", args.custom_palette_file,
        )
        custom_palette_class = getattr(
            custom_palette_module, args.custom_palette_class_name,
        )
        process_palette(
            palette=custom_palette_class,
            compile_for=args.create,
            base_svg_path=args.base_svg_path,
            images_path=args.images_path,
            base_path=args.base_path,
        )
    else:
        for palette in [DarkPalette, LightPalette]:
            process_palette(
                palette=palette,
                compile_for=args.create,
                base_svg_path=args.base_svg_path,
                images_path=args.images_path,
                base_path=args.base_path,
            )


if __name__ == "__main__":
    sys.exit(main())
