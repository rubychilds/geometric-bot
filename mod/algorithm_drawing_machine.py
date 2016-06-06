# #!/usr/bin/env python3
import os
import time
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
from . import utilz

# Objects
class Axis:
    def __init__ ( self, cx, cy, r, angle_inc = 0 ):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.angle_current = random.random() * 2 * math.pi
        self.angle_inc = angle_inc
    def rotate( self, angle = 0 ):
        # if angle == None:
        #     angle = self.angle_inc
        self.angle_current += angle
        return self
    def getPoint( self ):
        x = self.cx + self.r * math.cos( self.angle_current )
        y = self.cy + self.r * math.sin( self.angle_current )
        return [ x, y ]

def render():

    w = 600
    h = 600
    cx = w / 2
    cy = h / 2
    t = 0

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(ims)

    # Clear
    ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
    ctx.set_source_rgb(0.1, 0.1, 0.1)
    ctx.fill ()

    # Vars

    # "Paper"
    paper_w = w * 0.8
    paper_h = h * 0.8
    paper_r = w * 0.8 / 2 # radius
    paper_inc_angle = random.random() * 5 - 2.5 # -2.5 / 2.5

    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.circle( ctx, cx, cy, paper_r)
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, cx, cy, 2)

    # Axis A
    axis_a = Axis(
        cx - paper_r, # - ( ( random.random() *  axis_a_r * 2 ) - axis_a_r )
        (h - paper_h) / 2 + random.random() * paper_h,
        random.random() * ( paper_r / 2 ) + paper_r / 10,
        0
    )

    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.circle( ctx, axis_a.cx, axis_a.cy, axis_a.r)
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, axis_a.cx, axis_a.cy, 2)

    axis_b = Axis(
        cx + paper_r, # - ( ( random.random() *  axis_a_r * 2 ) - axis_a_r )
        (h - paper_h) / 2 + random.random() * paper_h,
        random.random() * ( paper_r / 2 ) + paper_r / 10,
        0
    )

    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.circle( ctx, axis_b.cx, axis_b.cy, axis_b.r)
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, axis_b.cx, axis_b.cy, 2)

    # Rod (eje que une las ruedas de una locomotora)
    pa = axis_a.getPoint()
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, pa[0], pa[1], 2)
    pb = axis_b.getPoint()
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, pb[0], pb[1], 2)
    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.line( ctx, pa[0], pa[1], pb[0], pb[1] )
    rod_length = utilz.distance( pa[0], pa[1], pb[0], pb[1] )

    # center axis
    rod_center = utilz.lineLerp( pa[0], pa[1], pb[0], pb[1], 0.5 )
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, rod_center['x'], rod_center['y'], 2)

    axis_final = Axis(
        rod_center['x'],
        rod_center['y'],
        max(random.random() * paper_w / 2, 60), # (random.random() * rod_length / 4) + rod_length / 6,
        0
    )
    # axis_final.cx = rod_center['x']
    # axis_final.cy = rod_center['y']

    # final point "pencil"
    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.circle( ctx, axis_final.cx, axis_final.cy, axis_final.r)
    pencil = axis_final.getPoint()
    ctx.set_source_rgba(0.9, 0, 0, 0.2)
    draw.plot( ctx, pencil[0], pencil[1], 2)
    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.2)
    draw.line( ctx, axis_final.cx, axis_final.cy, pencil[0], pencil[1] )
    last_x = pencil[0]
    last_y = pencil[1]

    ctx.set_source_rgba(0.9, 0.9, 0.9, 0.25)
    ctx.set_line_width(1.2)

    iteraciones = random.randint(2000, 40000)
    ROT = ( 90 * 2 * math.pi ) / iteraciones
    print(iteraciones)

    axis_a_rot_factor = random.randint(1, 12) + 0.005
    axis_b_rot_factor = random.randint(1, 12) + 0.005
    axis_p_rot_factor = random.randint(1, 12) + 0.005
    while axis_a_rot_factor == axis_p_rot_factor or axis_b_rot_factor == axis_p_rot_factor:
         axis_p_rot_factor = random.randint(2, 12) + 0.005

    #print('ROT:' + str(ROT) )
    print('a: ' + str(axis_a_rot_factor))
    print('b: ' + str(axis_b_rot_factor))
    print('p: ' + str(axis_p_rot_factor))

    hsl = [ 0.069, 1.0, 0.5 ]

    ctx.set_operator(cairo.OPERATOR_SCREEN)
    h = random.random()

    video_framecount = 0

    for i in range(iteraciones):

        rotation = i * ROT

        pa = axis_a.rotate( ROT * axis_a_rot_factor ).getPoint()
        pb = axis_b.rotate( ROT * axis_b_rot_factor ).getPoint()
        rod_center = utilz.lineLerp( pa[0], pa[1], pb[0], pb[1], 0.5 )
        axis_final.cx = rod_center['x']
        axis_final.cy = rod_center['y']
        pencil = axis_final.rotate( ROT * axis_p_rot_factor  ).getPoint()

        pencil_r = utilz.rotatePoint( cx, cy,  pencil[0], pencil[1], rotation )

        s = 1 - (utilz.distance( cx, cy,  pencil[0], pencil[1] ) / (paper_w / 2))
        rgb = colorsys.hsv_to_rgb( h, s, 0.5)
        ctx.set_source_rgba( *rgb, 0.25)

        ctx.move_to( last_x, last_y )
        ctx.line_to( pencil_r[0], pencil_r[1] )
        ctx.stroke()
        last_x = pencil_r[0]
        last_y = pencil_r[1]

        if i % 100 == 0 and True:
            print( video_framecount )
            ims.write_to_png( './video/'+str(video_framecount).rjust(8, '0')+'.png' )
            video_framecount += 1

    gp = collections.OrderedDict()
    gp['name'] = 'drawing-machine'
    gp['params'] = collections.OrderedDict()
    gp['params']['loop'] = iteraciones
    gp['params']['a'] = axis_a_rot_factor
    gp['params']['b'] = axis_b_rot_factor
    gp['params']['p'] = axis_p_rot_factor

    footline = name.footline( gp )
    draw.footline( ctx, footline)
    filename = name.filename( gp )

    return ims, filename, footline
