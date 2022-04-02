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
        self.ui = MainFormUI() #создали экземпляр MainFormUI() скобки означают создание
        self.ui.setupUi(self)
        #attach event handlers
        self.ui.execute_button.clicked.connect(self.__execute)
        self.ui.query_history.itemDoubleClicked.connect(self.__edit)

    def __del__(self): #деструктор
        self.ui = None #удаление указателя на ui чтобы удалилось то на что он ссылается

    def __edit(self):#редактирование прошлого запроса
        item = self.ui.query_history.currentItem()#если кликнули а это не текст, а лабуда
        if item is None:
            return
        self.ui.query_text.setText(item.text()) #кликнутый попадает в бокс для редактирования

    def __execute(self): #приватный тк есть подчеркивания, видно только из методов этого класса
        query = self.ui.query_text
        history = self.ui.query_history
        #fetch query text, ignore empty query:
        text = query.text().strip() #get text from string in window, delete whitespace
        if len(text) == 0: #если ничего после обрезания пробелов не осталось тоже ничего не делаем
            return
        # add query to history:
        history.addItem(text)
        #clear input box
        query.setText('')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
