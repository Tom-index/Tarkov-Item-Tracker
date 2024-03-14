from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel
from PySide6.QtGui import QFont, QPalette, QColor, Qt

import utils

class TarkovItemTracker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Tarkov Item Tracker")
        self.setMinimumSize(600, 400)

        # Layout Settings
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Entry field
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter item name...")
        self.line_edit.returnPressed.connect(self.handle_item_query)
        main_layout.addWidget(self.line_edit)

        # Results display area
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        font = QFont("Consolas", 10)
        self.text_edit.setFont(font)
        main_layout.addWidget(self.text_edit)

        # description label
        self.label = QLabel("Write the name of the item and press Enter.")
        font = QFont("Arial", 10)
        self.label.setFont(font)
        main_layout.addWidget(self.label)

        # Set background and text color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

    def handle_item_query(self):
        """
        Fetch data from the API based on the entered item name and display the result
        """
        item_name = self.line_edit.text()
        data = utils.run_query(item_name)

        if data and 'data' in data and 'items' in data['data']:
            items = data['data']['items']
            if items:
                item = items[0]
                html_text = f"<b>Item Name: {item['name']}</b><br/><br/>"
                html_text += f"<font face='Arial'>Last Low Price: {item['lastLowPrice']}<br/>"
                html_text += f"Avg Price (24h): {item['avg24hPrice']}<br/><br/><br/>"

                html_text += f"<b>Used in tasks:</b><br/>"
                if item['usedInTasks']:
                    for task in item['usedInTasks']:
                        kappa_required_str = "Required" if task['kappaRequired'] else "Not Required"
                        task_info = f"- {task['name']} (Kappa: {kappa_required_str}, Trader: {task['trader']['name']})"
                        if task['kappaRequired']:
                            html_text += f"<font color='green'>{task_info}</font><br/>"
                        else:
                            html_text += f"<font color='red'>{task_info}</font><br/>"
                else:
                    html_text += "<b>Not used in tasks</b><br/>"

                self.text_edit.setHtml(html_text)
            else:
                self.text_edit.setPlainText("No item found.")
        else:
            self.text_edit.setPlainText("Failed to fetch item data.")