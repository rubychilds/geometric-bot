# #!/usr/bin/env python3
import os
import sys
import math
import random
import collections

import cairocffi as cairo

from . import draw
from . import name
from mod.colz  import *

# Clear
def clear( ctx, w, h ):
    ctx.rectangle( 0, 0, w, h ) # Rectangle(x0, y0, x1, y1)
    ctx.set_source_rgb( 0.1, 0.1, 0.1 )
    ctx.fill()

class Zircle:
    def __init__( self, cx, cy, r ):
        self.r = r
        # self.sw = random
        self.cx = cx
        self.cy = cy
        self.orientation = 'A'
        self.painted = False

        # top, right, bottom, left
        self.top    = [ cx + r * math.cos( math.radians( 270 ) ), cy + r * math.sin( math.radians( 270 ) ) ]
        self.right  = [ cx + r * math.cos( 0 ), cy + r * math.sin( 0 ) ]
        self.bottom = [ cx + r * math.cos( math.radians( 90 ) ), cy + r * math.sin( math.radians( 90 ) ) ]
        self.left   = [ cx + r * math.cos( math.radians( 180 ) ), cy + r * math.sin( math.radians( 180 ) ) ]

        self.tr_painted = False
        self.tl_painted = False
        self.br_painted = False
        self.bl_painted = False
    def render( self, ctx, sw, sector_wh ):
        # ctx.save()
        # ctx.set_operator(cairo.OPERATOR_OVER)
        # ctx.set_source_rgba(1.0, 1.0, 1.0, 0.05)
        # draw.circle( ctx, self.cx, self.cy, self.r)
        # ctx.set_line_width(0.5)
        # ctx.stroke()
        # ctx.restore()

        ctx.set_line_width( sw )

        ctx.set_operator(cairo.OPERATOR_SCREEN)
        ctx.set_source_rgba( 1.0, 1.0, 1.0, 0.05 + 0.25 * (1 - sw / sector_wh ) )

        # self.dir = random.sample(range(0, 4), 2) # two random
        # if 0 in self.dir: # TL
        #     ctx.arc(self.cx - self.r, self.cy - self.r, self.r, 0, arc)
        #     ctx.stroke()
        # if 1 in self.dir: # BR
        #     ctx.arc(self.cx + self.r, self.cy + self.r, self.r, arc * 2, arc * 3)
        #     ctx.stroke()
        # if 2 in self.dir: # TR
        #     ctx.arc(self.cx + self.r, self.cy - self.r, self.r, arc, arc * 2)
        #     ctx.stroke()
        # if 3 in self.dir: # BL
        #     ctx.arc(self.cx - self.r, self.cy + self.r, self.r, arc * 3, 0 )
        #     ctx.stroke()

        self.orientation = random.choice( [ 'A', 'B' ] )
        if self.orientation == 'A':
            self.draw( ctx, 'tl' )
            self.draw( ctx, 'br' )
        else:
            self.draw( ctx, 'tr' )
            self.draw( ctx, 'bl' )
        # print(self.orientation)

    def draw( self, ctx, sector ):
        arc = 2 * math.pi / 4
        if sector == 'tl':
            ctx.arc(self.cx - self.r, self.cy - self.r, self.r, 0, arc)
            ctx.stroke()
        if sector == 'br':
            ctx.arc(self.cx + self.r, self.cy + self.r, self.r, arc * 2, arc * 3)
            ctx.stroke()
        if sector == 'tr':
            ctx.arc(self.cx + self.r, self.cy - self.r, self.r, arc, arc * 2)
            ctx.stroke()
        if sector == 'bl':
            ctx.arc(self.cx - self.r, self.cy + self.r, self.r, arc * 3, 0 )
            ctx.stroke()

# Dibuja los sectores de las líneas
def draw_line_path ( ctx, mx, my, from_ = 'top' ):
    global painted_sectors, prev_mx, prev_my, prev_orientation, num_zircles, dir_

    if mx < 0 or mx > num_zircles - 1 or my < 0 or my > num_zircles - 1:
        #print( 'Done!' )
        return

    painted_sectors += 1

    idx = mx + my * num_zircles
    # print( 'idx: '+str(idx) )
    z = zircles[ idx ]

    # print( z.orientation+' | '+from_ )
    if z.orientation == 'A':
        if from_ == 'top':
            if z.tl_painted == True:
                return
            z.draw( ctx, 'tl' )
            z.tl_painted = True
            draw_line_path( ctx, mx - 1, my, 'right' )
        if from_ == 'right':
            if z.br_painted == True:
                return
            z.draw( ctx, 'br' )
            z.br_painted = True
            draw_line_path( ctx, mx, my + 1, 'top' )
        if from_ == 'bottom':
            if z.br_painted == True:
                return
            z.draw( ctx, 'br' )
            z.br_painted = True
            draw_line_path( ctx, mx+1, my, 'left' )
        if from_ == 'left':
            if z.tl_painted == True:
                return
            z.draw( ctx, 'tl' )
            z.tl_painted = True
            draw_line_path( ctx, mx, my - 1, 'bottom' )
    elif z.orientation == 'B':
        if from_ == 'top':
            if z.tr_painted == True:
                return
            z.draw( ctx, 'tr' )
            z.tr_painted = True
            draw_line_path( ctx, mx + 1, my, 'left' )
        if from_ == 'right':
            if z.tr_painted == True:
                return
            z.draw( ctx, 'tr' )
            z.tr_painted = True
            draw_line_path( ctx, mx, my - 1, 'bottom' )
        if from_ == 'bottom':
            if z.bl_painted == True:
                return
            z.draw( ctx, 'bl' )
            z.bl_painted = True
            draw_line_path( ctx, mx - 1, my, 'right' )
        if from_ == 'left':
            if z.bl_painted == True:
                return
            z.draw( ctx, 'bl' )
            z.bl_painted = True
            draw_line_path( ctx, mx, my + 1, 'top' )

# Global vars
num_zircles = random.randint( 2, 16 ) #32
print(str(num_zircles))
zircles = []

# Recorrer los círculos y hacer una línea
prev_mx = -9999
prev_my = -9999
prev_orientation = ''
dir_ = None
painted_sectors = 0

# from top
c1 = Colz()
c1.setHex('E06E53')
c1.rotateHue( random.random() )
c1.a = 0.8

# Main renderer
def render():
    w = 600
    h = 600
    cx = w / 2
    cy = h / 2

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
    ctx = cairo.Context(ims)

    clear( ctx, w, h )

    lienzo = 0.8 * w
    sector_wh = lienzo / num_zircles
    offset = sector_wh / 2 + ( ( w - lienzo ) / 2 )

    sw = max(4, random.random() * sector_wh)
    if num_zircles > 8:
        sw *= 0.5
    print('Base sw: '+str(sw))

    for i in range(num_zircles):
        for j in range(num_zircles):
            x = offset + sector_wh * j
            y = offset + sector_wh * i
            # offset_y
            r = sector_wh / 2
            zircle = Zircle( x, y, r )
            zircle.render( ctx, sw, sector_wh )
            zircles.append( zircle )

    color_sw = max(1.5, random.random() * sector_wh)
    ctx.set_line_width( color_sw )

    while painted_sectors / 4 < num_zircles ** 2 * 0.20 :

        ctx.set_operator(cairo.OPERATOR_ADD)
        ctx.set_source_rgba( *c1.rgba )

        ini_x = random.randint( 1, num_zircles - 1 )
        ini_y = random.randint( 1, num_zircles - 1 )
        draw_line_path ( ctx, ini_x, ini_y, 'top' )
        draw_line_path ( ctx, ini_x, ini_y -1, 'bottom' )

        c1.rotateHue( -5 )
        c1.setLum( c1.l * 0.99 )

    print('Painted sectors: '+str(painted_sectors))

    gp = collections.OrderedDict()
    gp['name'] = 'zircles'
    gp['params'] = collections.OrderedDict()
    gp['params']['matrix'] = num_zircles
    gp['params']['bsw'] = sw
    gp['params']['csw'] = color_sw

    footline = name.footline( gp )
    draw.footline( ctx, footline)
    filename = name.filename( gp )

    return ims, filename, footline

    # ims.write_to_png("test.png")
