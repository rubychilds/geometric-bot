# #!/usr/bin/env python3
import os
import sys
import math
import datetime

import cairocffi as cairo

from mod import draw
from mod.colz import *


# Pyglet window
# window = pyglet.window.Window( w, h )

# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ims = cairo.ImageSurface.create_from_png("./input/ori.png")
ctx = cairo.Context(ims)

w = 334
h = 334
cx = w / 2
cy = h / 2
scale = 150

ims_d = cairo.ImageSurface(cairo.FORMAT_ARGB32, w * 2, h * 2)
ctx_d = cairo.Context(ims_d)

ctx_d.rectangle (0, 0, w * 2, h * 2) # Rectangle(x0, y0, x1, y1)
ctx_d.set_source_rgb(0.1, 0.1, 0.1)
ctx_d.fill ()
ctx_d.set_line_cap(cairo.LINE_CAP_ROUND)

buf = ims.get_data()
pixel = 0.0
ctx_d.set_operator(cairo.OPERATOR_OVER)
for i in range(0,len(buf),4):

    x1 = i / 4 % w
    y1 = i / 4 / w

    # In some environments pixel data ir returned as by in others as int :(
    r = buf[i]
    if isinstance( r, bytes ):
        r = int.from_bytes( r, byteorder='big' )
        r /= 255

    g = buf[i+1]
    if isinstance( g, bytes ):
        g = int.from_bytes( g, byteorder='big' )
        g /= 255

    b = buf[i+2]
    if isinstance( b, bytes ):
        b = int.from_bytes( b, byteorder='big' )
        b /= 255

    hsl = Colz.rgbToHsl( b, g, r )
    sw = max(0.5, 5 * hsl[0]) # Stroke width
    len_ = max(10, scale * hsl[2]) # line length

    angle = math.pi / 2
    # angle = (hsl[1] * math.pi * 2)
    #angle = hsl[1] * 2 * math.pi

    # y2 = y1 + len_ * math.sin( angle )
    # x2 = x1 + len_ * math.cos( angle )
    y2 = y1 + len_
    x2 = x1

    # ctx_d.set_line_width( sw )
    # ctx_d.set_source_rgba( 0.0, 0.0, 0.0, 0.15 )
    # draw.line ( ctx_d, x1 * 2, y1 * 2, x2 * 2 - 1 , y2 * 2 - 1 )

    ctx_d.set_line_width( sw )
    ctx_d.set_source_rgba( b, g, r, hsl[2] )
    draw.line ( ctx_d, x1 * 2, y1 * 2, x2 * 2 , y2 * 2 )
    # draw.line ( ctx_d, x1 * 2, y1 * 2, x1 * 2 , (y1 - len_) * 2 )

    # print(str(r)+' '+str(g)+' '+str(b))

    # print(str(x1)+' '+str(y1))
    # print(str(i / 4 % w))
    # print(str(i / 4 / w))
    # sys.exit()

# ctx.set_source_rgb(1.0, 0.1, 0.1)
# draw.line ( ctx, 100, 100, 200, 200 )

# data = (ctypes.c_ubyte * (w * h * 4))()
# stride = w * 4
# ims = cairo.ImageSurface.create_for_data( data, cairo.FORMAT_ARGB32, w, h, stride)
# ctx = cairo.Context(ims)

# Clear
# ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
# ctx.set_source_rgb(0.1, 0.1, 0.1)
# ctx.fill ()

# ctx.set_source_rgba(1.0, 1.0, 1.0, 0.5)
# draw.circle( ctx, 200, 200, 160, 9)
# ctx.stroke ()

ims_d.write_to_png("plands.png")
