import os
import logging
from PySide import QtGui, QtCore, QtUiTools
from shiboken import wrapInstance
import pymel.core as pm
import maya.OpenMayaUI as omui 

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


import screenGrab
reload(screenGrab)


def getMayaWindow():
    pointer = omui.MQtUtil.mainWindow()
    if pointer:
        return wrapInstance(long(pointer), QtGui.QMainWindow)

window = None


def run():
    global window
    if window:
        window.close()
    window = ImageGrabberUI(parent=getMayaWindow())
    window.show()


class ImageGrabberUI(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ImageGrabberUI, self).__init__(parent)

        self.gridLayout = QtGui.QGridLayout()
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.screenGrabPushButton = QtGui.QPushButton("Take Screenshot")
        self.verticalLayout.addWidget(self.screenGrabPushButton)
        self.previousImagesLabel = QtGui.QLabel("Previous Screenshots:")
        self.verticalLayout.addWidget(self.previousImagesLabel)
        self.imagePathLabel = QtGui.QLabel("Path:")
        self.verticalLayout.addWidget(self.imagePathLabel)
        self.pathLineEdit = QtGui.QLineEdit()
        self.verticalLayout.addWidget(self.pathLineEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.count = 0

        self.setLayout(self.gridLayout)
        self.setWindowTitle("SCREEN GRAB DEMO TOOL")
        self.makeConnections()
        self.show()

    def makeConnections(self):
        self.screenGrabPushButton.clicked.connect(self.addImageToLayout)

    def addImageToLayout(self):
        screenGrab.getScreenGrab(self.count)
        self.updateCount()

    def updateCount(self):
        self.count += 1


