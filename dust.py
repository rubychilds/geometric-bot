# #!/usr/bin/env python3
import os
import sys
import math
import random
from noise import pnoise1, pnoise2
import cairocffi as cairo

from mod import draw
from mod import utilz
from mod.colz import *

w = 520
h = 520
cx = w / 2
cy = h / 2

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ctx = cairo.Context(ims)

# Clear
ctx.set_operator(cairo.OPERATOR_OVER)
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

class Wind:
    def __init__( self, x, y, angle, radius, force ):
        self.x = x
        self.y = y
        self.angle = angle
        self.current_angle = angle
        self.radius = radius
        self.force = force
        # 25% of probability of attract
        self.force_direction = random.choice( [ -1.0, 1.0, 1.0, 1.0 ] )
        self.noise_base = random.random()
        self.noise_inc  = 0.001
        self.vx = self.force * math.cos( self.current_angle )
        self.vy = self.force * math.sin( self.current_angle )
    def setColor( self, hsl ):
        self.color = Colz()
        self.color.setHsl( hsl )

class Dust:
    def __init__( self ):
        self.x = random.random() * w
        self.y = random.random() * h
        self.mass = random.random()

        # self.color = Colz()
        # self.color.setRgba( 0.1803, 0.80, 0.44, 0.1 + ( self.mass * 0.1 ) )
        # self.color.setRgba( 0.5, 0.5, 0.5, 0.15 + ( self.mass * 0.1 ) )
        self.alpha = 0.08 + ( self.mass * 0.08 )

    def update( self, vx, vy ):
        vx = vx * ( self.mass )
        vy = vy * ( self.mass )
        self.x += vx # + ( random.random() - 0.5 ) * ( 1 - self.mass )
        self.y += vy # + ( random.random() - 0.5 ) * ( 1 - self.mass )
        if self.x > w or self.x < 0 or self.y > h or self.y < 0:
            self.x = random.random() * w
            self.y = random.random() * h
    def render( self, ctx, rgb ):
        # ctx.set_source_rgba(1.0, 1.0, 1.0, 0.1 + ( self.mass * 0.1 ) )
        ctx.set_source_rgba( *rgb, self.alpha )
        draw.plot( ctx, self.x, self.y, 1.0 )

dustdots = []
for i in range(500):
    d0 = Dust()
    # d0.render( ctx )
    dustdots.append( d0 )

# Array to store winds
winds = []
w0_an = random.random() * 2 * math.pi
w0_cx = cx + ( h * 4 ) * math.cos( w0_an )
w0_cy = cy + ( h * 4 ) * math.sin( w0_an )
w0 = Wind(
    w0_cx,
    w0_cy,
    random.random() * 2 * math.pi,
    h * 8, # radius
    random.random() * 10.0  # force
)
w0_hue = random.randint( 0, 359 )
w0.setColor( [ w0_hue, 55, 50 ] ) # Hsl Lime 74, 55, 50
w0.color.setSat( 15 )
w0.color.alpha = 0.15
winds.append( w0 )
print('w0 - f:'+str(w0.force) )

# Addtional winds
for i in range(3):
    f = 3.0 + ( random.random() * 20.0 )
    w1 = Wind(
        random.randint( 0, w ), # x
        random.randint( 0, h ), # y
        0.0,
        random.random() * w / 2,    # radius
        f  # force
    )
    w1.setColor( w0.color.hsl )
    w1.color.setHue( w0_hue + ( i + 1 ) * 30 )
    w1.color.setSat( 55 )
    w1.alpha = 0.5
    winds.append( w1 )
    print('w'+str(i+1)+': '+str(f)+' dir:'+str(w1.force_direction))

# w2 = Wind( 150, 150, random.random() * 2 * math.pi, 180, 10.1 )
# winds.append( w2 )
# w3 = Wind( 450, 450, random.random() * 2 * math.pi, 250, 5.0 )
# winds.append( w3 )
# w4 = Wind( cx, 2 * h, random.random() * 2 * math.pi, 1800, 0.05 )
# winds.append( w4 )

ctx.set_operator(cairo.OPERATOR_ADD)

loops = 800
angle_direction = random.choice( [ -1.0, 1.0, 1.0, 1.0 ] )
print('angle_dir: '+str(angle_direction))
for i in range(loops):
    for dustdot in dustdots:
        temp_c = Colz()
        temp_c.setRgb( winds[0].color.rgb )
        for wind in winds:
            d = utilz.distance( wind.x, wind.y, dustdot.x, dustdot.y )
            a = utilz.angleTo ( wind.x, wind.y, dustdot.x, dustdot.y )
            a *= angle_direction
            force = 0.0
            if d < wind.radius:
                force = wind.force * ( 1 - d / wind.radius ) # d / wind.radius
            if wind.force < 5.0 and wind.force_direction < 0.0:
                force *= wind.force_direction
            vx = force * math.cos( a )
            vy = force * math.sin( a )

            dustdot.update( vx, vy )

            #colores
            d = utilz.distance( wind.x, wind.y, dustdot.x, dustdot.y )
            if d < wind.radius:
                mix = 1 - d / wind.radius
                cmix1 = Colz.interpolate( temp_c, wind.color, mix )
                temp_c.setHsla( *cmix1 )
        # ctx.set_source_rgba( *wind.color.rgb, 1.0)
        dustdot.render( ctx, temp_c.rgb )

for wind in winds:
    ctx.set_source_rgba(0.1, 0.1, 0.1, 1.0)
    draw.plot( ctx, wind.x, wind.y, 6 )
    ctx.set_source_rgba( *wind.color.rgb, 1.0)
    draw.plot( ctx, wind.x, wind.y, 4 )
    print(str(wind.color.rgba))

w = 600
h = 600
ims_final = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
ctx_final = cairo.Context(ims_final)
ctx_final.set_operator(cairo.OPERATOR_OVER)
ctx_final.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx_final.set_source_rgb(0.1, 0.1, 0.1)
ctx_final.fill ()

ctx_final.set_source_surface(ims, 40, 40)
ctx_final.paint()

ctx_final.set_source_rgb( 0.7, 0.7, 0.7 )
ctx_final.rectangle (40, 40, 520, 520)
ctx.set_line_width(2.0)
ctx_final.stroke()

ims_final.write_to_png("dust.png")
