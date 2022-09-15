import sys
import os
import random

from PySide6 import QtCore, QtWidgets, QtGui

from PySide6.QtCore import *
from PySide6.QtWidgets import *

_placeholder =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam fermentum nisl est, eu cursus mi bibendum sit amet. Nullam nisl metus, pharetra ac elit et, mattis eleifend dolor. In tempor leo eu justo tincidunt tristique. Donec id maximus nulla, sed suscipit ante. Sed facilisis fringilla enim, a pharetra nisi. Etiam auctor maximus ullamcorper. Nam sollicitudin gravida lectus, et lacinia nulla tristique sit amet. In laoreet porttitor leo sed laoreet. In arcu erat, faucibus sit amet posuere bibendum, dignissim at ante."

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        text_widget = QLabel(_placeholder)
        text_widget.setWordWrap(True)
        text_widget.setAlignment(Qt.AlignCenter)
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)


        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.setWindowTitle("Hello, world!")

    with open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    w.resize(800, 600)
    w.show()

    sys.exit(app.exec())
