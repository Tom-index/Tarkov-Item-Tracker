from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel, QSizePolicy
from PySide6.QtGui import QFont, QPalette, QColor,Qt

import utils


class TarkovItemTracker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Tarkov Item Tracker")
        self.setMinimumSize(600, 400)

        # レイアウトの設定
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 入力フィールド
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter item name...")
        self.line_edit.returnPressed.connect(self.handle_item_query)
        main_layout.addWidget(self.line_edit)

        # 結果表示エリア
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        font = QFont("Consolas", 10)
        self.text_edit.setFont(font)
        main_layout.addWidget(self.text_edit)

        # 説明ラベル
        self.label = QLabel("Write the name of the item and press Enter.")
        font = QFont("Arial", 10)
        self.label.setFont(font)
        main_layout.addWidget(self.label)

        # 背景色とテキストカラーの設定
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
                info = f"Name: {item['name']}\nLast Low Price: {item['lastLowPrice']}\n\nUsed in Tasks:"
                for task in item['usedInTasks']:
                    info += f"\n- {task['name']} (Kappa: {task['kappaRequired']}, Trader: {task['trader']['name']})"
                self.text_edit.setPlainText(info)
            else:
                self.text_edit.setPlainText("No item found.")
        else:
            self.text_edit.setPlainText("Failed to fetch item data.")