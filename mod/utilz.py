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
  result = { }
  result.x = x1 + (x2 - x1) * amt
  result.y = y1 + (y2 - y1) * amt
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
