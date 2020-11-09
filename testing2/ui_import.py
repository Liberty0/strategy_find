# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from PyQt5 import QtWidgets, uic
# from PyQt5 import QtGui, QtCore
import os
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg
# from matplotlib.backends.backend_qt5agg import FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        path = os.getcwd()
        qtCreatorFile = path + os.sep + "ui" + os.sep + "mainwindow.ui"  # ui檔案路徑
        uic.loadUi(qtCreatorFile,self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")
        
        # connect callbacks
        self.pushButton.clicked.connect(self.btn1click)
        self.pushButton_5.clicked.connect(self.btn5click)
        self.textEdit.textChanged.connect(self.varinput)

    def btn1click(self):
        self.pushButton_6.setText("clicked")
        
    def btn5click(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [1, 2, 3, 4, 5, 6, 9, 8, 7, 0, 10]
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(x,y)
        # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()
        
    def varinput(self):
        self.label.setText(self.textEdit.toPlainText())

# path = os.getcwd()
# qtCreatorFile = path + os.sep + "ui" + os.sep + "mainwindow.ui"  # ui檔案路徑

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()