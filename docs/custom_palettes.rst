Custom Palettes Guide
=====================

This guide explains how to create and use custom palettes with QDarkStyleSheet. Custom palettes allow you to define completely custom color schemes with any theme name and ID.

Understanding Custom Palettes
-----------------------------

QDarkStyleSheet supports fully custom palettes with:

- **Custom ID**: Any string identifier you want (e.g., 'ocean', 'forest', 'neon')
- **Custom colors**: Complete freedom to define all colors
- **Custom color system**: Can use built-in colors or define your own
- **Generated resources**: CLI generates all necessary files (QSS, QRC, PNG icons)

**Important**: Custom palettes use a different workflow than the built-in dark/light themes. You cannot use `qdarkstyle.load_stylesheet()` with custom palettes. Instead, you use the generated QSS file directly.

Creating a Custom Palette
-------------------------

Basic Structure
~~~~~~~~~~~~~~~

All custom palettes must inherit from the ``Palette`` class:

.. code-block:: python

    from qdarkstyle.palette import Palette

    class OceanTheme(Palette):
        """Ocean-inspired custom theme."""
        
        # Custom ID - can be any string
        ID = 'ocean'
        
        # Background colors (customize as needed)
        COLOR_BACKGROUND_1 = '#0a1a2e'  # Deep ocean blue
        COLOR_BACKGROUND_2 = '#16213e'  # Dark blue
        COLOR_BACKGROUND_3 = '#1e2d4f'  # Medium blue
        COLOR_BACKGROUND_4 = '#253a5e'  # Lighter blue
        COLOR_BACKGROUND_5 = '#2d476d'  # Light blue
        COLOR_BACKGROUND_6 = '#35547c'  # Lightest blue
        
        # Text colors
        COLOR_TEXT_1 = '#e6f3ff'       # Almost white with blue tint
        COLOR_TEXT_2 = '#cce7ff'       # Light blue-white
        COLOR_TEXT_3 = '#99d6ff'       # Medium blue-white
        COLOR_TEXT_4 = '#66c5ff'       # Darker blue-white
        
        # Accent colors (for interactive elements)
        COLOR_ACCENT_1 = '#00d4ff'     # Bright cyan
        COLOR_ACCENT_2 = '#00b8e6'     # Medium cyan
        COLOR_ACCENT_3 = '#009ccc'     # Darker cyan
        COLOR_ACCENT_4 = '#0080b3'     # Dark cyan
        COLOR_ACCENT_5 = '#006699'     # Very dark cyan
        
        COLOR_DISABLED = '#4a6b8a'
        OPACITY_TOOLTIP = 230

Required Properties
~~~~~~~~~~~~~~~~~~~

Every custom palette must define these properties:

- **ID**: Any string identifier for your theme
- **Background Colors**: Six levels (COLOR_BACKGROUND_1 to COLOR_BACKGROUND_6)
- **Text Colors**: Four levels (COLOR_TEXT_1 to COLOR_TEXT_4)
- **Accent Colors**: Five levels (COLOR_ACCENT_1 to COLOR_ACCENT_5)
- **Disabled Color**: COLOR_DISABLED for disabled elements
- **Tooltip Opacity**: OPACITY_TOOLTIP (0-255)

Using Custom Color Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Option 1: Using Built-in Color Systems**

You can mix custom hex colors with the built-in color systems:

.. code-block:: python

    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray, Blue

    class ForestTheme(Palette):
        """Forest-inspired theme with custom and built-in colors."""
        
        ID = 'forest'
        
        # Mix custom colors with color system
        COLOR_BACKGROUND_1 = '#1a2f1a'      # Custom dark green
        COLOR_BACKGROUND_2 = '#2d4a2d'      # Custom medium green
        COLOR_BACKGROUND_3 = Gray.B30        # Built-in gray
        COLOR_BACKGROUND_4 = Gray.B40        # Built-in gray
        COLOR_BACKGROUND_5 = Gray.B50        # Built-in gray
        COLOR_BACKGROUND_6 = Gray.B60        # Built-in gray
        
        # Use built-in colors for consistency
        COLOR_TEXT_1 = Gray.B150
        COLOR_TEXT_2 = Gray.B140
        COLOR_TEXT_3 = Gray.B130
        COLOR_TEXT_4 = Gray.B120
        
        # Custom accent colors
        COLOR_ACCENT_1 = '#4ade80'
        COLOR_ACCENT_2 = '#22c55e'
        COLOR_ACCENT_3 = '#16a34a'
        COLOR_ACCENT_4 = '#15803d'
        COLOR_ACCENT_5 = '#166534'
        
        COLOR_DISABLED = Gray.B70
        OPACITY_TOOLTIP = 230

**Option 2: Creating Fully Custom Color Systems**

For complete control over all colors, you can create your own color system classes:

.. code-block:: python

    # custom_colors.py - Define your own color system
    class WarmColors:
        """Warm color palette system."""
        # Reds and oranges
        RED_DARK = '#8B0000'      # Dark red
        RED_MEDIUM = '#DC143C'    # Crimson
        RED_LIGHT = '#FF6347'     # Tomato
        
        ORANGE_DARK = '#FF4500'   # Orange red
        ORANGE_MEDIUM = '#FF8C00' # Dark orange
        ORANGE_LIGHT = '#FFA500'  # Orange
        
        # Yellows and warm neutrals
        YELLOW_DARK = '#DAA520'   # Goldenrod
        YELLOW_MEDIUM = '#FFD700' # Gold
        YELLOW_LIGHT = '#FFFF99' # Light yellow
        
        WARM_GRAY_1 = '#2F2F2F'   # Very dark gray
        WARM_GRAY_2 = '#4A4A4A'   # Dark gray
        WARM_GRAY_3 = '#6B6B6B'   # Medium gray
        WARM_GRAY_4 = '#8C8C8C'   # Light gray
        WARM_GRAY_5 = '#ADADAD'   # Very light gray
        
    class CoolColors:
        """Cool color palette system."""
        # Blues and greens
        BLUE_DARK = '#191970'     # Midnight blue
        BLUE_MEDIUM = '#4169E1'   # Royal blue
        BLUE_LIGHT = '#87CEEB'    # Sky blue
        
        GREEN_DARK = '#006400'    # Dark green
        GREEN_MEDIUM = '#228B22'  # Forest green
        GREEN_LIGHT = '#90EE90'   # Light green
        
        # Purples and cool neutrals
        PURPLE_DARK = '#4B0082'   # Indigo
        PURPLE_MEDIUM = '#8A2BE2' # Blue violet
        PURPLE_LIGHT = '#DDA0DD'  # Plum
        
        COOL_GRAY_1 = '#2E3440'   # Dark cool gray
        COOL_GRAY_2 = '#3B4252'   # Medium dark gray
        COOL_GRAY_3 = '#434C5E'   # Medium gray
        COOL_GRAY_4 = '#4C566A'   # Light gray
        COOL_GRAY_5 = '#5E81AC'   # Very light gray

Now use your custom color systems in your palette:

.. code-block:: python

    from qdarkstyle.palette import Palette
    from custom_colors import WarmColors, CoolColors

    class SunsetTheme(Palette):
        """Warm sunset-inspired theme using custom color system."""
        
        ID = 'sunset'
        
        # Use your custom warm colors
        COLOR_BACKGROUND_1 = WarmColors.WARM_GRAY_1    # Very dark background
        COLOR_BACKGROUND_2 = WarmColors.WARM_GRAY_2    # Dark background
        COLOR_BACKGROUND_3 = WarmColors.WARM_GRAY_3    # Medium background
        COLOR_BACKGROUND_4 = WarmColors.RED_DARK       # Dark red for raised elements
        COLOR_BACKGROUND_5 = WarmColors.ORANGE_DARK    # Orange for pressed elements
        COLOR_BACKGROUND_6 = WarmColors.ORANGE_MEDIUM  # Bright orange for hover
        
        # Warm text colors
        COLOR_TEXT_1 = WarmColors.YELLOW_LIGHT         # Primary text
        COLOR_TEXT_2 = WarmColors.YELLOW_MEDIUM        # Secondary text
        COLOR_TEXT_3 = WarmColors.ORANGE_LIGHT         # Tertiary text
        COLOR_TEXT_4 = WarmColors.WARM_GRAY_5          # Quaternary text
        
        # Warm accent colors
        COLOR_ACCENT_1 = WarmColors.RED_LIGHT          # Bright accent
        COLOR_ACCENT_2 = WarmColors.RED_MEDIUM         # Medium accent
        COLOR_ACCENT_3 = WarmColors.RED_DARK           # Dark accent
        COLOR_ACCENT_4 = WarmColors.ORANGE_DARK        # Darker accent
        COLOR_ACCENT_5 = WarmColors.WARM_GRAY_4        # Subtle accent
        
        COLOR_DISABLED = WarmColors.WARM_GRAY_3
        OPACITY_TOOLTIP = 230

**Why Use Custom Color Systems?**

- **Consistency**: Ensures all colors work harmoniously together
- **Maintainability**: Easy to update color schemes across multiple themes
- **Design System**: Creates a cohesive color language for your application
- **Flexibility**: Mix and match color systems for different themes

Complete Workflow
-----------------

1. Create Your Palette File
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a Python file with your custom palette:

.. code-block:: python

    # my_theme.py
    from qdarkstyle.palette import Palette

    class NeonTheme(Palette):
        """Cyberpunk neon theme."""
        
        ID = 'neon'
        
        # Dark backgrounds with neon accents
        COLOR_BACKGROUND_1 = '#0d0d0d'  # Almost black
        COLOR_BACKGROUND_2 = '#1a1a1a'  # Very dark gray
        COLOR_BACKGROUND_3 = '#262626'  # Dark gray
        COLOR_BACKGROUND_4 = '#333333'  # Medium gray
        COLOR_BACKGROUND_5 = '#404040'  # Light gray
        COLOR_BACKGROUND_6 = '#4d4d4d'  # Lighter gray
        
        # Bright text colors
        COLOR_TEXT_1 = '#ffffff'        # Pure white
        COLOR_TEXT_2 = '#e6e6e6'        # Light gray
        COLOR_TEXT_3 = '#cccccc'        # Medium gray
        COLOR_TEXT_4 = '#b3b3b3'        # Darker gray
        
        # Neon accent colors
        COLOR_ACCENT_1 = '#ff0080'      # Hot pink
        COLOR_ACCENT_2 = '#e6006b'      # Dark pink
        COLOR_ACCENT_3 = '#cc0066'      # Darker pink
        COLOR_ACCENT_4 = '#b30055'      # Very dark pink
        COLOR_ACCENT_5 = '#990044'      # Almost black pink
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 230

2. Generate Theme Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   **CRITICAL REQUIREMENT**: You MUST generate theme resources before using any custom palette. This process creates the necessary QSS stylesheets, PNG icons, and resource files with your custom colors. Custom palettes cannot be used without this step.

.. warning::
   **Asset Generation Required for Custom Color Systems**: When using custom color systems (like the WarmColors/CoolColors example above), the asset generation process will create PNG icons using your custom colors. This ensures that UI elements like checkboxes, arrows, and other icons match your color scheme.

Use the QDarkStyleSheet CLI to generate all necessary files:

.. code-block:: bash

    python -m qdarkstyle.utils \
        --custom-palette-file my_theme.py \
        --custom-palette-class-name NeonTheme \
        --base-path ./my_themes

This creates the complete theme structure:

.. code-block:: text

    my_themes/
    └── neon/                       # Your custom ID
        ├── neonstyle.qss          # Generated stylesheet
        ├── neonstyle.qrc          # Qt resource file
        ├── neonstyle_rc.py        # Python resource module
        ├── palette.py             # Your palette class
        ├── main.scss              # SCSS source
        ├── _variables.scss        # SCSS variables
        └── rc/                    # Generated PNG icons (150+ files)
            ├── arrow_down.png
            ├── checkbox_checked.png
            └── ... (all icons in your colors)

**What Happens During Asset Generation?**

The asset generation process does several critical things:

1. **Creates Colored Icons**: Takes the base SVG icons and generates PNG versions using your palette's colors
   
   - ``COLOR_ACCENT_2`` is used for pressed states
   - ``COLOR_ACCENT_5`` is used for focus states  
   - ``COLOR_BACKGROUND_4`` is used for disabled states
   - ``COLOR_TEXT_1`` is used for normal states

2. **Generates QSS Stylesheet**: Compiles SCSS variables with your colors into a complete QSS stylesheet

3. **Creates Resource Files**: Generates Qt resource files (.qrc) and Python resource modules (_rc.py) that bundle all assets

4. **Ensures Color Consistency**: All UI elements (backgrounds, text, icons, borders) use colors from your palette

**Without asset generation, your custom theme will not work** because:

- Icons will not match your color scheme
- Many UI elements depend on the generated PNG resources
- The QSS file contains references to generated resources

3. Use Your Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~

**Method 1: Load QSS file directly**

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    
    # Load your custom stylesheet directly
    with open('./my_themes/neon/neonstyle.qss', 'r') as f:
        stylesheet = f.read()
    
    app.setStyleSheet(stylesheet)
    
    window = QMainWindow()
    window.setWindowTitle("Neon Theme")
    window.show()
    
    app.exec_()

**Method 2: Import generated resources**

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtCore import QFile, QTextStream

    # Add your theme path
    sys.path.insert(0, './my_themes')
    
    # Import the generated resources
    import neon.neonstyle_rc  # This loads the resources
    
    app = QApplication(sys.argv)
    
    # Load stylesheet from resources
    qss_file = QFile(":/qdarkstyle/neon/neonstyle.qss")
    qss_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(qss_file)
    stylesheet = stream.readAll()
    
    app.setStyleSheet(stylesheet)
    
    window = QMainWindow()
    window.setWindowTitle("Neon Theme with Resources")
    window.show()
    
    app.exec_()

Advanced Examples
----------------

Multiple Theme Variants
~~~~~~~~~~~~~~~~~~~~~~~

You can create multiple variants of the same theme:

.. code-block:: python

    class RetroBlue(Palette):
        ID = 'retro_blue'
        # ... blue-themed colors
        
    class RetroGreen(Palette):
        ID = 'retro_green'
        # ... green-themed colors
        
    class RetroRed(Palette):
        ID = 'retro_red'
        # ... red-themed colors

Dynamic Theme Switching
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class ThemeManager:
        def __init__(self, app):
            self.app = app
            self.themes = {
                'ocean': './themes/ocean/oceanstyle.qss',
                'forest': './themes/forest/foreststyle.qss',
                'neon': './themes/neon/neonstyle.qss',
            }
        
        def apply_theme(self, theme_name):
            if theme_name in self.themes:
                with open(self.themes[theme_name], 'r') as f:
                    stylesheet = f.read()
                self.app.setStyleSheet(stylesheet)

High Contrast Accessibility Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class AccessibilityTheme(Palette):
        """High contrast theme for accessibility."""
        
        ID = 'accessibility'
        
        # Maximum contrast colors
        COLOR_BACKGROUND_1 = '#000000'  # Pure black
        COLOR_BACKGROUND_2 = '#1a1a1a'  # Very dark
        COLOR_BACKGROUND_3 = '#333333'  # Dark
        COLOR_BACKGROUND_4 = '#4d4d4d'  # Medium
        COLOR_BACKGROUND_5 = '#666666'  # Light
        COLOR_BACKGROUND_6 = '#808080'  # Lighter
        
        # High contrast text
        COLOR_TEXT_1 = '#ffffff'        # Pure white
        COLOR_TEXT_2 = '#f0f0f0'        # Almost white
        COLOR_TEXT_3 = '#e0e0e0'        # Light
        COLOR_TEXT_4 = '#d0d0d0'        # Medium light
        
        # Bright, distinguishable accents
        COLOR_ACCENT_1 = '#ffff00'      # Bright yellow
        COLOR_ACCENT_2 = '#ffcc00'      # Orange-yellow
        COLOR_ACCENT_3 = '#ff9900'      # Orange
        COLOR_ACCENT_4 = '#ff6600'      # Red-orange
        COLOR_ACCENT_5 = '#ff3300'      # Red
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 255

Testing Your Custom Theme
-------------------------

Complete Test Application
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                                QWidget, QPushButton, QLabel, QLineEdit, 
                                QCheckBox, QSlider, QProgressBar, QComboBox,
                                QTextEdit, QTabWidget, QGroupBox, QTableWidget,
                                QTableWidgetItem, QRadioButton, QSpinBox)
    from PyQt5.QtCore import Qt

    class CustomThemeTestWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Custom Theme Test")
            self.setGeometry(100, 100, 800, 600)
            
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            main_layout = QVBoxLayout(central_widget)
            
            # Test all widget types
            self.create_test_widgets(main_layout)
        
        def create_test_widgets(self, layout):
            # Basic widgets
            basic_group = QGroupBox("Basic Widgets")
            basic_layout = QVBoxLayout(basic_group)
            basic_layout.addWidget(QLabel("Test Label"))
            basic_layout.addWidget(QPushButton("Test Button"))
            basic_layout.addWidget(QCheckBox("Test Checkbox"))
            basic_layout.addWidget(QRadioButton("Test Radio"))
            layout.addWidget(basic_group)
            
            # Input widgets
            input_group = QGroupBox("Input Widgets")
            input_layout = QVBoxLayout(input_group)
            input_layout.addWidget(QLineEdit("Test Input"))
            input_layout.addWidget(QSpinBox())
            combo = QComboBox()
            combo.addItems(["Option 1", "Option 2", "Option 3"])
            input_layout.addWidget(combo)
            layout.addWidget(input_group)
            
            # Display widgets
            display_group = QGroupBox("Display Widgets")
            display_layout = QVBoxLayout(display_group)
            slider = QSlider(Qt.Horizontal)
            slider.setValue(50)
            display_layout.addWidget(slider)
            progress = QProgressBar()
            progress.setValue(75)
            display_layout.addWidget(progress)
            text_edit = QTextEdit("Multi-line text\\nSecond line\\nThird line")
            text_edit.setMaximumHeight(80)
            display_layout.addWidget(text_edit)
            layout.addWidget(display_group)

    def test_custom_theme(qss_file_path):
        app = QApplication(sys.argv)
        
        # Load custom theme
        with open(qss_file_path, 'r') as f:
            stylesheet = f.read()
        app.setStyleSheet(stylesheet)
        
        window = CustomThemeTestWindow()
        window.show()
        
        return app.exec_()

    if __name__ == '__main__':
        # Test your custom theme
        theme_file = './my_themes/neon/neonstyle.qss'
        sys.exit(test_custom_theme(theme_file))

Best Practices
-------------

Color Selection Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Background Hierarchy**: Use COLOR_BACKGROUND_1 for main areas, higher numbers for elevated surfaces
2. **Text Contrast**: Ensure sufficient contrast between text and background colors
3. **Accent Consistency**: Use COLOR_ACCENT_3 as primary selection color
4. **Accessibility**: Test with color vision deficiency simulators
5. **System Colors**: Consider using built-in color constants for consistency

Theme Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Design Phase**: Plan your color scheme with design tools
2. **Prototype**: Create palette class and generate initial theme
3. **Test**: Use the test application to verify all widgets
4. **Iterate**: Refine colors based on visual testing
5. **Validate**: Check accessibility and usability

File Management
~~~~~~~~~~~~~~

1. **Organization**: Keep themes in separate directories
2. **Version Control**: Track palette files and generated resources
3. **Documentation**: Document color choices and theme purpose
4. **Backup**: Maintain copies of working themes

Important Notes
--------------

Limitations and Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Cannot use with load_stylesheet()**: Custom palettes cannot be used with ``qdarkstyle.load_stylesheet()``. This function only works with the built-in DarkPalette and LightPalette.

**Resource Management**: Generated themes include resource files that must be properly imported if using Method 2.

**Path Management**: Ensure proper path handling when loading QSS files in different environments.

**Qt Binding Compatibility**: Generated resource files work with all Qt bindings (PyQt5, PyQt6, PySide2, PySide6).

Troubleshooting
--------------

Common Issues
~~~~~~~~~~~~

**Theme not loading**: Verify the QSS file path is correct and accessible.

**Icons not showing**: Ensure resource files are properly imported (Method 2) or use Method 1.

**Colors not applied**: Check that all required palette properties are defined.

**CLI generation fails**: Verify qtsass and watchdog are installed, and palette class is properly defined.

**Performance issues**: Large themes may take time to load; consider caching stylesheets.

Resources
---------

- **CLI Reference**: See :doc:`scripts/run_ui_css_edition` for command-line options
- **Color System**: See :doc:`color_reference` for built-in colors
- **API Reference**: See :doc:`reference/modules` for palette class details

**External Tools**:

- `Adobe Color <https://color.adobe.com/>`_ - Professional color palette generator
- `Coolors <https://coolors.co/>`_ - Fast color scheme generator
- `Material Design Colors <https://material.io/design/color/>`_ - Google's color system
- `WebAIM Contrast Checker <https://webaim.org/resources/contrastchecker/>`_ - Accessibility verification 
