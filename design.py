# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Marisa\Documents\imageGrabber\design.ui'
#
# Created: Wed Feb 14 07:14:50 2018
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.screenGrabPushButton = QtGui.QPushButton(Dialog)
        self.screenGrabPushButton.setObjectName("screenGrabPushButton")
        self.verticalLayout.addWidget(self.screenGrabPushButton)
        self.previousImagesLabel = QtGui.QLabel(Dialog)
        self.previousImagesLabel.setObjectName("previousImagesLabel")
        self.verticalLayout.addWidget(self.previousImagesLabel)
        self.imagePathLabel = QtGui.QLabel(Dialog)
        self.imagePathLabel.setObjectName("imagePathLabel")
        self.verticalLayout.addWidget(self.imagePathLabel)
        self.pathLineEdit = QtGui.QLineEdit(Dialog)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.verticalLayout.addWidget(self.pathLineEdit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.screenGrabPushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.previousImagesLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.imagePathLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

