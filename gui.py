import os
import logging
from PySide2 import QtWidgets, QtGui
from shiboken2 import wrapInstance
import pymel.core as pm
import maya.OpenMayaUI as omui

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


import screenGrab
reload(screenGrab)


def getMayaWindow():
    pointer = omui.MQtUtil.mainWindow()
    if pointer:
        return wrapInstance(long(pointer), QtWidgets.QMainWindow)

window = None


def run():
    global window
    if window:
        window.close()
    window = ImageGrabberUI(parent=getMayaWindow())
    window.show()


class ImageGrabberUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ImageGrabberUI, self).__init__(parent)
        
        self.count = 0
        
        self.setCentralWidget(QtWidgets.QWidget(self)) 
        self.gridLayout = QtWidgets.QGridLayout()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.screenGrabPushButton = QtWidgets.QPushButton("Take Screenshot")
        self.verticalLayout.addWidget(self.screenGrabPushButton)
        self.imagePathLabel = QtWidgets.QLabel("Path:")
        self.verticalLayout.addWidget(self.imagePathLabel)
        self.pathLineEdit = QtWidgets.QLineEdit()
        self.pathLineEdit.setText("Path here")
        self.verticalLayout.addWidget(self.pathLineEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.makeConnections()
        self.centralWidget().setLayout(self.gridLayout)
        self.setWindowTitle("SCREEN GRAB DEMO TOOL")
        self.show()
        

    def makeConnections(self):
        self.screenGrabPushButton.clicked.connect(self.takeScreenshot)

    def takeScreenshot(self):
        self.imagesFolderPath = screenGrab.getScreenGrab(self.count)
        self.pathLineEdit.setText(self.imagesFolderPath)
        self.updateCount()

    def updateCount(self):
        self.count += 1
