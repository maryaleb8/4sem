#!/usr/bin/env python3
from functools import partial #частичное выполнение для функций
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton)

N, M = 2, 3

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__grid = QGridLayout()
        self.__button = []
        self.setLayout(self.__grid)
        for r in range(N):
            buttons_row = []
            for c in range(M):
                button = QPushButton(f'{r} {c}', self)# 2-какой оконный элемент является его родителем
                button.clicked.connect(
                    partial(self.__button_clicked, r, c) #создает функцию, у которой меньше параметров
                )
                self.__grid.addWidget(button, r, c)
                buttons_row.append(button)
            self.__button.append(buttons_row)

    def __button_clicked(self, row, column):
        num_rows = len(self.__buttons) #получили колво строк
        num_buttons = len(self.__buttons[row])
        #жмем кнопку добавляется строчка

if __name__ == '__main__':
    app = QApplication(sys.argv) #просто создание приложения
    w = MainWindow() #создали окошко, но не появляется
    w.show() #показали окошко, но не факт что он будет меняться
    # события чтобы что-то менялось в нашем окошке, все скрладывается в стек, нужно его посмотреть
    app.exec_() #вернет управление когда придет сообщение закройся, вернет 0 если все норм
    sys.exit(app.exec_())# возвращает return app.exec_
    #chmod +x pyqt5_ex1.py пишем в командной строке, включение файла исполняемым, rwx
    # можно просто будет кликнуть на файл и все запустится
