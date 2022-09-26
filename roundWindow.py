from PyQt5 import QtGui, QtWebKit, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import Qt, QSize

class RoundWindow(QWebView):
    def __init__(self):
        super(RoundWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def sizeHint(self):
        return QSize(300,300)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QtGui.QColor(255, 255, 255, 255))
        qp.drawEllipse(0, 0, 300, 300)
        qp.end()

# a = QtGui.QApplication([])
import sys
a = QtWidgets.QApplication(sys.argv)
# app = QtGui.QApplication(sys.argv)
rw = RoundWindow()
rw.show()
a.exec_()