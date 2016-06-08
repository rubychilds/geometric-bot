#!/usr/bin/env python3
import os
import time
import math
import random
from noise import pnoise1, pnoise2

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from mod import draw

w = 600
h = 600
cx = w / 2
cy = h / 2

now = time.time()

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ctx = cairo.Context(ims)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

ctx.set_operator(cairo.OPERATOR_ADD)

class Arm:
    def __init__ (self, cx, cy, angle = math.pi/2, segments = 250, dis = 2.0):
        self.cx = cx
        self.cy = cy
        self.current_x = cx
        self.current_y = cy
        self.prev_x = cx
        self.prev_y = cy
        self.angle = random.random() * math.pi*2
        self.segments = segments
        self.segment_w = 100.0
        self.segment_w_current = self.segment_w
        self.dis = dis

    def render(self, ctx):
        ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
        seed = random.random() * 9.99

        for i in range(self.segments):

            pn1 = pnoise1 (
                seed + ( i / self.segments * 8 ),
                2,
                0.2,  # persintence 0.2
                4.0,  # Lacunarity 2.0
                256,   # repeat 1024
                # 2
            )
            print(str(pn1))

            _cos = math.cos(self.angle)
            _sin = math.sin(self.angle)
            self.current_x = self.current_x + self.dis * _cos
            self.current_y = self.current_y + self.dis * _sin
            # print(str(self.current_x) + ' ' + str(self.current_y))

            # self.angle += random.random() * 0.1 - 0.05
            self.angle += pn1 / 10
            ctx.set_source_rgba(0.9, 0.9, 0.9, 0.25)
            # draw.plot( ctx, self.current_x, self.current_y, 1)

            # if i != 0:
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

            #self.segment_w_current = self.segment_w * ( 1.0 - i / self.segments )

            self.prev_x = self.current_x
            self.prev_y = self.current_y
            # draw.line( ctx, self.cx, self.cy, self.cx + 30, self.cy )

arm1 = Arm( cx, cy, )
arm1.render( ctx )

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.plot( ctx, cx, cy, 1)

ims.write_to_png("test.png")
