Custom Palettes Guide
=====================

This guide explains how to create and use custom palettes with QDarkStyleSheet. Custom palettes allow you to define your own color schemes while maintaining the consistent design language of QDarkStyleSheet.

Understanding the Palette System
--------------------------------

QDarkStyleSheet uses a palette-based approach for theming. A palette is a Python class that defines color variables, sizes, and other styling properties. The system includes:

- **Base Palette Class**: The foundation that all palettes inherit from
- **Built-in Palettes**: DarkPalette and LightPalette provided by QDarkStyleSheet
- **Custom Palettes**: User-defined palettes that extend the base system

The palette system ensures consistency across all Qt widgets while allowing complete customization of colors and styling properties.

Creating a Custom Palette
-------------------------

Basic Structure
~~~~~~~~~~~~~~~

All custom palettes must inherit from the ``Palette`` class:

.. code-block:: python

    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray, Blue

    class MyCustomPalette(Palette):
        """My custom color palette."""
        
        # Unique identifier for your palette
        ID = 'my_custom'
        
        # Background colors (lightest to darkest)
        COLOR_BACKGROUND_1 = '#2b2b2b'
        COLOR_BACKGROUND_2 = '#3c3c3c'
        COLOR_BACKGROUND_3 = '#4d4d4d'
        COLOR_BACKGROUND_4 = '#5e5e5e'
        COLOR_BACKGROUND_5 = '#6f6f6f'
        COLOR_BACKGROUND_6 = '#808080'
        
        # Text colors (primary to secondary)
        COLOR_TEXT_1 = '#ffffff'
        COLOR_TEXT_2 = '#e0e0e0'
        COLOR_TEXT_3 = '#c0c0c0'
        COLOR_TEXT_4 = '#a0a0a0'
        
        # Accent colors for interactive elements
        COLOR_ACCENT_1 = '#4a9eff'
        COLOR_ACCENT_2 = '#3a8eef'
        COLOR_ACCENT_3 = '#2a7edf'
        COLOR_ACCENT_4 = '#1a6ecf'
        COLOR_ACCENT_5 = '#0a5ebf'
        
        # Disabled elements
        COLOR_DISABLED = '#808080'
        
        # Tooltip opacity (0-255)
        OPACITY_TOOLTIP = 230

Required Properties
~~~~~~~~~~~~~~~~~~~

Every custom palette must define these properties:

- **ID**: A unique string identifier for your palette
- **Background Colors**: Six levels (COLOR_BACKGROUND_1 to COLOR_BACKGROUND_6)
- **Text Colors**: Four levels (COLOR_TEXT_1 to COLOR_TEXT_4)
- **Accent Colors**: Five levels (COLOR_ACCENT_1 to COLOR_ACCENT_5)
- **Disabled Color**: COLOR_DISABLED for disabled elements
- **Tooltip Opacity**: OPACITY_TOOLTIP (0-255)

Using the Color System
~~~~~~~~~~~~~~~~~~~~~~~

For better consistency, use the built-in color system:

.. code-block:: python

    from qdarkstyle.colorsystem import Gray, Blue, Green, Red, Orange, Yellow

    class SystemBasedPalette(Palette):
        """Palette using the built-in color system."""
        
        ID = 'system_based'
        
        # Using Gray scale
        COLOR_BACKGROUND_1 = Gray.B15
        COLOR_BACKGROUND_2 = Gray.B25
        COLOR_BACKGROUND_3 = Gray.B35
        COLOR_BACKGROUND_4 = Gray.B45
        COLOR_BACKGROUND_5 = Gray.B55
        COLOR_BACKGROUND_6 = Gray.B65
        
        # Using Blue for accents
        COLOR_ACCENT_1 = Blue.B30
        COLOR_ACCENT_2 = Blue.B40
        COLOR_ACCENT_3 = Blue.B50
        COLOR_ACCENT_4 = Blue.B60
        COLOR_ACCENT_5 = Blue.B70
        
        # Mix colors for special effects
        COLOR_TEXT_1 = Gray.B140
        COLOR_TEXT_2 = Gray.B120
        COLOR_TEXT_3 = Gray.B100
        COLOR_TEXT_4 = Gray.B80
        
        COLOR_DISABLED = Gray.B70
        OPACITY_TOOLTIP = 230

Using Custom Palettes
---------------------

Loading with load_stylesheet()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you've created your custom palette, use it with the ``load_stylesheet()`` function:

.. code-block:: python

    import qdarkstyle
    from my_palette import MyCustomPalette

    # Load your custom palette
    stylesheet = qdarkstyle.load_stylesheet(palette=MyCustomPalette)
    
    # Apply to your application
    app.setStyleSheet(stylesheet)

You can also combine it with specific Qt API:

.. code-block:: python

    # For specific Qt binding
    stylesheet = qdarkstyle.load_stylesheet(
        qt_api='pyqt5',
        palette=MyCustomPalette
    )

Complete Example
~~~~~~~~~~~~~~~~~

Here's a complete example of creating and using a custom palette:

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
    from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
    
    import qdarkstyle
    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray, Green

    class NaturePalette(Palette):
        """A nature-inspired green palette."""
        
        ID = 'nature'
        
        # Forest-inspired backgrounds
        COLOR_BACKGROUND_1 = '#1a2f1a'
        COLOR_BACKGROUND_2 = '#2d4a2d'
        COLOR_BACKGROUND_3 = '#406540'
        COLOR_BACKGROUND_4 = '#538053'
        COLOR_BACKGROUND_5 = '#669b66'
        COLOR_BACKGROUND_6 = '#79b679'
        
        # Light text on dark backgrounds
        COLOR_TEXT_1 = '#e8f5e8'
        COLOR_TEXT_2 = '#d4ead4'
        COLOR_TEXT_3 = '#c0dfc0'
        COLOR_TEXT_4 = '#acd4ac'
        
        # Green accents
        COLOR_ACCENT_1 = '#4ade80'
        COLOR_ACCENT_2 = '#22c55e'
        COLOR_ACCENT_3 = '#16a34a'
        COLOR_ACCENT_4 = '#15803d'
        COLOR_ACCENT_5 = '#166534'
        
        COLOR_DISABLED = Gray.B70
        OPACITY_TOOLTIP = 230

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Custom Palette Example")
            self.setGeometry(100, 100, 400, 300)
            
            # Create central widget
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            
            # Create layout
            layout = QVBoxLayout()
            central_widget.setLayout(layout)
            
            # Add widgets
            layout.addWidget(QLabel("Custom Nature Palette"))
            layout.addWidget(QLineEdit("Type something here..."))
            layout.addWidget(QPushButton("Click me!"))

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        
        # Apply custom palette
        stylesheet = qdarkstyle.load_stylesheet(palette=NaturePalette)
        app.setStyleSheet(stylesheet)
        
        window = MainWindow()
        window.show()
        
        sys.exit(app.exec_())

Advanced Palette Features
--------------------------

Dynamic Palette Creation
~~~~~~~~~~~~~~~~~~~~~~~~~

You can create palettes dynamically from dictionaries:

.. code-block:: python

    from qdarkstyle.palette import Palette

    # Define palette as dictionary
    palette_dict = {
        'ID': 'dynamic',
        'COLOR_BACKGROUND_1': '#1a1a1a',
        'COLOR_BACKGROUND_2': '#2a2a2a',
        # ... define all required colors
    }
    
    # Create palette class
    DynamicPalette = Palette.from_dict(palette_dict, class_name='DynamicPalette')
    
    # Use it
    stylesheet = qdarkstyle.load_stylesheet(palette=DynamicPalette)

Extending Existing Palettes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can extend existing palettes and modify only specific colors:

.. code-block:: python

    from qdarkstyle.dark.palette import DarkPalette
    from qdarkstyle.colorsystem import Red

    class DarkRedPalette(DarkPalette):
        """Dark palette with red accents."""
        
        ID = 'dark_red'
        
        # Override only accent colors
        COLOR_ACCENT_1 = Red.B30
        COLOR_ACCENT_2 = Red.B40
        COLOR_ACCENT_3 = Red.B50
        COLOR_ACCENT_4 = Red.B60
        COLOR_ACCENT_5 = Red.B70

Additional Styling Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add custom properties for specific widgets:

.. code-block:: python

    class ExtendedPalette(Palette):
        """Palette with additional styling properties."""
        
        ID = 'extended'
        
        # Standard palette properties...
        # (define all required colors)
        
        # Custom properties for specific widgets
        W_STATUS_BAR_BACKGROUND_COLOR = '#ff6b6b'
        W_TOOLBAR_SEPARATOR_COLOR = '#444444'
        W_MENU_ITEM_HOVER_COLOR = '#555555'
        
        # Custom border styles
        BORDER_THICK = '2px solid $COLOR_ACCENT_3'
        BORDER_DASHED = '1px dashed $COLOR_TEXT_3'

CLI Usage for Custom Palettes
-----------------------------

The QDarkStyleSheet CLI tools support custom palettes. You can generate all necessary files for your custom palette:

Basic Usage
~~~~~~~~~~~~

.. code-block:: bash

    # Generate resources for custom palette
    python -m qdarkstyle.utils \
        --custom-palette-file my_palette.py \
        --custom-palette-class-name MyCustomPalette

This generates:
- Image files (.png) in the palette directory
- QRC file for resources
- SCSS variables file
- QSS stylesheet file
- Compiled resource files

Advanced CLI Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Generate for specific Qt binding
    python -m qdarkstyle.utils \
        --custom-palette-file my_palette.py \
        --custom-palette-class-name MyCustomPalette \
        --create pyqt5

    # Generate with custom paths
    python -m qdarkstyle.utils \
        --custom-palette-file my_palette.py \
        --custom-palette-class-name MyCustomPalette \
        --base-path /path/to/custom/location \
        --palette-images

Best Practices
--------------

Color Selection
~~~~~~~~~~~~~~~~

1. **Maintain Contrast**: Ensure sufficient contrast between text and background colors
2. **Use the Color System**: Leverage the built-in Gray and Blue classes for consistency
3. **Test Accessibility**: Check that your palette works for users with color vision deficiencies
4. **Consider Context**: Different background levels serve different purposes in the UI

Palette Design
~~~~~~~~~~~~~~

1. **Background Hierarchy**: Use COLOR_BACKGROUND_1 for main backgrounds, higher numbers for elevated surfaces
2. **Text Hierarchy**: COLOR_TEXT_1 for primary text, higher numbers for secondary information
3. **Accent Colors**: Use for interactive elements, with COLOR_ACCENT_3 as the primary selection color
4. **Disabled State**: Ensure COLOR_DISABLED provides clear visual indication

Development Workflow
~~~~~~~~~~~~~~~~~~~~~

1. **Start Simple**: Begin with a basic palette and iterate
2. **Use CLI Tools**: Generate resources using the CLI for complete integration
3. **Test Thoroughly**: Test your palette with different widgets and states
4. **Version Control**: Keep your palette files in version control for team collaboration

Common Patterns
~~~~~~~~~~~~~~~

**High Contrast Palette**:

.. code-block:: python

    class HighContrastPalette(Palette):
        ID = 'high_contrast'
        
        # Pure black/white for maximum contrast
        COLOR_BACKGROUND_1 = '#000000'
        COLOR_BACKGROUND_2 = '#111111'
        COLOR_BACKGROUND_3 = '#222222'
        COLOR_BACKGROUND_4 = '#333333'
        COLOR_BACKGROUND_5 = '#444444'
        COLOR_BACKGROUND_6 = '#555555'
        
        COLOR_TEXT_1 = '#ffffff'
        COLOR_TEXT_2 = '#eeeeee'
        COLOR_TEXT_3 = '#dddddd'
        COLOR_TEXT_4 = '#cccccc'
        
        # Bright accent colors
        COLOR_ACCENT_1 = '#00ff00'
        COLOR_ACCENT_2 = '#00ee00'
        COLOR_ACCENT_3 = '#00dd00'
        COLOR_ACCENT_4 = '#00cc00'
        COLOR_ACCENT_5 = '#00bb00'
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 255

**Warm Palette**:

.. code-block:: python

    class WarmPalette(Palette):
        ID = 'warm'
        
        # Warm brown/orange backgrounds
        COLOR_BACKGROUND_1 = '#2d1b14'
        COLOR_BACKGROUND_2 = '#3d2518'
        COLOR_BACKGROUND_3 = '#4d2f1c'
        COLOR_BACKGROUND_4 = '#5d3920'
        COLOR_BACKGROUND_5 = '#6d4324'
        COLOR_BACKGROUND_6 = '#7d4d28'
        
        # Cream/light text
        COLOR_TEXT_1 = '#f5f0e8'
        COLOR_TEXT_2 = '#e8ddd0'
        COLOR_TEXT_3 = '#dbcab8'
        COLOR_TEXT_4 = '#ceb7a0'
        
        # Orange accents
        COLOR_ACCENT_1 = '#ff8c42'
        COLOR_ACCENT_2 = '#ff7a28'
        COLOR_ACCENT_3 = '#ff680e'
        COLOR_ACCENT_4 = '#f45600'
        COLOR_ACCENT_5 = '#e04400'
        
        COLOR_DISABLED = '#8b5a3c'
        OPACITY_TOOLTIP = 230

Troubleshooting
----------------

Common Issues
~~~~~~~~~~~~~~

**Palette Not Loading**:
- Ensure all required color properties are defined
- Check that the ID is unique and properly set
- Verify the palette class inherits from Palette

**Colors Not Applying**:
- Make sure you're using the correct color format (hex strings)
- Check that your custom palette is passed to load_stylesheet()
- Verify that the QApplication.setStyleSheet() is called after the palette is loaded

**CLI Generation Fails**:
- Ensure your palette file is in the Python path
- Check that the class name matches exactly
- Verify all required color properties are defined

**Resource Files Missing**:
- Run the CLI tools to generate all necessary files
- Check that the base SVG files exist in the svg/ directory
- Ensure write permissions in the target directory

Testing Your Palette
~~~~~~~~~~~~~~~~~~~~

Create a test script to verify your palette works correctly:

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
    from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QCheckBox
    from PyQt5.QtWidgets import QSlider, QProgressBar, QComboBox
    
    import qdarkstyle
    from my_palette import MyCustomPalette

    def test_palette():
        app = QApplication(sys.argv)
        
        # Apply your custom palette
        stylesheet = qdarkstyle.load_stylesheet(palette=MyCustomPalette)
        app.setStyleSheet(stylesheet)
        
        # Create test window with various widgets
        window = QWidget()
        window.setWindowTitle("Palette Test")
        window.resize(400, 300)
        
        layout = QVBoxLayout()
        window.setLayout(layout)
        
        # Test different widget types
        layout.addWidget(QLabel("Test Label"))
        layout.addWidget(QLineEdit("Test Input"))
        layout.addWidget(QPushButton("Test Button"))
        layout.addWidget(QCheckBox("Test Checkbox"))
        layout.addWidget(QSlider())
        layout.addWidget(QProgressBar())
        layout.addWidget(QComboBox())
        
        window.show()
        return app.exec_()

    if __name__ == '__main__':
        sys.exit(test_palette())

Resources
---------

- **Color Reference**: See :doc:`color_reference` for detailed color usage
- **CLI Tools**: See :doc:`scripts/qdarkstyle_utils` for command-line interface
- **API Reference**: See :doc:`reference/modules` for complete API documentation
- **Contributing**: See :doc:`contributing` for development guidelines

**External Resources**:
- `Material Design Color System <https://material.io/design/color/>`_
- `Adobe Color <https://color.adobe.com/>`_ - Color palette generator
- `Coolors <https://coolors.co/>`_ - Color scheme generator
- `WebAIM Color Contrast Checker <https://webaim.org/resources/contrastchecker/>`_ 
