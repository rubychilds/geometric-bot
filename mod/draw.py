import os
import math

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

def plot (ctx, cx, cy, r):
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
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
    ctx.set_source_rgba( 1.0, 1.0, 1.0, 0.8 )
    ctx.set_operator(cairo.OPERATOR_OVER)
    # ctx.set_operator(cairo.OPERATOR_DIFFERENCE)
    ctx.select_font_face("Hack", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(10)
    ctx.set_antialias(cairo.ANTIALIAS_GRAY)
    ctx.move_to( x, y)
    ctx.show_text('@GeometricBot | '+text )

# Negative image
def negative(surface):
    buf = surface.get_data()
    for i in range(0,len(buf),4):
        buf[i]   = 255 - buf[i]
        buf[i+1] = 255 - buf[i+1]
        buf[i+2] = 255 - buf[i+2]
