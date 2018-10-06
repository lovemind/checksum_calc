# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\skan\Documents\GitHub\checksum_calc\checksum_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 348)
        Dialog.setSizeGripEnabled(False)
        self.btBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btBox.setGeometry(QtCore.QRect(150, 280, 231, 32))
        self.btBox.setOrientation(QtCore.Qt.Horizontal)
        self.btBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btBox.setObjectName("btBox")
        self.rbt1 = QtWidgets.QRadioButton(Dialog)
        self.rbt1.setGeometry(QtCore.QRect(30, 50, 81, 22))
        self.rbt1.setObjectName("rbt1")
        self.rbt2 = QtWidgets.QRadioButton(Dialog)
        self.rbt2.setGeometry(QtCore.QRect(110, 50, 81, 22))
        self.rbt2.setObjectName("rbt2")
        self.rbt3 = QtWidgets.QRadioButton(Dialog)
        self.rbt3.setGeometry(QtCore.QRect(190, 50, 101, 22))
        self.rbt3.setObjectName("rbt3")
        self.rbt4 = QtWidgets.QRadioButton(Dialog)
        self.rbt4.setGeometry(QtCore.QRect(290, 50, 101, 22))
        self.rbt4.setObjectName("rbt4")
        self.rbt5 = QtWidgets.QRadioButton(Dialog)
        self.rbt5.setGeometry(QtCore.QRect(400, 50, 101, 22))
        self.rbt5.setObjectName("rbt5")
        self.lbl_filePath = QtWidgets.QLabel(Dialog)
        self.lbl_filePath.setGeometry(QtCore.QRect(20, 100, 111, 18))
        self.lbl_filePath.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_filePath.setObjectName("lbl_filePath")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 210, 61, 34))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(450, 130, 61, 31))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 431, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 210, 431, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lbl_filePath_2 = QtWidgets.QLabel(Dialog)
        self.lbl_filePath_2.setGeometry(QtCore.QRect(20, 190, 121, 18))
        self.lbl_filePath_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_filePath_2.setObjectName("lbl_filePath_2")
        self.lbl_filePath_3 = QtWidgets.QLabel(Dialog)
        self.lbl_filePath_3.setGeometry(QtCore.QRect(10, 20, 181, 18))
        self.lbl_filePath_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_filePath_3.setObjectName("lbl_filePath_3")

        self.retranslateUi(Dialog)
        self.btBox.accepted.connect(Dialog.accept)
        self.btBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.rbt1, self.rbt2)
        Dialog.setTabOrder(self.rbt2, self.rbt3)
        Dialog.setTabOrder(self.rbt3, self.rbt4)
        Dialog.setTabOrder(self.rbt4, self.rbt5)
        Dialog.setTabOrder(self.rbt5, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.toolButton)
        Dialog.setTabOrder(self.toolButton, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rbt1.setText(_translate("Dialog", "MD5"))
        self.rbt2.setText(_translate("Dialog", "SHA1"))
        self.rbt3.setText(_translate("Dialog", "SHA256"))
        self.rbt4.setText(_translate("Dialog", "SHA384"))
        self.rbt5.setText(_translate("Dialog", "SHA512"))
        self.lbl_filePath.setText(_translate("Dialog", "파일위치"))
        self.pushButton.setText(_translate("Dialog", "비교"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.lbl_filePath_2.setText(_translate("Dialog", "Checksum 값"))
        self.lbl_filePath_3.setText(_translate("Dialog", "체크섬 알고리즘"))

