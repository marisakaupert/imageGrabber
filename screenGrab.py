import os
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

imagesFolderPath = os.path.join(os.path.dirname(__file__), 'screenCaptures')

if not os.path.exists(imagesFolderPath):
    os.makedirs(imagesFolderPath)


def cropImage(count=None):
    pass


def getScreenGrab(count=None):
    import maya.OpenMaya
    import maya.OpenMayaUI

    view = maya.OpenMayaUI.M3dView.active3dView()

    image = maya.OpenMaya.MImage()

    view.readColorBuffer(image, True)

    imageFileName = os.path.join(
        imagesFolderPath, "model_{0}.png".format(count))

    image.writeToFile(imageFileName, 'png')
