# #!/usr/bin/env python3
import os
import sys
import math
import random
import collections
from noise import pnoise1, pnoise2

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from . import draw
from . import name
from . import bitmap

def render():
    w = 480
    h = 480
    cx = w / 2
    cy = h / 2

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(ims)

    # Clear
    ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
    ctx.set_source_rgb(0.1, 0.1, 0.1)
    ctx.fill ()

    num_points = 333
    noise_scale_x = random.random() * 10
    noise_scale_y = random.random() * 10
    points_y = []
    random_rotation = (random.gauss(0, 1))
    print('Random_rotation:'+str(random_rotation))

    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.35)

    # ctx.set_operator(cairo.OPERATOR_SCREEN)
    ctx.set_operator(cairo.OPERATOR_OVERLAY)

    for i in range(num_points):
        py = random.random()
        points_y.append( py )

    for i in range(num_points):
        for j in range(num_points):
            octaves = int(random.random() * 16) + 1
            base = random.random() * 10000
            pn1 = pnoise2(
                i / num_points * noise_scale_x,
                j / num_points * noise_scale_y,
                octaves,   # Octaves 1
                0.2,  # persintence 0.2
                2.0,  # Lacunarity 2.0
                1024,   # repeat 1024
                base  #base 0.0
            )
            ctx.save()
            ctx.rotate( pn1 * random_rotation )
            brush = 0.5 + (8 * pn1)
            ctx.set_operator(cairo.OPERATOR_OVER)
            ctx.set_source_rgba(1.0, 1.0, 1.0, 0.22)
            draw.plot(
                ctx,
                i / num_points * w,
                (points_y[j] * h) + (pn1 * noise_scale_y -  noise_scale_y / 2),
                brush
            )
            ctx.set_operator(cairo.OPERATOR_OVERLAY)
            ctx.set_source_rgba(1.0, 1.0, 1.0, 0.28)
            draw.plot(
                ctx,
                i / num_points * w,
                (points_y[j] * h) + (pn1 * noise_scale_y -  noise_scale_y / 2),
                brush
            )
            ctx.restore()

    # draw.plot( ctx, cx, cy, 1)
    final_w = 600
    final_h = 600
    ims_final = cairo.ImageSurface(cairo.FORMAT_ARGB32, final_w, final_h)
    ctx_final = cairo.Context(ims_final)
    ctx_final.set_operator(cairo.OPERATOR_OVER)
    ctx_final.rectangle(0, 0, final_w, final_h) # Rectangle(x0, y0, x1, y1)
    ctx_final.set_source_rgb(0.1, 0.1, 0.1)
    ctx_final.fill()

    ctx_final.set_source_surface( ims, 60, 60 )
    ctx_final.paint()

    ctx_final.rectangle(60, 60, 480, 480) # Rectangle(x0, y0, x1, y1)
    ctx_final.set_source_rgb(0.35, 0.35, 0.35)
    ctx_final.set_line_width(0.5)
    ctx_final.stroke()

    # Rotate image
    ims_rotated = cairo.ImageSurface(cairo.FORMAT_ARGB32, final_w, final_h)
    ctx_rotated = cairo.Context(ims_rotated)
    ctx_rotated.save()
    ctx_rotated.translate(final_w/2, final_h/2)
    ra = int(random.random() * 4) * 90
    ctx_rotated.rotate( ra * math.pi / 180)
    ctx_rotated.translate(-final_w/2, -final_h/2)

    ctx_rotated.set_source_surface(ims_final, 0, 0)
    ctx_rotated.paint()
    ctx_rotated.restore()

    # gp -> generation params
    gp = collections.OrderedDict()
    gp['name'] = 'perlin-brush'
    gp['params'] = collections.OrderedDict()
    gp['params']['points'] = num_points
    gp['params']['nsx']    = noise_scale_x
    gp['params']['nsy']    = noise_scale_y
    gp['params']['ra']     = random_rotation

    footline = name.footline( gp )
    draw.footline( ctx_rotated, footline )
    filename = name.filename( gp )

    # invert image
    if int(random.random() * 2) == 0:
        bitmap.negative( ims_rotated )

    return ims_rotated, filename, footline
