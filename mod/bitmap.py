import os
import sys
import math
import struct

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

def bytes2int(str):
    return int(str.encode('hex'), 16)

# Loops over all the pixels measuring a float value combining rgb
def getLuminanceMedia(surface):
    buf = surface.get_data()
    pixel = 0.0
    for i in range(0,len(buf),4):
        # In some environments pixel data ir returned as by in others as int :(
        r = buf[i]
        if isinstance( r, bytes ):
            r = int.from_bytes( r, byteorder='big' )
        g = buf[i+1]
        if isinstance( g, bytes ):
            g = int.from_bytes( g, byteorder='big' )
        b = buf[i+2]
        if isinstance( b, bytes ):
            b = int.from_bytes( b, byteorder='big' )
        pixel += ( ( r / 255.0 + g / 255.0 + b / 255.0 ) / 3.0 )
    return pixel / (len(buf)/4)
