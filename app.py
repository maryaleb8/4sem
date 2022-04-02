#!/usr/bin/python3

import os.path as op
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def resource_path(res_name):
    return op.join(op.dirname(__file__), res_name)

MainFormUI, MainForm = uic.loadUiType(resource_path('main.ui'))

class MainWindow(MainForm):
    def __init__(self, parent=None):# constructor
        # Initialise base form
        super().__init__()
        # Create and Initialise UI elements
        self.ui = MainFormUI()
        self.ui.setupUi(self)

    def __del__(self): #деструктор
        self.ui = None #удаление указателя на ui чтобы удалилось то на что он ссылается

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
