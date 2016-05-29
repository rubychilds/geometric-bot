# #!/usr/bin/env python3
import os
import time
import math
import random

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from mod import draw
from mod import utilz

# Objects
class Axis:
    def __init__ ( self, cx, cy, r, angle_inc = 0 ):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.angle_current = random.random() * 2 * math.pi
        self.angle_inc = angle_inc
    def rotate( self ):
        self.angle_current += self.angle_inc
    def getPoint( self ):
        x = self.cx + self.r * math.cos( self.angle_current )
        y = self.cy + self.r * math.sin( self.angle_current )
        return [ x, y ]

w = 600
h = 600
cx = w / 2
cy = h / 2
t = 0
iteraciones = 1000

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

# Vars

# "Paper"
paper_w = w * 0.8
paper_h = h * 0.8
paper_r = w * 0.8 / 2 # radius
paper_inc_angle = random.random() * 5 - 2.5 # -2.5 / 2.5

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, cx, cy, paper_r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, cx, cy, 2)

# Axis A
axis_a = Axis(
    cx - paper_r, # - ( ( random.random() *  axis_a_r * 2 ) - axis_a_r )
    (h - paper_h) / 2 + random.random() * paper_h,
    random.random() * ( paper_r / 2 ) + paper_r / 10,
    random.random() * 5 - 2.5
)

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, axis_a.cx, axis_a.cy, axis_a.r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, axis_a.cx, axis_a.cy, 2)

axis_b = Axis(
    cx + paper_r, # - ( ( random.random() *  axis_a_r * 2 ) - axis_a_r )
    (h - paper_h) / 2 + random.random() * paper_h,
    random.random() * ( paper_r / 2 ) + paper_r / 10,
    random.random() * 5 - 2.5
)

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, axis_b.cx, axis_b.cy, axis_b.r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, axis_b.cx, axis_b.cy, 2)

# H line
pa = axis_a.getPoint()
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, pa[0], pa[1], 2)
pb = axis_b.getPoint()
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, pb[0], pb[1], 2)
ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.line( ctx, pa[0], pa[1], pb[0], pb[1] )
axis_distance = utilz.distance( pa[0], pa[1], pb[0], pb[1] )

# center axis
h_line_cp = utilz.lineLerp( pa[0], pa[1], pb[0], pb[1], 0.5 )
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, h_line_cp['x'], h_line_cp['y'], 2)

axis_final = Axis(
    h_line_cp['x'],
    h_line_cp['y'],
    random.random() * axis_distance / 2,
    0
)

# final point "pen"
ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, axis_final.cx, axis_final.cy, axis_final.r)
pen = axis_final.getPoint()
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, pen[0], pen[1], 2)
ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.line( ctx,axis_final.cx, axis_final.cy, pen[0], pen[1] )

# for i in range(iteraciones):


ims.write_to_png("test.png")
