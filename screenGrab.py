import os
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

imagesFolderPath = os.path.join(os.path.dirname(__file__), 'screenCaptures')

if not os.path.exists(imagesFolderPath):
    os.makedirs(imagesFolderPath)


def getScreenGrab():
    import maya.OpenMaya
    import maya.OpenMayaUI

    view = maya.OpenMayaUI.M3dView.active3dView()

    image = maya.OpenMaya.MImage()

    view.readColorBuffer(image, True)

    imageFileName = os.path.join(imagesFolderPath, "{0}.png".format("test"))

    image.writeToFile(imageFileName, 'png')
