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

def inBack(t, overshoot = 1.70158):
    return 1*t*t*((overshoot+1)*t-overshoot)

def inBounce(t):
    return 1 - outBounce(1-t)

def inElastic (t, amplitude = 1.0, period = 0.3):
    if (t == 0) or (t == 1): return t
    if (amplitude == 1.0):
        offset = period / 4
    else:
        offset = period/(math.pi*2.0)*math.asin(1/amplitude)
    t=t-1
    return -(amplitude*math.pow(2,10*t)*math.sin(((t-offset)*(math.pi*2))/period))

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

def outBack(t, overshoot = 1.70158):
    t = t - 1
    return t*t*((overshoot+1)*t+overshoot)+1

def outBounce(t):
    if t < 0.36363636363636365:
        return 7.5625*t*t
    elif t < 0.7272727272727273:
        t = t - 0.5454545454545454
        return 7.5625*t*t+0.75
    elif t < 0.9090909090909091:
        t = t - 0.8181818181818182
        return 7.5625*t*t+0.9375
    else:
        t = t - 0.9545454545454546
        return 7.5625*t*t+0.984375

def outElastic(t, amplitude = 1.0, period = 0.3):
    # escape early for 0 and 1
    if (t == 0.0) or (t == 1.0):
        return t
    if amplitude == 1.0:
        offset = period / 4
    else:
        offset = period/(math.pi*2.0)*math.asin(1/amplitude)
    return amplitude*math.pow(2,-10*t)*math.sin((t-offset)*(math.pi*2)/period)+1

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
    return (math.cos(math.pi*t)-1)/-2

def inOutBack(t, overshoot = 1.70158):
    t = t / 2;
    overshoot = overshoot * 1.525
    return (t * t * ((overshoot + 1) * t - overshoot)) / 2

def inOutBounce(t):
    if t < 0.5:
        return inBounce(t*2)*0.5
    else:
        return outBounce(t*2-1)*0.5+1* 0.5

def inOutElastic(t, amplitude = 1.0, period = 0.44999999999999996):
    t = (t/2)-1
    # escape early for 0 and 1
    if (t == 0.0) or (t == 1.0):
        return t
    if amplitude == 1.0:
        offset = period/4
    else:
        offset = period/(math.pi*2.0)*math.asin(1/amplitude)

    return (amplitude*math.pow(2,10*t)*math.sin((t-offset)*(math.pi*2)/period))/-2
