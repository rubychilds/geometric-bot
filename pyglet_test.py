#!/usr/bin/env python3
import pyglet

w = 600
h = 600

window = pyglet.window.Window( w, h )
image = pyglet.resource.image('test.png')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
