import os
import math

import cairocffi as cairo

def plot (ctx, cx, cy, r = 2.0):
    ctx.arc(cx, cy, r, 0, 2.0 * math.pi)
    ctx.fill ()

def circle (ctx, cx, cy, r, sw = 1.0):
    ctx.set_line_width(sw)
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.stroke()

def line (ctx, x1, y1, x2, y2):
    ctx.move_to( x1, y1 )
    ctx.line_to( x2, y2 )
    ctx.stroke()

# Negative image
def footline(ctx, text, x=8, y=590):
    ctx.set_source_rgba( 1.0, 1.0, 1.0, 0.6 )
    #ctx.set_operator(cairo.OPERATOR_OVER)
    ctx.set_operator(cairo.OPERATOR_DIFFERENCE)
    ctx.select_font_face("Hack", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(10)
    ctx.set_antialias(cairo.ANTIALIAS_GRAY)
    ctx.move_to( x, y)
    ctx.show_text('@GeometricBot | '+text )
