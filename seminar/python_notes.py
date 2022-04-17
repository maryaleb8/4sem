                                                            12/3
#передача аргументов в функцию

def f(a, b):
    print('A=', a)
    print('B=', b)
    #можно вводить и числа и слова, даже можно переносить строку:
    a = """1234
    fvvvvv""" #но это будет восприниматься как документация функции
#Документация
def f(a, b):
    'prints its parametrs' #будет выводиться эта документация если спросить f? или f.__doc__
    print('A=', a)
    print('B=', b)

#можно объявить параметр по умолчанию, тогда можно и от нуля параметров вызвать
def f(a, b=2500)... f(2)

#функции с переменным числом аргументов, например print

#Реализуем свой print
def my_print(*args, **kwargs): #много аргументов там, перед чем стоит звездочка
#**kwargs если нужно чтобы передавалось с именем, словарь, ключ - названия, значение - то что записали
# * еще означает проитерироваться по объекту
    for x in args:
        print(x)

def my_print(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
x = {'a': 42, 'b': 7500}
#my_print(c=1, **x) будет 42 7500 две звезды это распаковка словаря, одна звезда распаковка списка


a = (1, 2, 3, 4)
x, *y = a
will be y = [2, 3, 4]

a = 1, 2, 3
b = 3, 4, 5
q, w, e, r, t, y = *a, *b #тогда каждый получит цифру, так как распаковка идет, если без нее написать
#то будет a, b выводится ((1, 2, 3), (1, 2, 3))

for x in c:
    f()
else: #будет выполнен только когда все элементы будут обработаны
    g() # общий вид цикла for, превращается в

@ = iter(c)
& = True
while &:
    try:
        x = @.next #есть метод который берет следующий
    except StopIteration:
        & = False
        break
    f()

можно даже писать for _ in range(5): #range может идти и обратно и с шагом list(range(-1, -10, -3)) получится [-1, -4, -7]
                        print('Hello')





                                                                19/03
-----------ФОРМАТИРОВАНИЕ
x = 42
f'X = {x:05d}' #форматная строка, добивает до 5 знаков

import datetime as dt
t = dt.datetime.uncnow()
f'T = {t:%d.%m.%Y}' получается T = 19.03.2022
но для этого использовалось не такое удобное форматирование
'X = {0:05d} (0x{0:X}), T = {1:%d.%m.%Y}'.format(x, t)  на место 0 подставляется везде x,
на метто 1 подставляется t, format уже не знает кто x, кто t
'X = {a:05d} (0x{a:X}), T = {b:%d.%m.%Y}'.format(a = x, b = t) эти два работают на раньших версиях

s = 'X = %05d (0x%X)' 16 ричный вывод через %X
t = (42, 42)
y = s % t получается y = 'X = 42 (0x2A)'

-----------РАБОТА С СТРОКАМИ
s = 'abcdef' будет работать s[3] = 'd', s[-1] = 'e', s[3:6] = 'def' то есть можно азять массив
можно даже выходить за границы или писать s[3:], с конца s[-2:0], четные s[::2], нечетные s[1::2]
можно писать все что есть в range, по сути это так и работает
x = '123'
x.isdigit() дает равен true
str.isdigit(x) то же самое

s = '1,2,3'
s.split(',') разделит строку на динамический массив ['1', '2', '3']
s.split(',', 1) разделит только один раз ['1', '2,3']

---
SQLite3 самый продвинутый движок баз данных, встраиваемая субд
import sqlite3 в питоне DB-API2 сертифицирует как должны выглядеть субд, потом чтобы на postgree например
есть объект, описывающий соединение с базой, лучше делать одно соединение с базой, так как это тяжело
но при этом нужно обслуживать много клиентов, для этого используют пул соединений
метод connect с параметрами, возвращает собъект соединения
DB-API2 -->(connect) connection
                                |
                                V (cursor)
                        созданные курсоры (легковесные соединения)
                    у них есть метод execute чтобы отправить запро с базе
                fetchone() достает по одной строке, fatchall() достает список кортежей

conn = sqlite3.connect('/tmp/test.s3db') может создать файл если его нет, любой пользователь в системе
может читать, нет пользователей и ролей
cur = conn.cursor() выдает курсоры
cur.execute('SELECT current_timestamp') подключились к бд и достали время
cur.execute("""CREATE TABLE t1 (
    a INTEGER,
    b TEXT
)""") создали таблицу
Типы данных в sqlite: NULL, INTEGER, REAL (число с плав точкой двойной точности), TEXT, BLOB (массив байтов)
С помощью sqlitebrowser можно настроить все что можно

import sqlite3
conn = sqlite3.connect('/tmp/test.s3db')
cur = conn.cursor()
cur.execute('INSERT INTO t1(a, b) VALUES (?, ?)', (41, 'Hello'))
или executemany чтобы сделать много вставок и много кортежей
но другой пользователь пока не зхакоммитим не увидит этих изменений conn.commit(), только тогда данные попадают




                                                            26/03
------ОКОННЫЕ ПРИЛОЖЕНИЯ






#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton)

def f():
    print('Hello')

class MainWindow(QWidget):
    def __init__(self): #создаем свой конструктор, __init__ то всегда конструктор
        super().__init__() # super берет от родительского класса конструктор
        #накидываем элементы в окошке: нужно нормально их расположить
        grid = QGridLayout() #менеджер раскладки, делает автоматически адекватно, созлает сетку
        self.setLayout(grid)
        button1 = QPushButton('Click me', self)# 2-какой оконный элемент является его родителем
        button1.clicked.connect(f) #что будет при одинарном нажатии
        grid.addWidget(button1, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv) #просто создание приложения
    w = MainWindow() #создали окошко, но не появляется
    w.show() #показали окошко, но не факт что он будет меняться
    # события чтобы что-то менялось в нашем окошке, все скрладывается в стек, нужно его посмотреть
    app.exec_() #вернет управление когда придет сообщение закройся, вернет 0 если все норм
    sys.exit(app.exec_())# возвращает return app.exec_
    #chmod +x pyqt5_ex1.py пишем в командной строке, включение файла исполняемым, rwx
    # можно просто будет кликнуть на файл и все запустится





#!/usr/bin/env python3
from functools import partial #частичное выполнение для функций
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton)

N, M = 2, 3

class MainWindow(QWidget):
    def __init__(self): #создаем свой конструктор, __init__ то всегда конструктор
        super().__init__() # super берет от родительского класса конструктор
        #накидываем элементы в окошке: нужно нормально их расположить
        grid = QGridLayout() #менеджер раскладки, делает автоматически адекватно, созлает сетку
        self.setLayout(grid)
        for r in range(N):
            for c in range(M):
                button = QPushButton(f'{r} {c}', self)# 2-какой оконный элемент является его родителем
                button.clicked.connect(
                    partial(self.__button_clicked, r, c) #создает функцию, у которой меньше параметров
                )
                grid.addWidget(button, r, c)

    def __button_clicked(self, row, column):
        print(f'r = {row}, c = {column}')

if __name__ == '__main__':
    app = QApplication(sys.argv) #просто создание приложения
    w = MainWindow() #создали окошко, но не появляется
    w.show() #показали окошко, но не факт что он будет меняться
    # события чтобы что-то менялось в нашем окошке, все скрладывается в стек, нужно его посмотреть
    app.exec_() #вернет управление когда придет сообщение закройся, вернет 0 если все норм
    sys.exit(app.exec_())# возвращает return app.exec_
    #chmod +x pyqt5_ex1.py пишем в командной строке, включение файла исполняемым, rwx
    # можно просто будет кликнуть на файл и все запустится


                                                            02/04
------СОЕДИНЕНИЕ БД И ПАПКИ С КНОПКАМИ

открыли qtcreator добавили list widget когда зашли на main.ui выбрали самые обычные настройки
Смотри app.py