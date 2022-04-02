#!/usr/bin/python3

import os.path as op
import sqlite3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QListWidgetItem #<-класс всех строчек ну конкретно тут
from PyQt5 import uic

DB_PATH = '/tmp/test.s3db'

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
        # Attach event handlers
        self.ui.execute_button.clicked.connect(self.__execute)
        self.ui.query_history.itemDoubleClicked.connect(self.__edit)
        # Connect to our database:
        self.__dbc = sqlite3.connect(DB_PATH)

    def __del__(self): #деструктор
        self.ui = None #удаление указателя на ui чтобы удалилось то на что он ссылается
        self.__dbc.close()

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
        history.addItem(text)
        # Try to execute query:
        try:
            cur = self.__dbc.cursor()
            cur.execute(text)
            self.__dbc.commit()
            result = cur.fetchall()
            error = None
        except Exception as exc:
            result = None
            error = str(exc)
        # Display query result or error message:
        if error is None:
            # Add query to history and clear input box
            query.setText('')
            # Add query result if it's not empty:
            if len(result) == 0:
                return
            result_text = '<table border=l>'
            for row in result:
                result_text += '<tr>'
                result_text += ''.join(f'<td>{cell}</td>' for cell in row)
                result_text += '</tr>'
            result_text += '</table>'
        else:
            #FIXME: error могут быть особые символы, например, скобки
            # Let's display waring in red:
            result_text = f'<span style="color: red;"><b>{error}</b></span>'
        label = QLabel(result_text)
        list_item = QListWidgetItem()
        # Set proper dimensions for these wwidgets:
        label_size_hint = label.sizeHint()
        label.resize(label_size_hint)
        list_item.setSizeHint(label_size_hint)
        # Add widget to history:
        history.addItem(list_item)
        history.setItemWidget(list_item, label)

    def keyPressEvent(self, event): #что будет происходмть при назажии на энтр
        key = event.key()
        if key == Qt.Key_Return or key == Qt.Key_Enter:
            if self.ui.query_text.hasFocus():#если стоял курсор в вводе текста то выполняем
                self.__execute()
            elif self.ui.query_history.hasFocus():#если курсор стоял в истории редактируем
                self.__edit()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
