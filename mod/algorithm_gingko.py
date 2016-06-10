# #!/usr/bin/env python3
import os
import time
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
from . import utilz
from mod.colz  import *

# Global Vars
w = 600
h = 600
cx = w / 2
cy = h / 2

col = Colz()
col.setHsla( random.randint(0, 359), 51, 50, 0.25)


ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

ctx.set_operator(cairo.OPERATOR_OVER)
ctx.set_operator(cairo.OPERATOR_SCREEN)
ctx.set_line_width(1.0)

num_of_arms = random.randint(2, 9)

# Objects
class Arm:
    def __init__ (self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.segments = random.randint( 1000, 5000)
        self.dis = random.uniform(0.25, 0.65)
        self.segment_w = random.randint(50, 250)
        self.segment_w_current = self.segment_w
        self.noise_seed = random.random() * 10.0
        self.noise_speed = 4.0 + ( random.random() * 6.0 )
        self.noise_base = random.randint(1, 16)

        if num_of_arms < 4:
            self.segment_w *= 3

    def render(self, ctx):
        self.current_x = cx
        self.current_y = cy
        self.prev_x = cx
        self.prev_y = cy
        self.angle = 0 # random.random() * math.pi*2

        for i in range(self.segments):

            pn1 = pnoise1 (
                self.noise_seed + ( (i / self.segments) * self.noise_speed ),
                2,
                0.2,  # persintence 0.2
                4.0,  # Lacunarity 2.0
                1024,   # repeat 1024
                self.noise_base
            )
            # print(str(pn1))

            _cos = math.cos(self.angle)
            _sin = math.sin(self.angle)
            self.current_x = self.current_x + self.dis * _cos
            self.current_y = self.current_y + self.dis * _sin

            self.angle += pn1 / 60.0

            self.segment_w_current = self.segment_w * pn1 * 2

            col.a = 0.5 + (pn1 * 0.5)
            col.rotateHue( pn1 / random.randint( 200, 4000) )
            # col.setSat( 0.0 )
            ctx.set_source_rgba( *col.rgba)
            # draw.plot( ctx, self.current_x, self.current_y, 1)

            ABx =  self.current_x - self.prev_x
            ABy =  self.current_y - self.prev_y
            NABx = ABx / self.dis
            NABy = ABy / self.dis
            PNABx = -NABy
            PNABy =  NABx
            Dx1 = self.current_x + self.segment_w_current * PNABx
            Dy1 = self.current_y + self.segment_w_current * PNABy
            Dx2 = self.current_x - self.segment_w_current * PNABx
            Dy2 = self.current_y - self.segment_w_current * PNABy
            draw.line( ctx, Dx1, Dy1, Dx2, Dy2)

            self.prev_x = self.current_x
            self.prev_y = self.current_y
            # draw.line( ctx, self.cx, self.cy, self.cx + 30, self.cy )

def render():

    arm1 = Arm( 0, 0 )

    ctx.save()
    for i in range(num_of_arms):
        ctx.save()
        ctx.translate(cx, cy)
        ctx.rotate( 2 * math.pi / num_of_arms * i )
        ctx.translate(-cx, -cy)
        arm1.render( ctx )
        ctx.restore()

    # ims.write_to_png("test.png")

    gp = collections.OrderedDict()
    gp['name'] = 'gingko'
    gp['params'] = collections.OrderedDict()
    gp['params']['a'] = num_of_arms
    gp['params']['s'] = arm1.segments
    gp['params']['d'] = arm1.dis
    gp['params']['w'] = arm1.segment_w
    gp['params']['ns'] = arm1.noise_seed
    gp['params']['np'] = arm1.noise_speed
    gp['params']['nb'] = arm1.noise_base

    footline = name.footline( gp )
    draw.footline( ctx, footline)
    filename = name.filename( gp )

    return ims, filename, footline
