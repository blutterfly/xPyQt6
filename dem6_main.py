import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QListWidget, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem
)
from ui_helpers import init_menu_bar, init_tool_bar, init_status_bar


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
            "Stocks": "Click a button below to view data:",
        }

        # Mapping for CSV files
        self.csv_files = {
            "S&P 500": "data/summary/wikipedia_sp500.csv",
            "Nasdaq Composite": "data/summary/wikipedia_nasdaq.csv",
            "Dow Jones": "data/summary/wikipedia_dowjones.csv",
        }

        # Initialize UI components
        init_menu_bar(self)
        init_tool_bar(self)
        init_status_bar(self)
        self.init_layout()

    def init_layout(self):
        """Initialize the layout."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        horizontal_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_layout)

        # Side Panel
        side_panel = self.create_side_panel()
        horizontal_layout.addWidget(side_panel)

        # Main Panel
        self.main_panel, self.button_layout = self.create_main_panel()
        horizontal_layout.addWidget(self.main_panel)

        # Stocks Panel (for CSV display)
        self.stocks_panel = QTableWidget()
        main_layout.addWidget(self.stocks_panel)

    def create_side_panel(self):
        """Create the side panel."""
        side_panel = QWidget()
        side_panel.setFixedWidth(200)
        side_layout = QVBoxLayout()
        side_panel.setLayout(side_layout)

        side_layout.addWidget(QLabel("Side Panel"))

        side_list = QListWidget()
        side_list.addItems(self.data.keys())
        side_list.itemClicked.connect(self.display_items_in_main_panel)
        side_layout.addWidget(side_list)

        return side_panel

    def create_main_panel(self):
        """Create the main panel with buttons."""
        main_panel = QWidget()
        main_panel_layout = QVBoxLayout()
        main_panel.setLayout(main_panel_layout)

        main_panel_label = QLabel("Main Panel")
        main_panel_text = QTextEdit()
        main_panel_text.setReadOnly(True)
        button_layout = QHBoxLayout()

        main_panel_layout.addWidget(main_panel_label)
        main_panel_layout.addWidget(main_panel_text)
        main_panel_layout.addLayout(button_layout)

        # Create buttons for stock indexes
        for index_name in self.csv_files.keys():
            button = QPushButton(index_name)
            button.clicked.connect(lambda checked, name=index_name: self.display_csv_in_stocks_panel(name))
            button_layout.addWidget(button)

        self.main_panel_label = main_panel_label
        self.main_panel_text = main_panel_text

        return main_panel, button_layout

    def display_items_in_main_panel(self, item):
        """Display the objects or overview related to the clicked side panel item."""
        category = item.text()
        if category == "Stocks":
            self.main_panel_label.setText("Main Panel: Stocks")
            self.main_panel_text.setText(self.data["Stocks"])
        else:
            self.main_panel_label.setText(f"Main Panel: {category}")
            self.main_panel_text.setText("\n".join(self.data.get(category, [])))

    def display_csv_in_stocks_panel(self, index_name):
        """Read the corresponding CSV file and display it in the Stocks Panel."""
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
