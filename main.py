import os
import sys

import PySide6
from PySide6.QtWidgets import QApplication

from overlay import TarkovItemTracker

if __name__ == "__main__":
    # Set environment variables for PySide6
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    # Launch the application
    app = QApplication(sys.argv)
    window = TarkovItemTracker()
    window.show()
    sys.exit(app.exec())