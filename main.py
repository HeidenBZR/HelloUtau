import sys
import os
from PySide import QtCore, QtGui
from ui import *

class HelloUtauUI(Ui_MainWindow):

    def setupUi(self, Dialog):
        super().setupUi(Dialog) # super class setupUi
        self.okButton.clicked.connect(close)

    def addUstLine(self, line):
        line = line.replace("\n","") # kick new line symbol because listWidget has build one
        self.listWidget.addItem(line) # I had put the view as a ListWidget, so.

def close():
    sys.exit()


def getUst(path, window):
    f = open(path, "r") # open UST which is just a textlike file
    for line in f:
        window.addUstLine(line) # simply adding any line
    f.close() # close UST

def __main__():

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = HelloUtauUI()
    ui.setupUi(MainWindow)
    MainWindow.show()

    if len(sys.argv) > 1:
        getUst(sys.argv[1], ui)

    sys.exit(app.exec_())

__main__()
