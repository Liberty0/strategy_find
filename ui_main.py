
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
        self.textEdit.textChanged.connect(self.varinput)

    def btn1click(self):
        self.pushButton_6.setText("clicked")
        
        date_price = scr.price_scraper('TW', self.textEdit.toPlainText())
        # analysis = ana.analysis(date_price)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(date_price[0],date_price[1])
        # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

    def varinput(self):
        self.label.setText(self.textEdit.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()