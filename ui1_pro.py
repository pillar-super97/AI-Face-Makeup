# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui2_pro import Ui_SelectStyle
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

Stylesheet = """
{
    background: #002025;
    border-radius: 20px;
    opacity: 100;
    border: 2px solid #ff2025;                   
}
"""
class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        # Dialog.setWindowOpacity(0.5)
        # Dialog.setStyleSheet("border: 3px solid blue; border-radius: 200px;")

        side = min(self.width(), self.height())
        maskedRegion = QtGui.QRegion(self.width()/2 - side/2, self.height()/2 - side/2, side, side, QtGui.QRegion.Ellipse)
        self.setMask(maskedRegion)

        self.label = QtWidgets.QLabel(Dialog)
        # self.label.setWindowOpacity(0)
        # Dialog.setStyleSheet("background:transparent;")
        self.label.setGeometry(QtCore.QRect(50, 50, 400, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("FaceSwap/photo/avatar.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ButtonTakePicture = QtWidgets.QPushButton(Dialog)
        self.ButtonTakePicture.setGeometry(QtCore.QRect(200, 420, 101, 31))
        self.ButtonTakePicture.setObjectName("ButtonTakePicture")
        self.ButtonConfirm = QtWidgets.QPushButton(Dialog)
        self.ButtonConfirm.setGeometry(QtCore.QRect(200, 420, 101, 31))
        self.ButtonConfirm.setObjectName("ButtonConfirm")
        self.ButtonConfirm.clicked.connect(self.openSelectStyleDialog)
        self.ButtonConfirm.hide()
        self.ButtonTakeAgain = QtWidgets.QPushButton(Dialog)
        self.ButtonTakeAgain.setEnabled(True)
        self.ButtonTakeAgain.setGeometry(QtCore.QRect(200, 380, 101, 31))
        self.ButtonTakeAgain.setObjectName("ButtonTakeAgain")
        self.ButtonTakeAgain.hide()

        self.retranslateUi(Dialog)
        self.ButtonTakePicture.clicked.connect(self.getPicture) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ButtonTakePicture.setText(_translate("Dialog", "Take a picuture"))
        self.ButtonConfirm.setText(_translate("Dialog", "Confirm"))
        self.ButtonTakeAgain.setText(_translate("Dialog", "Take Again"))

    def getPicture(self):
        self.label.clear()
        self.label.setPixmap(QtGui.QPixmap("FaceSwap/photo/1.png"))
        self.ButtonTakeAgain.show()
        self.ButtonConfirm.show()
        self.ButtonTakePicture.hide()

    def openSelectStyleDialog(self):
        
        dlg = Ui_SelectStyle()
        dlg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec()
    # sys.exit(app.exec_())
