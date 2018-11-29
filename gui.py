from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QPushButton, QMessageBox
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5 import QtGui


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self, data):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        result = self.get_data(data)
        print(result)

        self.setMinimumSize(QSize(500, 400))  # Устанавливаем размеры
        self.setWindowTitle("Метрики Чепина и Спен")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет

        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(4)  # Устанавливаем три колонки
        table.setRowCount(2)  # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["  C  ", "  M  ", "  P  ", "  T  "])
        table.setVerticalHeaderLabels(['Перемнные в группе', 'Количество перменных в группе'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)


        # заполняем первую строку

        table.setItem(0, 0, QTableWidgetItem(result[0][0]))
        table.setItem(0, 1, QTableWidgetItem(result[0][1]))
        table.setItem(0, 2, QTableWidgetItem(result[0][2]))
        table.setItem(0, 3, QTableWidgetItem(result[0][3]))

        table.setItem(1, 0, QTableWidgetItem(str(result[0][4])))
        table.setItem(1, 1, QTableWidgetItem(str(result[0][5])))
        table.setItem(1, 2, QTableWidgetItem(str(result[0][6])))
        table.setItem(1, 3, QTableWidgetItem(str(result[0][7])))



        # расширенный

        table1 = QTableWidget(self)  # Создаём таблицу
        table1.setColumnCount(4)  # Устанавливаем три колонки
        table1.setRowCount(2)

        # Устанавливаем заголовки таблицы
        table1.setHorizontalHeaderLabels(["  C  ", "  M  ", "  P  ", "  T  "])
        table1.setVerticalHeaderLabels(['Перемнные в группе','Количество перменных в группе'])

        # Устанавливаем выравнивание на заголовки
        table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        table1.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table1.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        table1.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)

        # заполняем первую строку

        table1.setItem(0, 0, QTableWidgetItem(result[1][0]))
        table1.setItem(0, 1, QTableWidgetItem(result[1][1]))
        table1.setItem(0, 2, QTableWidgetItem(result[1][2]))
        table1.setItem(0, 3, QTableWidgetItem(result[1][3]))

        table1.setItem(1, 0, QTableWidgetItem(str(result[1][4])))
        table1.setItem(1, 1, QTableWidgetItem(str(result[1][5])))
        table1.setItem(1, 2, QTableWidgetItem(str(result[1][6])))
        table1.setItem(1, 3, QTableWidgetItem(str(result[1][7])))

        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
        table1.resizeColumnsToContents()


        # Спен
        rowcount = len(result[2])
        table2 = QTableWidget(self)  # Создаём таблицу
        table2.setColumnCount(2)  # Устанавливаем три колонки
        table2.setRowCount(rowcount)
        table2.setHorizontalHeaderLabels(["  Переменная  ", "  Спен  "])

        i = 0
        for x,y in list(result[2].items()):

            table2.setItem(i, 0, QTableWidgetItem(x))
            table2.setItem(i, 1, QTableWidgetItem(str(y)))
            i += 1

        grid_layout.addWidget(table,  0, 0)  # Добавляем таблицу в сетку
        grid_layout.addWidget(table1, 1, 0)
        grid_layout.addWidget(table2, 2, 0)

    def get_data(self, list_of_dict):
        chepin = list_of_dict[0]
        chepin_ext = list_of_dict[1]
        spen = list_of_dict[2]

        chepin_list_manager = []
        chepin_list_assigment = []
        chepin_list_input = []
        chepin_list_trash = []

        for i in range(len(chepin[0])):
            chepin_list_manager.append(chepin[0].pop())
        print(chepin_list_manager)

        for i in range(len(chepin[1])):
            chepin_list_assigment.append(chepin[1].pop())
        print(chepin_list_assigment)

        for i in range(len(chepin[2])):
            chepin_list_input.append(chepin[2].pop())
        print(chepin_list_input)

        for i in range(len(chepin[3])):
            chepin_list_trash.append(chepin[3].pop())
        print(chepin_list_trash)

        chepinext_list_manager = []
        chepinext_list_assigment = []
        chepinext_list_input = []
        chepinext_list_trash = []

        for i in range(len(chepin_ext[0])):
            chepinext_list_manager.append(chepin_ext[0].pop())

        for i in range(len(chepin_ext[1])):
            chepinext_list_assigment.append(chepin_ext[1].pop())

        for i in range(len(chepin_ext[2])):
            chepinext_list_input.append(chepin_ext[2].pop())

        for i in range(len(chepin_ext[3])):
            chepinext_list_trash.append(chepin_ext[3].pop())


        P, M, C, T = '','','',''
        for el in chepin_list_manager:
            P += el+','
        for el in chepin_list_assigment:
            M += el+','
        for el in chepin_list_input:
            C += el+','
        for el in chepin_list_trash:
            T += el+','
        print(P,M,C,T)
        P = P[:-1]
        M = M[:-1]
        C = C[:-1]
        T = T[:-1]

        Pe, Me, Ce, Te = '', '', '', ''
        for el in chepinext_list_manager:
            Pe += el + ','
        for el in chepinext_list_assigment:
            Me += el + ','
        for el in chepinext_list_input:
            Ce += el + ','
        for el in chepinext_list_trash:
            Te += el + ','
        print(Pe, Me, Ce, Te)
        Pe = Pe[:-1]
        Me = Me[:-1]
        Ce = Ce[:-1]
        Te = Te[:-1]
        return [P,M,C,T,len(chepin_list_manager),len(chepin_list_assigment),len(chepin_list_input),len(chepin_list_trash)]\
            , [Pe,Me,Ce,Te,len(chepinext_list_manager),len(chepinext_list_assigment),len(chepinext_list_input),len(chepinext_list_trash)]\
            , spen


if __name__ == "__main__":
    import sys
    from main import main

    app = QApplication(sys.argv)

    mw = MainWindow(main('kek.txt'))
    mw.show()
    sys.exit(app.exec())
