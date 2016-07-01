# #!/usr/bin/env python3
import os
import math
import ctypes

import cairocffi as cairo

from mod import draw
from mod import bitmap
from mod.colz import *

w = 600
h = 600
cx = w / 2
cy = h / 2

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ctx = cairo.Context(ims)

# Clear
ctx.set_operator(cairo.OPERATOR_OVER)
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

circles_num = 36 # 36
circles_radius = 540 / 4
col = Colz()
col.setHsl( 272, 49, 58 )
hue_rotation = int(360 / circles_num)

ctx.set_operator(cairo.OPERATOR_SCREEN)
ctx.set_source_rgba(1.0, 1.0, 1.0, 1.0)

for i in range( circles_num ):

    col.rotateHue( hue_rotation )
    ctx.set_source_rgba( *col.rgb, 0.20)

    ctx.save()
    ctx.translate( cx, cy )
    ctx.rotate( i / circles_num * 2 * math.pi )
    ctx.translate( 0, -circles_radius )
    draw.plot( ctx, 0, 0, circles_radius)
    ctx.restore()

# bitmap.contrast( ims, 30.0 )

level_op = {
    'gamma': 1.0,
    'input': {
        'min': 100,
        'max': 230
    },
    'output': {
        'min': 0,
        'max': 255
    }
}
bitmap.levels( ims, level_op )

ims.write_to_png("test.png")
