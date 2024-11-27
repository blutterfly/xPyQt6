import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QToolBar,
    QStatusBar, QLabel, QListWidget, QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Demo Application")
        self.setGeometry(100, 100, 800, 600)

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f9f9f9;
            }
            QMenuBar {
                background-color: #4CAF50;
                color: white;
            }
            QMenuBar::item {
                background-color: #4CAF50;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #45a049;
            }
            QToolBar {
                background-color: #333333;
                color: white;
                border: none;
            }
            QStatusBar {
                background-color: #4CAF50;
                color: white;
            }
            QWidget#SidePanel {
                background-color: #f0f0f0;
                border: 1px solid #cccccc;
            }
            QWidget#MainPanel {
                background-color: #ffffff;
                border: 1px solid #cccccc;
            }
            QWidget#Footer {
                background-color: #333333;
                color: white;
            }
            QListWidget {
                background-color: #ffffff;
                border: none;
            }
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
            }
        """)

        # Initialize UI components
        self.init_menu_bar()
        self.init_tool_bar()
        self.init_status_bar()
        self.init_layout()

    def init_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)

    def init_tool_bar(self):
        tool_bar = QToolBar("Main Toolbar", self)
        tool_bar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        tool_bar.addAction(new_action)
        tool_bar.addAction(open_action)
        tool_bar.addSeparator()
        tool_bar.addAction(exit_action)

    def init_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def init_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        horizontal_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_layout)

        # Side Panel
        side_panel = QWidget()
        side_panel.setObjectName("SidePanel")
        side_panel.setFixedWidth(200)
        side_layout = QVBoxLayout()
        side_panel.setLayout(side_layout)
        side_layout.addWidget(QLabel("Side Panel"))
        side_list = QListWidget()
        side_list.addItems(["Fruits", "Cars", "Students"])
        side_layout.addWidget(side_list)
        horizontal_layout.addWidget(side_panel)

        # Main Panel
        main_panel = QWidget()
        main_panel.setObjectName("MainPanel")
        main_panel_layout = QVBoxLayout()
        main_panel.setLayout(main_panel_layout)
        main_panel_layout.addWidget(QLabel("Main Panel"))
        main_panel_layout.addWidget(QTextEdit())
        horizontal_layout.addWidget(main_panel)

        # Footer
        footer = QWidget()
        footer.setObjectName("Footer")
        footer_layout = QHBoxLayout()
        footer.setLayout(footer_layout)
        footer_layout.addWidget(QLabel("Footer"), alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(footer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
