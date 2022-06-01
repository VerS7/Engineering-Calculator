import math
from PyQt5.Qt import *
from EngCalculatorUI import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplot import MplCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """Кнопки 0-9"""
        self.ui._1.clicked.connect(lambda: self.NumBtn(1))
        self.ui._2.clicked.connect(lambda: self.NumBtn(2))
        self.ui._3.clicked.connect(lambda: self.NumBtn(3))
        self.ui._4.clicked.connect(lambda: self.NumBtn(4))
        self.ui._5.clicked.connect(lambda: self.NumBtn(5))
        self.ui._6.clicked.connect(lambda: self.NumBtn(6))
        self.ui._7.clicked.connect(lambda: self.NumBtn(7))
        self.ui._8.clicked.connect(lambda: self.NumBtn(8))
        self.ui._9.clicked.connect(lambda: self.NumBtn(9))
        self.ui._0.clicked.connect(lambda: self.NumBtn(0))
        """Специальные кнопки"""
        self.ui.Pi.clicked.connect(lambda: self.NumBtn(f"{math.pi:.{5}f}"))
        self.ui.Exp.clicked.connect(lambda: self.NumBtn(f"{math.e:.{5}f}"))
        """Операторы"""
        self.ui.factorial.clicked.connect(lambda: self.Factorial())
        self.ui.plus.clicked.connect(lambda: self.Plus())
        self.ui.minus.clicked.connect(lambda: self.Minus())
        self.ui.divide.clicked.connect(lambda: self.Divide())
        self.ui.mult.clicked.connect(lambda: self.Mult())
        self.ui.Persentage.clicked.connect(lambda: self.Percent())
        self.ui.log.clicked.connect(lambda: self.Log2())
        self.ui.log2.clicked.connect(lambda: self.Log4())
        self.ui.log8.clicked.connect(lambda: self.Log8())
        self.ui.lg10.clicked.connect(lambda: self.Log10())
        self.ui.root.clicked.connect(lambda: self.Sqrt())
        self.ui.degree2.clicked.connect(lambda: self.Degree2())
        """Конечные операторы"""
        self.ui.Clear.clicked.connect(lambda: self.Clear())
        self.ui.ClearForOne.clicked.connect(lambda: self.ClearOne())
        self.ui.Calculate.clicked.connect(lambda: self.Equal())
        """График функции"""
        self.ui.graph_build.clicked.connect(lambda: self.plot_build())
        self.canv = MplCanvas()
        self.toolbar = NavigationToolbar(self.canv, self)
        self.layout = QVBoxLayout(self.ui.graph)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.canv)
        self.layout.addWidget(self.toolbar)
        self.toolbar.hide()

    Cal = ''
    PrevCal = ''

    def plot_build(self):
        try:
            y = self.ui.lineEdit.text()
            x = eval(self.ui.lineEdit_2.text())
            self.canv.make_plot(y,x)
            self.toolbar.show()
        except Exception as e:
            print(e)

    def ClearOne(self):
        try:
            self.Cal = str(self.Cal)[:len(str(self.Cal))-1]
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Degree2(self):
        try:
            self.Cal = self.Cal**2
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def NumBtn(self, num):
        try:
            num = str(num)
            self.ui.Cals.setText(self.ui.Cals.text()+num)
            self.Cal = float(self.ui.Cals.text())
            print(self.Cal)
        except Exception as e:
            print(e)

    def Factorial(self):
        try:
            self.Cal = math.factorial(int(self.Cal))
            self.ui.Cals.clear()
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Clear(self):
        try:
            self.ui.Cals.clear()
            self.ui.PrevCals.clear()
            self.Cal = ''
            self.PrevCal = ''
        except Exception as e:
            print(e)

    def Equal(self):
        try:
            self.PrevCal, self.Cal = self.Cal, self.PrevCal
            self.ui.Cals.setText(str(self.Cal))
            self.ui.PrevCals.setText(str(self.PrevCal))
        except Exception as e:
            print(e)

    def Plus(self):
        try:
            self.PrevCal = float(self.Cal) + float(self.PrevCal)
            print(float(self.Cal))
            self.ui.PrevCals.setText(str(self.PrevCal))
            self.ui.Cals.clear()
            self.Cal = ''
        except Exception as e:
            print(e)
            print(type(self.Cal))

    def Minus(self):
        try:
            if int(self.PrevCal) == 1000 and int(self.Cal == 7):
                self.Cal = 'ГУЛЬ?'
                self.ui.Cals.setText(str(self.Cal))
                self.ui.PrevCals.clear()
            else:
                self.PrevCal = float(self.PrevCal) - float(self.Cal)
                print(float(self.Cal))
                self.ui.PrevCals.setText(str(self.PrevCal))
                self.ui.Cals.clear()
                self.Cal = ''
        except Exception as e:
            print(e)

    def Divide(self):
        try:
            self.PrevCal = float(self.PrevCal) / float(self.Cal)
            print(float(self.Cal))
            self.ui.PrevCals.setText(str(self.PrevCal))
            self.ui.Cals.clear()
            self.Cal = ''
        except Exception as e:
            print(e)

    def Mult(self):
        try:
            self.PrevCal = float(self.PrevCal) * float(self.Cal)
            print(float(self.Cal))
            self.ui.PrevCals.setText(str(self.PrevCal))
            self.ui.Cals.clear()
            self.Cal = ''
        except Exception as e:
            print(e)

    def Percent(self):
        try:
            self.Cal = float(self.Cal) * 0.1
            print(float(self.Cal))
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Log2(self):
        try:
            self.Cal = f"{math.log2(int(self.Cal)):.{5}f}"
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Log4(self):
        try:
            self.Cal = f"{math.log(int(self.Cal), 4):.{5}f}"
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Log8(self):
        try:
            self.Cal = f"{math.log(int(self.Cal), 8):.{5}f}"
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Log10(self):
        try:
            self.Cal = f"{math.log10(int(self.Cal)):.{5}f}"
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)

    def Sqrt(self):
        try:
            self.Cal = f"{math.sqrt(float(self.Cal)):.{5}f}"
            print(float(self.Cal))
            self.ui.Cals.setText(str(self.Cal))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()