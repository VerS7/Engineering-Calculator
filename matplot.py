from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import style
from matplotlib import pyplot as plt
from numpy import *
from math import *
class MplCanvas(FigureCanvas):
    style.use('ggplot')

    def __init__(self):
        self.fig = plt.figure()
        super(MplCanvas, self).__init__(self.fig)

    def make_plot(self, func, interval):
        x = []
        y = []
        for i in linspace(interval[0], interval[1], 100):
            x.append(i)
            y.append(eval(func.replace('x', str(i))))
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x,y,'r')
        self.ax.set_title(func)
        self.draw()

