# #!/usr/bin/env python3
import os
import time
import math

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

# Flower vars
radius = 0
deep = 14
final_angle = 1.0471975511965976 # Math.PI / 3, # 60º
final_angle_factor = 1
subangle_factor = 1
# Elemtents to be draw
circles = []
circles_radius = []
circles_distance_to_center = [0]
easing = 'quint'
# Colores gradientes
grd_fondo = None
# Time
t0 = 0
tb = 0
t_factor = 0
# colors
palette = [
    [ 30,  81, 52 ],
    [ 220, 77, 48 ]
]

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

# Move 0,0 to center of canvas
ctx.translate( cx, cy);
radius = -1 * h * 0.5 * 0.80; # Radius 80% of canvas

# ctx.set_source_rgba(192, 0, 0, 0.5)
# circle( ctx, 200, 200, 160, 9)

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.plot( ctx, 0, 0, 1)

ims.write_to_png("test.png")
