# #!/usr/bin/env python3
import os
import time
import math
import pyglet
import ctypes

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

from mod import draw

w = 600
h = 600
cx = w / 2
cy = h / 2

# Pyglet window
window = pyglet.window.Window( w, h )

# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h) # Simple Surface
data = (ctypes.c_ubyte * w * h * 4)()
stride = w * 4
ims = cairo.ImageSurface.create_for_data( data, cairo.FORMAT_ARGB32, w, h, stride)
ctx = cairo.Context(ims)

#pyglet
texture = pyglet.image.Texture.create_for_size(pyglet.gl.GL_TEXTURE_2D, w, h, pyglet.gl.GL_RGB)

# Clear
ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill ()

ctx.set_source_rgba(192, 0, 0, 0.5)
draw.circle( ctx, 200, 200, 160, 9)

ctx.set_source_rgba(0.9, 0.9, 0.9, 0.5)
draw.plot( ctx, cx, cy, 1)

ims.write_to_png("test.png")

@window.event
def on_draw():
    ctx.rectangle (0, 0, w, h) # Rectangle(x0, y0, x1, y1)
    ctx.set_source_rgb(0.1, 0.1, 0.1)
    ctx.fill()

    ctx.set_source_rgba(0.9, 0, 0, 1.0)
    draw.plot( ctx, cx, cy, 1)

    window.clear()

    pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
    pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, texture.id)

    pyglet.gl.glTexImage2D(pyglet.gl.GL_TEXTURE_2D, 0, pyglet.gl.GL_RGBA, w, h, 1, pyglet.gl.GL_BGRA, pyglet.gl.GL_UNSIGNED_BYTE, data)

    pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
    pyglet.gl.glTexCoord2f(0.0, 1.0)
    pyglet.gl.glVertex2i(0, 0)
    pyglet.gl.glTexCoord2f(1.0, 1.0)
    pyglet.gl.glVertex2i( w, 0 )
    pyglet.gl.glTexCoord2f(1.0, 0.0)
    pyglet.gl.glVertex2i( w, h )
    pyglet.gl.glTexCoord2f(0.0, 0.0)
    pyglet.gl.glVertex2i(0, h )
    pyglet.gl.glEnd()

    ctx.set_source_rgb(1, 0, 0)
    ctx.paint()

pyglet.app.run()
