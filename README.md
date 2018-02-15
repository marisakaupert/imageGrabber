Tool to grab images in Maya. 

These are what I got from the meeting:
    1. Take an image in Maya without having to do a manual screenshot
    2. Have it be set to a certain resoluton so the image is never skewed
    3. Have the image be saved to a path
    4. The image needs 'tags' so it know where to store the image and upload it on Shotgun

```import sys 
sys.path.append( 'C:\Users\Marisa\Documents/imageGrabber' )

import gui
reload(gui)
gui.run()```

http://download.autodesk.com/us/maya/2009help/API/group___open_maya_u_i.html