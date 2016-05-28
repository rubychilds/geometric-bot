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

# Vars
paper_w = w * 0.8
paper_h = h * 0.8
paper_r = w * 0.8 / 2 # radius

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, cx, cy, paper_r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, cx, cy, 2)

# Axis A
axis_a_r = random.random() * ( paper_r / 2 ) + paper_r / 10
axis_a_x = cx - paper_r # - ( ( random.random() *  axis_a_r * 2 ) - axis_a_r )
axis_a_y = (h - paper_h) / 2 + random.random() * paper_h
axis_a_init_angle = random.random() * 2 * math.pi

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, axis_a_x, axis_a_y, axis_a_r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, axis_a_x, axis_a_y, 2)

# Axis B
axis_b_r = random.random() * ( paper_r / 2 ) + paper_r / 10
axis_b_x = cx + paper_r # - ( ( random.random() *  axis_b_r * 2 ) - axis_b_r )
axis_b_y = (h - paper_h) / 2 + random.random() * paper_h
axis_b_init_angle = random.random() * 2 * math.pi

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.circle( ctx, axis_b_x, axis_b_y, axis_b_r)
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, axis_b_x, axis_b_y, 2)

# H line
h_line_x1 = axis_a_x + axis_a_r * math.cos( axis_a_init_angle )
h_line_y1 = axis_a_y + axis_a_r * math.sin( axis_a_init_angle )
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, h_line_x1, h_line_y1, 2)
h_line_x2 = axis_b_x + axis_b_r * math.cos( axis_b_init_angle )
h_line_y2 = axis_b_y + axis_b_r * math.sin( axis_b_init_angle )
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, h_line_x2, h_line_y2, 2)
ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.line( ctx, h_line_x1, h_line_y1, h_line_x2, h_line_y2 )

# center point
cp = utilz.lineLerp(  h_line_x1, h_line_y1, h_line_x2, h_line_y2, 0.5 )
ctx.set_source_rgba(0.9, 0, 0, 1.0)
draw.plot( ctx, cp['x'], cp['y'], 2)

ims.write_to_png("test.png")
