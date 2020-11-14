
import sys
from PyQt5 import QtWidgets, uic
# from PyQt5 import QtGui, QtCore
import os
import price_scraper as scr
# import price_analysis as ana

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
        date_price = scr.price_scraper('TW', symbol)
        # analysis = ana.analysis(date_price)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(date_price[0],date_price[1])
        # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

    def weight_changed(self):
        
        # self.properties.RSIWeight = float(self.weight_RSI.value())
        # self.properties.MACDWeight = float(self.weight_MACD.value())
        # self.properties.ADXWeight = float(self.weight_ADX.value())
        # self.properties.MA5Weight = float(self.weight_MA5.value())
        # self.properties.MA10Weight = float(self.weight_MA10.value())
        # self.properties.MA20Weight = float(self.weight_MA20.value())
        # self.properties.KDWeight = float(self.weight_KD.value())
        
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