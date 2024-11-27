import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout,
    QWidget, QToolBar, QStatusBar, QLabel, QListWidget, QTextEdit, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

"""
How It Looks
Menu Bar: At the top with "File" and "Help" menus.
Toolbar: Below the menu bar with "New," "Open," and "Exit" icons.
Side Panel: On the left with a list of items.
Main Panel: Centered, including a text area.
Footer: A small styled section at the bottom.
"""

class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Demo Application")
        self.setGeometry(100, 100, 800, 600)

        # Initialize UI components
        self.init_menu_bar()
        self.init_tool_bar()
        self.init_status_bar()
        self.init_layout()

    def init_menu_bar(self):
        # Create the menu bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)  # Close the app
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)

    def init_tool_bar(self):
        # Create a toolbar
        tool_bar = QToolBar("Main Toolbar", self)
        tool_bar.setMovable(False)  # Toolbar cannot be moved
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        # Add actions to the toolbar
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        tool_bar.addAction(new_action)
        tool_bar.addAction(open_action)
        tool_bar.addSeparator()
        tool_bar.addAction(exit_action)

    def init_status_bar(self):
        # Create a status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def init_layout(self):
        # Central widget with layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout structure
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Split into horizontal sections (side panel and main panel)
        horizontal_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_layout)

        # Side panel
        side_panel = QWidget()
        side_panel.setFixedWidth(200)
        side_layout = QVBoxLayout()
        side_panel.setLayout(side_layout)
        side_panel.setStyleSheet("background-color: #f0f0f0;")
        side_layout.addWidget(QLabel("Side Panel"))
        side_list = QListWidget()
        side_list.addItems(["Item 1", "Item 2", "Item 3"])
        side_layout.addWidget(side_list)
        horizontal_layout.addWidget(side_panel)

        # Main panel
        main_panel = QWidget()
        main_panel_layout = QVBoxLayout()
        main_panel.setLayout(main_panel_layout)
        main_panel.setStyleSheet("background-color: #ffffff;")
        main_panel_layout.addWidget(QLabel("Main Panel"))
        main_panel_layout.addWidget(QTextEdit())
        horizontal_layout.addWidget(main_panel)

        # Footer
        footer = QWidget()
        footer_layout = QHBoxLayout()
        footer.setLayout(footer_layout)
        footer.setStyleSheet("background-color: #e0e0e0;")
        footer_layout.addWidget(QLabel("Footer"), alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(footer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
