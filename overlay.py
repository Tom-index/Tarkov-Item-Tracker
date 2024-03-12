from PySide6.QtWidgets import QWidget, QLineEdit, QTextEdit, QLabel

import utils


class TarkovItemTracker(QWidget):
    """
    The main window for the Tarkov Item Tracker application
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        xpos = 200
        ypos = 150
        window_width = 400
        window_height = 250

        self.setGeometry(xpos, ypos, window_width, window_height)
        self.setFixedSize(window_width, window_height)

        self.setWindowTitle("Tarkov Item Tracker")

        self.setup_text_edit()
        self.setup_line_edit()
        self.setup_labels()

    def setup_text_edit(self):
        """
        Set up the QTextEdit widget for displaying results
        """
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.move(0, 50)
        self.text_edit.resize(400, 175)
        self.text_edit.setPlainText("Result will be displayed here.")

    def setup_line_edit(self):
        """
        Set up the QLineEdit widget for entering item names
        """
        self.line_edit = QLineEdit(self)
        self.line_edit.move(10, 10)
        self.line_edit.resize(200, 25)
        self.line_edit.returnPressed.connect(self.handle_item_query)

    def setup_labels(self):
        """
        Set up the QLabel widget for displaying instructions
        """
        self.input_label = QLabel(self)
        self.input_label.setWordWrap(True)  # Enable automatic line wrapping
        self.input_label.setText("Write the name of the item and press enter.")
        self.input_label.move(250, 10)

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
                info = f"Name: {item['name']}\nLast Low Price: {item['lastLowPrice']}\n\nUsed in Tasks:"
                for task in item['usedInTasks']:
                    info += f"\n- {task['name']} (Kappa: {task['kappaRequired']}, Trader: {task['trader']['name']})"
                self.text_edit.setPlainText(info)
            else:
                self.text_edit.setPlainText("No item found.")
        else:
            self.text_edit.setPlainText("Failed to fetch item data.")