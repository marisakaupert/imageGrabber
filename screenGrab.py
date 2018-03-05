import os
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

imagesFolderPath = os.path.join(os.path.dirname(__file__), 'screenCaptures')
imagesConvertPath = os.path.join(os.path.dirname(__file__), 'iconConvert.py')

if not os.path.exists(imagesFolderPath):
    os.makedirs(imagesFolderPath)


def cropImage(count):
    """ runs a subprocess to crop the image to 400x400
    """

    import subprocess

    imageStart = os.path.join(imagesFolderPath, "{0}.png".format(count))
    imageResult = os.path.join(imagesFolderPath, "{0}.jpg".format(count))

    cmd = ['python', imagesConvertPath, '-ip', imageStart, '-irp', imageResult]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    res, err = p.communicate()


def getScreenGrab(count):
    import maya.OpenMaya
    import maya.OpenMayaUI

    view = maya.OpenMayaUI.M3dView.active3dView()

    image = maya.OpenMaya.MImage()

    view.readColorBuffer(image, True)

    imageFileName = os.path.join(
        imagesFolderPath, "{0}.png".format(count))

    image.writeToFile(imageFileName, 'png')


def saveImage(doScreenGrab=False, doCrop=True, count=0):
    if doScreenGrab:
        getScreenGrab(count)
        _logger.info("Created screen grab")

    if doCrop:
        cropImage(count)
