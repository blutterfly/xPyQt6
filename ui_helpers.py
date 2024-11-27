from PyQt6.QtWidgets import QMenuBar, QToolBar, QStatusBar
from PyQt6.QtGui import QAction


def init_menu_bar(parent):
    """Initialize the menu bar."""
    menu_bar = QMenuBar(parent)

    # File Menu
    file_menu = menu_bar.addMenu("File")
    new_action = QAction("New", parent)
    open_action = QAction("Open", parent)
    exit_action = QAction("Exit", parent)
    exit_action.triggered.connect(parent.close)  # Close the app
    file_menu.addAction(new_action)
    file_menu.addAction(open_action)
    file_menu.addSeparator()
    file_menu.addAction(exit_action)

    # Help Menu
    help_menu = menu_bar.addMenu("Help")
    about_action = QAction("About", parent)
    help_menu.addAction(about_action)

    parent.setMenuBar(menu_bar)


def init_tool_bar(parent):
    """Initialize the toolbar."""
    tool_bar = QToolBar("Main Toolbar", parent)
    tool_bar.setMovable(False)  # Toolbar cannot be moved
    parent.addToolBar(tool_bar)

    # Add actions to the toolbar
    new_action = QAction("New", parent)
    open_action = QAction("Open", parent)
    exit_action = QAction("Exit", parent)
    exit_action.triggered.connect(parent.close)
    tool_bar.addAction(new_action)
    tool_bar.addAction(open_action)
    tool_bar.addSeparator()
    tool_bar.addAction(exit_action)


def init_status_bar(parent):
    """Initialize the status bar."""
    status_bar = QStatusBar(parent)
    parent.setStatusBar(status_bar)
    status_bar.showMessage("Ready")
