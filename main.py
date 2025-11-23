import sys
from PyQt6.QtWidgets import QApplication
from window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            color: #222;
            background-color: #fafafa;
            font-size: 14px;
        }

        QMainWindow {
            background-color: #fafafa;
        }

        QToolBar {
            background: #ffffff;
            border: none;
            padding: 2px;
        }

        QToolButton {
            background: transparent;
            border: none;
            padding: 6px;
            margin: 2px;
        }

        QToolButton:checked {
            background-color: #cfe3ff;
            border: 1px solid #6ca8ff;
            border-radius: 4px;
        }

        QToolButton:hover {
            background-color: #e0e0e0;
            border-radius: 4px;
        }

        QMenuBar {
            background-color: #ffffff;
            color: #222;
        }

        QMenuBar::item {
            background: transparent;
            padding: 4px 10px;
        }

        QMenuBar::item:selected {
            background: #d0d0d0;
        }

        QMenu {
            background-color: #ffffff;
            color: #222;
            border: 1px solid #c8c8c8;
        }

        QMenu::item {
            padding: 4px 20px;
        }

        QMenu::item:selected {
            background-color: #dce8ff;
        }

        QMenu::item:checked {
            background-color: #cfe3ff;
            font-weight: bold;
        }

        QPushButton {
            background: #e6e6e6;
            border: 1px solid #bfbfbf;
            border-radius: 4px;
            padding: 5px 10px;
        }

        QPushButton:hover {
            background: #dcdcdc;
        }
    """)

    win = MainWindow()

    win.show()
    app.exec()
