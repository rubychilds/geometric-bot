import os
import sys
import math
import struct

import cairocffi as cairo

# Negative image
# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
# ctx = cairo.Context(ims)
# bitmap.negative( ims )
def negative(surface):
    buf = surface.get_data()
    for i in range(0,len(buf),4):
        r = buf[i]
        if isinstance( r, bytes ):
            r = int.from_bytes( r, byteorder='big' )
        r = 255 - r

        g = buf[i+1]
        if isinstance( g, bytes ):
            g = int.from_bytes( g, byteorder='big' )
        g = 255 - g

        b = buf[i+2]
        if isinstance( b, bytes ):
            b = int.from_bytes( b, byteorder='big' )
        b = 255 - b

        buf[i]   = struct.pack("B", r)
        buf[i+1] = struct.pack("B", g)
        buf[i+2] = struct.pack("B", b)

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
    return pixel / ( len( buf ) / 4 )

# Constrast image
# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
# ctx = cairo.Context(ims)
# bitmap.contrast( ims, [ -100 - 100 ] )
def contrast(surface, contrast):
    buf = surface.get_data()
    factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
    print(str(factor))

    for i in range(0,len(buf),4):
        r = buf[i]
        if isinstance( r, bytes ):
            r = int.from_bytes( r, byteorder='big' )
        r = ( factor * ( r - 128 ) ) + 128

        g = buf[i+1]
        if isinstance( g, bytes ):
            g = int.from_bytes( g, byteorder='big' )
        g = ( factor * ( g - 128 ) ) + 128

        b = buf[i+2]
        if isinstance( b, bytes ):
            b = int.from_bytes( b, byteorder='big' )
        b = ( factor * ( b - 128 ) ) + 128

        buf[i]   = struct.pack("B", int(r))
        buf[i+1] = struct.pack("B", int(g))
        buf[i+2] = struct.pack("B", int(b))

# Levels adjusteemnt a-la Photoshop
# Original code from https://github.com/talentedmrjones/Javascript-Canvas-Tools/blob/master/canvasTools.js
# Pass an options object as follow:
# level_op = {
#     'gamma': 1.0,
#     'input': {
#         'min': 100,
#         'max': 230
#     },
#     'output': {
#         'min': 0,
#         'max': 255
#     }
# }
# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
# ctx = cairo.Context(ims)
# bitmap.levels( ims, level_op )
def levels( surface, options ):
    buf = surface.get_data()
    minInput  = options['input']['min'] / 255
    maxInput  = options['input']['max'] / 255
    minOutput = options['output']['min'] / 255
    maxOutput = options['output']['max'] / 255

    for i in range(0,len(buf),4):
        r = buf[i]
        if isinstance( r, bytes ):
            r = int.from_bytes( r, byteorder='big' )
        r = ( minOutput + ( maxOutput - minOutput ) * ( min( max( ( r / 255 ) - minInput, 0.0 ) / ( maxInput - minInput ), 1.0 ) ) **  ( 1 / options['gamma'] ) ) * 255

        g = buf[i+1]
        if isinstance( g, bytes ):
            g = int.from_bytes( g, byteorder='big' )
        g = ( minOutput + ( maxOutput - minOutput ) * ( min( max( ( g / 255 ) - minInput, 0.0 ) / ( maxInput - minInput ), 1.0 ) ) **  ( 1 / options['gamma'] ) ) * 255

        b = buf[i+2]
        if isinstance( b, bytes ):
            b = int.from_bytes( b, byteorder='big' )
        b = ( minOutput + ( maxOutput - minOutput ) * ( min( max( ( b / 255 ) - minInput, 0.0 ) / ( maxInput - minInput ), 1.0 ) ) **  ( 1 / options['gamma'] ) ) * 255

        buf[i]   = struct.pack("B", int(r))
        buf[i+1] = struct.pack("B", int(g))
        buf[i+2] = struct.pack("B", int(b))

# Convert image to grayscale
# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
# ctx = cairo.Context(ims)
# bitmap.grayscale( ims )
def grayscale( surface, weighted = True ):
    buf = surface.get_data()
    for i in range(0,len(buf),4):
        r = buf[i]
        if isinstance( r, bytes ):
            r = int.from_bytes( r, byteorder='big' )
        g = buf[i+1]
        if isinstance( g, bytes ):
            g = int.from_bytes( g, byteorder='big' )
        b = buf[i+2]
        if isinstance( b, bytes ):
            b = int.from_bytes( b, byteorder='big' )

        if weighted:
            # standard luminence calculation based on the human eye's sensitivity to green
            avg = ( ( ( r * 0.299 ) + ( g * 0.587 ) + ( b * 0.114 ) ) )
        else:
            avg = ( ( r + g +b ) / 3 )
        buf[i]   = struct.pack("B", int( avg ) )
        buf[i+1] = struct.pack("B", int( avg ) )
        buf[i+2] = struct.pack("B", int( avg ) )
