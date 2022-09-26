import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel

from PyQt5 import QtCore, QtGui, QtWidgets
from ui3_pro import Ui_FaceSwap
from functools import partial

class Ui_SelectStyle(QDialog):
    def __init__(self):
        super().__init__()

        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(40, 60, 400, 400))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("FaceSwap/photo/style/1.bmp"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.label_1.mousePressEvent = partial(self.changeFaceDialog, 1)
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("FaceSwap/photo/style/2.bmp"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent = partial(self.changeFaceDialog, 2)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("FaceSwap/photo/style/3.bmp"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = partial(self.changeFaceDialog, 3)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("FaceSwap/photo/style/4.bmp"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent = partial(self.changeFaceDialog, 4)
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.setLayout(self.gridLayout)

    def changeFaceDialog(self, var, Id):
        print("Success!")
        dlg = Ui_FaceSwap(var)
        dlg.exec()