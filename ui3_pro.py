import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel

from PyQt5 import QtCore, QtGui, QtWidgets

import os
import cv2
import argparse

from face_detection import select_face, select_all_faces
from face_swap import face_swap

class Ui_FaceSwap(QDialog):
    
    def __init__(self, Id):
        super().__init__()
        
        # Dialog.setObjectName("Dialog")
        # Dialog.resize(500, 500)
        # self.label = QtWidgets.QLabel(Dialog)
        src_img = 'FaceSwap/photo/1.png'
        dst_img = 'FaceSwap/photo/style/real/' + str(Id) + '.jpg'
        out_img = 'FaceSwap/photo/out.jpg'

        result = self.faceSwap(src_img, dst_img, out_img)
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(50, 50, 400, 400))
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setGeometry(QtCore.QRect(50, 50, 400, 400))
        self.label_1.setText("")
        pixmap = QtGui.QPixmap(out_img)
        pixmap_resized = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)

        self.label_1.setPixmap(pixmap_resized)
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.setLayout(self.gridLayout)

    def faceSwap(self, src_img, dst_img, out_img):
        src_img = cv2.imread(src_img)
        dst_img = cv2.imread(dst_img)

        args = {
            'out' : out_img,
            'correct_color' : True,
            'warp_2d' : False,
            'no_debug_window': True
        }

        class dotdict(dict):
            """dot.notation access to dictionary attributes"""
            __getattr__ = dict.get
            __setattr__ = dict.__setitem__
            __delattr__ = dict.__delitem__

        args = dotdict(args)
        
        # Select src face
        src_points, src_shape, src_face = select_face(src_img)
        # Select dst face
        dst_faceBoxes = select_all_faces(dst_img)

        if dst_faceBoxes is None:
            print('Detect 0 Face !!!')
            exit(-1)

        output = dst_img
        for k, dst_face in dst_faceBoxes.items():
            output = face_swap(src_face, dst_face["face"], src_points,
                            dst_face["points"], dst_face["shape"],
                            output, args)

        dir_path = os.path.dirname(args.out)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        cv2.imwrite(args.out, output)

        ##For debug
        if not args.no_debug_window:
            cv2.imshow("From", dst_img)
            cv2.imshow("To", output)
            cv2.waitKey(0)
            
            cv2.destroyAllWindows()

        return output
