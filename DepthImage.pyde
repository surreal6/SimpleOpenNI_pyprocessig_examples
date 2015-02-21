"""
/* --------------------------------------------------------------------------
 * SimpleOpenNI DepthImage Test
 * --------------------------------------------------------------------------
 * Processing Wrapper for the OpenNI/Kinect 2 library
 * http://code.google.com/p/simple-openni
 * --------------------------------------------------------------------------
 * prog:  Max Rheiner / Interaction Design / Zhdk / http:#iad.zhdk.ch/
 * date:  12/12/2012 (m/d/y)
 *
 * translated to pyprocessing: Carlos Padial
 * ----------------------------------------------------------------------------
 */
 """

from SimpleOpenNI import SimpleOpenNI

import sys

context = SimpleOpenNI(this)

def setup():
    size(640*2, 480)

    if context.isInit() == False:
        print("Can't init SimpleOpenNI, maybe the camera is not connected!") 
        exit()
        return

    # mirror is by default enabled
    context.setMirror(True)

    # enable depthMap generation 
    context.enableDepth()

    # enable ir generation
    context.enableRGB()

def draw():
    # update the cam
    context.update()

    background(200, 0, 0)

    # draw depthImageMap
    image(context.depthImage(), 0, 0)

    # draw irImageMap
    image(context.rgbImage(), context.depthWidth() + 10, 0)
