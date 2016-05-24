# Python Easing Functions considering only the time (t)
# t value for the range [0, 1] => [0, 1]
#
# Any speed improvement will be great aprettiated!
#
# Based in the work of many others
# http://gizma.com/easing/
# https://github.com/CharlotteGore/functional-easing
# http://joshondesign.com/2013/03/01/improvedEasingEquations
#
# Carlos Cabo (@putuko) 2015 V.1.00
# based upon https://github.com/carloscabo/eaze-js

import os
import math

def linear(t):
    return t

def lineal(t):
    return t

## In

def inQuad(t):
    return t*t

def inCubic(t):
    return t*t*t

def inQuart(t):
    return t*t*t*t

def inQuint(t):
    return t*t*t*t*t

def inCirc(t):
    return math.sqrt(1-t*t)-1

def inSine(t):
    return -1*math.cos(t*(math.pi/2))+1

## OUT

def outQuad(t):
    return t*(2-t)

def outCubic(t):
    return (--t)*t*t+1

def outQuart(t):
    return 1-(--t)*t*t*t

def outQuint(t):
    return 1+(--t)*t*t*t*t

def outCirc(t):
    return math.sqrt(1-(--t)*t)

def outSine(t):
    return math.sin(t*(math.pi/2))

## INOut
def inOutQuad(t):
    r =  (2*t*t) if (t<0.5) else -1+(4-2*t)*t
    return r

def inOutCubic(t):
    r = (4*t*t*t) if (t<0.5) else (t-1)*(2*t-2)*(2*t-2)+1
    return r

def inOutQuart(t):
    r = (8*t*t*t*t) if (t<0.5) else 1-8*(--t)*t*t*t
    return r

def inOutQuint(t):
    r = (16*t*t*t*t*t) if (t<0.5) else 1+16*(--t)*t*t*t*t
    return r

def inOutCirc(t):
    t=t/2
    return (math.sqrt(1-t*t)-1)/-2

def inOutSine(t):
    return (math.cos(math.PI*t)-1)/-2
