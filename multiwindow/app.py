#!/usr/bin/python3

import os.path as op
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def load_form(form_name):
    return uic.loadUiType(op.join(op.dirname(__file__), form_name))

MainFormUI, MainForm = load_form('main.ui')
FirstFormUI, FirstFormBase = load_form('form_one.ui')
SecondFormUI, SecondFormBase = load_form('form_two.ui')

class MainWindow(MainForm):
    def __init__(self, parent=None):
        # Initialize base form:
        super().__init__(parent)
        # Create and initialize UI elements:
        self.ui = MainFormUI()
        self.ui.setupUi(self)
        #start with form 1
        self.__current_form = FirstForm(self)
        self.ui.grid.addWidget(self.__current_form)

    def __del__(self):
        self.ui = None


    def replace_form(self, new_form):
        new_form.setParent(self)
        self.ui.grid.replaceWidget(self.__current_form, new_form)
        self.__current_form.setParent(None)
        self.__current_form = new_form

class FirstForm(FirstFormBase):
    __instance = None

    @classmethod #можифицирует следующую функцию, она будет для всего класса, а не для экземпляра
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    def __init__(self, parent=None):
        #singleton pattern
        cls = type(self)
        if cls.__instance is not None:
            raise Exception('attempt to create second instance')
        cls.__instance = self
        # Initialize base form:
        super().__init__(parent)
        # Create and initialize UI elements:
        self.ui = FirstFormUI()
        self.ui.setupUi(self)
        # Attach event handlers:
        self.ui.switch_button.clicked.connect(self.__switch_to_form_two)

    def __del__(self):
        self.ui = None

    def __switch_to_form_two(self):
        parent = self.parent()
        parent.replace_form(SecondForm.get_instance())

class SecondForm(SecondFormBase):
    __instance = None

    @classmethod #можифицирует следующую функцию, она будет для всего класса, а не для экземпляра
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    def __init__(self, parent=None):
        #singleton pattern
        cls = type(self)
        if cls.__instance is not None:
            raise Exception('attempt to create second instance')
        cls.__instance = self
        # Initialize base form:
        super().__init__()
        # Create and initialize UI elements:
        self.ui = SecondFormUI()
        self.ui.setupUi(self)
        # Attach event handlers:
        self.ui.switch_button.clicked.connect(self.__switch_to_form_one)

    def __del__(self):
        self.ui = None

    def __switch_to_form_one(self):
        self.parent().replace_form(FirstForm.get_instance())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
