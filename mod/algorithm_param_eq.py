# Parametric equations
# https://en.wikipedia.org/wiki/Parametric_equation
import os
import sys
import math
import random
import colorsys
import collections

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from . import draw
from . import name

def render():
    w = 600
    h = 600
    cx = w / 2
    cy = h / 2
    angle = 0
    angle_inc = 0.22
    iteraciones = 100000
    paper_angle_inc = 0.000001
    print(paper_angle_inc)

    parameters = []
    p0 = math.ceil(random.random() * 4)
    p1 = math.ceil(random.random() * 8)
    p2 = math.ceil(random.random() * 64)
    p3 = math.ceil(random.random() * 512)

    if p0 == 0: p0 = 2
    if p1 == 0: p1 = 2
    if p2 == 0: p2 = 3
    if p3 == 0: p3 = 3

    print(p0, p1, p2, p3)

    parameters.append(p0)
    parameters.append(p1)
    parameters.append(p2)
    parameters.append(p3)
    random.shuffle(parameters)

    pa = parameters.pop()
    pb = parameters.pop()
    pc = parameters.pop()
    pd = parameters.pop()

    sum = pa + pb + pc + pd

    print(pa, pb, pc, pd, 'sum:', (pa+pb+pc+pd) )

    scale_factor = 0

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(ims)

    # ctx.set_source_rgba(192, 0, 0, 1)
    # ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
    #     cairo.FONT_WEIGHT_NORMAL)
    # ctx.set_font_size(40)
    # ctx.move_to(10, 50)
    # ctx.show_text("Disziplin ist Macht.")

    ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
    ctx.set_source_rgb(0.1, 0.1, 0.1)
    ctx.fill ()

    # ctx.set_source_rgba(192, 0, 0, 0.5)
    # circle( ctx, 200, 200, 160, 9)

    rgba_a = [0.96, 0.80, 0.18, 0.12 ]
    h, s, v = colorsys.rgb_to_hsv( rgba_a[0], rgba_a[1], rgba_a[2] )
    h = random.random()
    s = s / 2

    ctx.set_source_rgba( *rgba_a )
    draw.plot( ctx, cx, cy, 1)

    ctx.set_operator(cairo.OPERATOR_OVERLAY)
    # ctx.set_operator(cairo.OPERATOR_ADD)

    ctx.translate( cx, cy)

    for i in range(iteraciones):

        x = ( math.cos( angle * pa) - math.cos ( angle * pb ) ) * 120
        y = ( math.sin( angle * pc) - math.sin ( angle * pd ) ) * 120

        # hypotrochoid
        # x = ( ( R - r ) * math.cos( angle ) ) + d * math.cos ( f * angle )
        # y = ( ( R - r ) * math.sin( angle ) ) - d * math.sin ( f * angle )

        # h_ = h + ( 0.5 * (i / iteraciones) )
        # if h_ > 1: h_ = h - 1.0
        r, g, b = colorsys.hsv_to_rgb( h, s, v )
        ctx.set_source_rgba( r, g, b, rgba_a[3] )

        ctx.set_operator(cairo.OPERATOR_ADD)
        draw.plot( ctx, x, y, 1.0)
        ctx.set_operator(cairo.OPERATOR_OVERLAY)
        draw.plot( ctx, x, y, 1.0)

        # ctx.set_line_width(1)
        # ctx.set_source_rgba(0.9, 0.9, 0.9, 0.1)
        # ctx.move_to( cx, cy)
        # ctx.line_to(x, y)
        # ctx.stroke()

        # ctx.save()
        # ctx.translate( cx, cy)
        # if sum < 65: ctx.rotate( paper_angle_inc )
        # ctx.translate( -cx, -cy)
        # ctx.restore()

        angle += angle_inc

    # gp -> generation params
    gp = collections.OrderedDict()
    gp['name'] = 'param-eq'
    gp['params'] = collections.OrderedDict()
    gp['params']['a'] = pa
    gp['params']['b'] = pb
    gp['params']['c'] = pc
    gp['params']['d'] = pd
    gp['params']['i'] = iteraciones
    gp['params']['rad+'] = angle_inc

    ctx.translate( -cx, -cy)
    footline = name.footline( gp )
    draw.footline( ctx, footline )
    filename = name.filename( gp )

    return ims, filename, footline
