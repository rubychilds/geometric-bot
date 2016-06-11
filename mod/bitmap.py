import os
import math

if os.name == 'nt': # Is windows
    import cairo
else:
    import cairocffi as cairo

# Negative image
# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
# ctx = cairo.Context(ims)
# bitmap.negative( ims )
def negative(surface):
    buf = surface.get_data()
    for i in range(0,len(buf),4):
        buf[i]   = 255 - buf[i]
        buf[i+1] = 255 - buf[i+1]
        buf[i+2] = 255 - buf[i+2]

# Loops over all the pixels measuring a float value combining rgb
# 
def getLuminanceMedia(surface):
    buf = surface.get_data()
    pixel = 0.0
    for i in range(0,len(buf),4):
        pixel += ( ( buf[i]/255 + buf[i+1]/255 + buf[i+2]/255 ) / 3 )
    return pixel / (len(buf)/4)
