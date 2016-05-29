import os
import math

# Calculates a number between two numbers at a specific increment.
# The amt parameter is the amount to interpolate between the two
# values where 0.0 equal to the first point, 0.1 is very near the
# first point, 0.5 is half-way in between, etc.
# The lerp function is convenient for creating motion along a
# straight path and for drawing dotted lines.
def lerp (value1, value2, amt):
  return value1 + (value2 - value1) * amt

# Same with a line (x, y)
def lineLerp (x1, y1, x2, y2, amt):
  result = { 'x': None, 'y': None }
  result['x'] = x1 + (x2 - x1) * amt
  result['y'] = y1 + (y2 - y1) * amt
  return result

# Interpolates between 2 angles, from 0 to 360 degrees
def angleLerp(ang1, ang2, percent):
    ret = 0
    diff = math.fabs(ang2 - ang1)
    if (diff > 180):
        if (ang2 > ang1):
            ang1 += 360
        else:
            ang2 += 360
    # Interpolacion
    ret = (ang1 + ((ang2 - ang1) * percent))
    if (ret < 0) or (ret > 360):
        ret = ret % 360
    return ret

# Interpolates HSL color
def hslLerp(hsl1, hsl2, percent):
    h1 = hsl1[0]
    s1 = hsl1[1]
    l1 = hsl1[2]
    h2 = hsl2[0]
    s2 = hsl2[1]
    l2 = hsl2[2]
    result = []

    diff = math.fabs(h2 - h1)
    if (diff > 0.5):
        if (h2 > h1):
            h1 += 0.5
        else:
            h2 += 0.5
    # Interpolacion
    h_final = (h1 + ((h2 - h1) * percent))
    if (h_final < 0) or (h_final > 1.0):
        h_final = h_final % 1.0

    result.append( h_final )
    result.append( lerp(s1, s2, percent) )
    result.append( lerp(l1, l2, percent) )

    return result

# Returns angle in radians between 2 points
def angleTo (x1, y1, x2, y2):
  return math.atan2( y2 - y1, x2 - x1 )

# Rotates a point px, py from a pivot (center) in cx, cy
# Rotation must be in radians
def rotatePoint (cx, cy, px, py, rad):
    cos = math.cos(rad)
    sin = math.sin(rad)
    nx = (cos * (px - cx)) + (sin * (py - cy)) + cx
    ny = (cos * (py - cy)) - (sin * (px - cx)) + cy
    return [nx, ny]

# Distance between 2 2D points (x1, y1), (x2, y2)
def distance (x1, y1, x2, y2):
    return math.hypot( x2 - x1, y2 - y1 )
