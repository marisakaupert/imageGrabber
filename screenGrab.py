import os
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

imagesFolderPath = os.path.join(os.path.dirname(__file__), 'screenCaptures')
imagesConvertPath = os.path.join(os.path.dirname(__file__), 'imagesConvert.py')

if not os.path.exists(imagesFolderPath):
    os.makedirs(imagesFolderPath)


def cropImage(count=None):
    import subprocess

    imageStart = os.path.join(imagesFolderPath, "model_{0}.png".format(count))
    imageResult = os.path.join(
        imagesFolderPath, "model_{0}.jpeg".format(count))

    cmd = ['python', imagesConvertPath,
           '-ip', imageStart,
           '-irp', imageResult]

    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    resolution, error = p.communicate()


def getScreenGrab(count=None):
    import maya.OpenMaya
    import maya.OpenMayaUI

    view = maya.OpenMayaUI.M3dView.active3dView()

    image = maya.OpenMaya.MImage()

    view.readColorBuffer(image, True)

    imageFileName = os.path.join(
        imagesFolderPath, "model_{0}.png".format(count))

    image.writeToFile(imageFileName, 'png')
