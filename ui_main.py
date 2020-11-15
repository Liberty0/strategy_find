
import sys
from PyQt5 import QtWidgets, uic
# from PyQt5 import QtGui, QtCore
import os
# import matplotlib
import numpy as np
import price_scraper as scr
import price_analysis as ana

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        path = os.getcwd()
        qtCreatorFile = path + os.sep + "ui" + os.sep + "mainwindow.ui"  # ui檔案路徑
        uic.loadUi(qtCreatorFile,self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")
        
        # connect callbacks
        self.pushButton.clicked.connect(self.btn1click)
        # self.pushButton_5.clicked.connect(self.btn5click_plot)
        # self.symbolEdit.textChanged.connect(self.varinput)
        self.weight_RSI.valueChanged.connect(self.weight_changed)
        self.weight_MACD.valueChanged.connect(self.weight_changed)
        self.weight_ADX.valueChanged.connect(self.weight_changed)
        self.weight_MA5.valueChanged.connect(self.weight_changed)
        self.weight_MA10.valueChanged.connect(self.weight_changed)
        self.weight_MA20.valueChanged.connect(self.weight_changed)
        self.weight_KD.valueChanged.connect(self.weight_changed)

    def btn1click(self):
        # self.pushButton_6.setText("clicked")
        
        symbol = self.symbolEdit.toPlainText()
        Timetick = self.TimeTick.currentText()

        date_price = scr.price_scraper('TW', symbol, Timetick)
        analysis = ana.analysis(date_price)


        ## plotter
        Dates = date_price[0]
        Closes = date_price[1]
        RSI = analysis[1]

        self.MplWidget.canvas.axes.clear()
        
        if Timetick=='d' or Timetick=='w' or Timetick=='m':
            self.MplWidget.canvas.axes.plot(Dates,Closes,'-')
            self.MplWidget.canvas.axes.plot(Dates[(len(Dates)-1-len(RSI)):(len(Dates)-1)],RSI,'-')
            # self.MplWidget.canvas.axes.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
        elif Timetick=='5m' or Timetick=='10m' or Timetick=='30m':
            x_axis = np.linspace(0,len(Closes),len(Closes)+1)
            self.MplWidget.canvas.axes.plot(Closes,'-')
            self.MplWidget.canvas.axes.plot(x_axis[(len(x_axis)-1-len(RSI)):(len(x_axis)-1)],RSI,'-')
        
        
        # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

    def weight_changed(self):
        
        TotalWeight = \
            float(self.weight_RSI.value())\
            + float(self.weight_MACD.value())\
            + float(self.weight_ADX.value())\
            + float(self.weight_MA5.value())\
            + float(self.weight_MA5.value())\
            + float(self.weight_MA20.value())\
            + float(self.weight_KD.value())
        
        self.weight_total.setText(str(TotalWeight))
        
        self.label.setText(self.symbolEdit.toPlainText())
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()