# #!/usr/bin/env python3
import time
import math
import cairo
#import cairocffi as cairo #MacOS

from mod import draw

w = 600
h = 600
cx = w / 2
cy = h / 2

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

# ctx.set_source_rgba(192, 0, 0, 0.5)
# circle( ctx, 200, 200, 160, 9)

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.plot( ctx, cx, cy, 1)

ims.write_to_png("test.png")
