# #!/usr/bin/env python3
import os
import time
import math

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from mod import draw
from mod import eaze
from mod import utilz

w = 600
h = 600
cx = w / 2
cy = h / 2

# Flower vars
radius = -1 * h * 0.5 * 0.80; # Radius 80% of canvas
deep = 14
final_angle = 1.0471975511965976 # Math.PI / 3, # 60º
final_angle_factor = 1
subangle_factor = 1
# Elemtents to be draw
circles = []
circles_radius = []
circles_distance_to_center = [0]
easing = 'Quint'
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

# Create surface
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

# Move 0,0 to center of canvas
ctx.translate( cx, cy);

# Calculate circles
last = 0

for i in range(deep):
    circle = []
    t = i / deep
    e_func = getattr( eaze, 'in'+easing )
    f = e_func(t)
    # print(t)

    for j in range(i):
        angle = ( final_angle / i) * j * subangle_factor
        py = f * radius
        point = utilz.rotatePoint(0, 0, 0, py, angle)

        if point[1] != 0:
            circle.append(point)

        if j == 0:
            r = math.fabs(last - py)
            circles_radius.append(r)
            circles_distance_to_center.append(py)
            last = py

        ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
        draw.plot(ctx, point[0], point[1], 1)

circles.append(circle)

# Current time
t0 = int(time.time())

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.plot( ctx, 0, 0, 1)

# Draw circles
for i in range( len(circles), 0, -1 )
    tn = int(time.time())

    line_alpha = 1 - (i / deep)

    col = utilz.hslLerp(palette[0], palette[1], Math.abs(gV.circles_distance_to_center[i] / gV.radius))

ims.write_to_png("test.png")
