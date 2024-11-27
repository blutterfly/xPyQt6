import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QToolBar,
    QStatusBar, QLabel, QListWidget, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Demo Application")
        self.setGeometry(100, 100, 800, 600)

        # Data for side panel items
        self.data = {
            "Fruits": ["Apple", "Banana", "Cherry"],
            "Cars": ["Toyota", "Ford", "BMW"],
            "Students": ["Alice", "Bob", "Charlie"],
            "Stocks": """
                **Click a button below to view data:**
            """,
        }

        # Mapping for CSV files
        self.csv_files = {
            "S&P 500": "data/summary/wikipedia_sp500.csv",
            "Nasdaq Composite": "data/summary/wikipedia_nasdaq.csv",
            "Dow Jones": "data/summary/wikipedia_dowjones.csv",
        }

        # Apply styles and initialize UI
        self.init_menu_bar()
        self.init_tool_bar()
        self.init_status_bar()
        self.init_layout()

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

        # Side List
        side_list = QListWidget()
        side_list.addItems(self.data.keys())
        side_list.itemClicked.connect(self.display_items_in_main_panel)
        side_layout.addWidget(side_list)
        horizontal_layout.addWidget(side_panel)

        # Main Panel
        self.main_panel = QWidget()
        self.main_panel.setObjectName("MainPanel")
        main_panel_layout = QVBoxLayout()
        self.main_panel.setLayout(main_panel_layout)

        # Main Panel Label and Buttons
        self.main_panel_label = QLabel("Main Panel")
        self.main_panel_text = QTextEdit()
        self.main_panel_text.setReadOnly(True)
        self.button_layout = QHBoxLayout()

        # Buttons for Stock Indexes
        self.create_stock_buttons()

        main_panel_layout.addWidget(self.main_panel_label)
        main_panel_layout.addWidget(self.main_panel_text)
        main_panel_layout.addLayout(self.button_layout)
        horizontal_layout.addWidget(self.main_panel)

        # Stocks Panel (for CSV display)
        self.stocks_panel = QTableWidget()
        main_layout.addWidget(self.stocks_panel)

    def create_stock_buttons(self):
        #"""Create buttons for S&P 500, Nasdaq, and Dow Jones."""
        for index_name in self.csv_files.keys():
            button = QPushButton(index_name)
            button.clicked.connect(lambda checked, name=index_name: self.display_csv_in_stocks_panel(name))
            self.button_layout.addWidget(button)

    def display_items_in_main_panel(self, item):
        """Display the objects or overview related to the clicked side panel item."""
        category = item.text()
        if category == "Stocks":
            self.main_panel_label.setText("Main Panel: Stocks")
            self.main_panel_text.setText(self.data["Stocks"].strip())
        else:
            self.main_panel_label.setText(f"Main Panel: {category}")
            self.main_panel_text.setText("\n".join(self.data.get(category, [])))

    def display_csv_in_stocks_panel(self, index_name):
        """
S&P 500:
Tracks the performance of 500 large publicly traded companies in the US.

Nasdaq 100:
Includes over stocks listed on the Nasdaq stock exchange.
Known for its heavy representation of technology and growth companies.

Dow Jones Industrial Average (DJIA):
Averages the stock prices of 30 significant publicly traded companies in the U.S.
Represents blue-chip companies and is a narrower index.
"""
        file_path = self.csv_files.get(index_name)
        if not file_path:
            return

        try:
            # Load CSV file using pandas
            df = pd.read_csv(file_path)

            # Display in the QTableWidget
            self.stocks_panel.setRowCount(len(df))
            self.stocks_panel.setColumnCount(len(df.columns))
            self.stocks_panel.setHorizontalHeaderLabels(df.columns)

            for row_idx, row in df.iterrows():
                for col_idx, value in enumerate(row):
                    self.stocks_panel.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except FileNotFoundError:
            self.main_panel_text.setText(f"File not found: {file_path}")
        except Exception as e:
            self.main_panel_text.setText(f"Error: {e}")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
