# #!/usr/bin/env python3
import os
import sys
import time
import math
import random
import colorsys

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
final_angle = 1.0471975511965976 # Math.PI / 3, # 60º

deep = random.randint(3, 32)
print('Deep:' + str(deep))
subangle_factor = (random.random() * 10) - 5.0
print('Subangle:' + str(subangle_factor))

direction = random.choice(['in', 'out', 'inOut'])
avaliable_easings = ['Quint', 'Cubic', 'Quad', 'Sine', 'Back', 'Bounce', 'Elastic']
if (direction == 'inOut') or (direction == 'in'):
    avaliable_easings.remove('Elastic');
    avaliable_easings.remove('Back');
easing = random.choice(avaliable_easings)
print('Easing:' + direction + easing)

# Elemtents to be draw
circles = []
circles_radius = []
circles_distance_to_center = [0]

# colors
# palette = [ [ 30,  81, 52 ], [ 220, 77, 48 ] ]
palette = [ [ 0.0833,  0.81, 0.52 ], [ 0.6111, 0.77, 0.48 ] ]

# Create surface
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

# Move 0,0 to center of canvas
ctx.translate( cx, cy )

# Calculate circles
last = 0

for i in range(deep):
    circle = []
    t = i / deep
    e_func = getattr( eaze, direction + easing )
    f = e_func(t)
    # print(t)

    ctx.rotate( random.random() )

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

        # ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
        # draw.plot(ctx, point[0], point[1], 1)

    if len(circle) > 0:
        circles.append(circle)
        #print(circle)

# ims.write_to_png("test.png")
# sys.exit()

# Current time
t0 = int(time.time())

# Draw circles
for i in range( len(circles) -1, 0, -1 ):

    line_alpha = 1 - (i / deep)

    col = utilz.hslLerp(palette[0], palette[1], math.fabs(circles_distance_to_center[i] / radius))
    # print(col)

    # Draw 6 times
    for k in range(6):

        ctx.rotate(final_angle)
        ctx.set_operator(cairo.OPERATOR_SCREEN)

        # Draws all circles in current level
        for j in range(len(circles[i])):

            grd = cairo.RadialGradient( circles[i][j][0], circles[i][j][1], circles_radius[i-1]*0.64, circles[i][j][0], circles[i][j][1], circles_radius[i-1] )

            grd.add_color_stop_rgba(0, 0.85, 0.108, 0.333, 0.12)
            grd.add_color_stop_rgba(1, 0.85, 0.108, 0.333, 0.60)
            rgb = colorsys.hsv_to_rgb( *col )
            grd.add_color_stop_rgba(0, *rgb, 0.10)
            grd.add_color_stop_rgba(1, *rgb, 0.75)
            ctx.set_source(grd)

            draw.plot( ctx, circles[i][j][0], circles[i][j][1], circles_radius[i-1] )

            ctx.set_source_rgba( *rgb, line_alpha )
            draw.circle( ctx, circles[i][j][0], circles[i][j][1], circles_radius[i-1] );

    # Cover central part of current level of circles
    if ( i > 1 ):
        grd_tapa = cairo.RadialGradient( 0, 0, math.fabs( circles[i][0][1] )*0.78, 0, 0, math.fabs( circles[i][0][1] ) )
        grd_tapa.add_color_stop_rgba(0.0, 0.1, 0.1, 0.1, 1.0)
        grd_tapa.add_color_stop_rgba(1.1, 0.1, 0.1, 0.1, 0.0)
        ctx.set_source(grd_tapa)
        ctx.set_operator(cairo.OPERATOR_OVER)
        draw.plot(ctx, 0, 0, math.fabs( circles[i][0][1] ))

ims.write_to_png("test.png")
