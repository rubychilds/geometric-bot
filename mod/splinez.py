# Curve calc function for canvas 2.3.1
# Epistemex (c) 2013-2014
# License: MIT
#
# Port to python3 by carloscabo (all the mistakes are my fault ;)
#
# Calculates an array containing points representing a cardinal spline through given point array.
# Points must be arranged as: [x1, y1, x2, y2, ..., xn, yn].
#
# The points for the cardinal spline are returned as a new array.
#
# @param {Array} points - point array
# @param {Number} [tension=0.5] - tension. Typically between [0.0, 1.0] but can be exceeded
# @param {Number} [numOfSeg=20] - number of segments between two points (line resolution)
# @param {Boolean} [close=False] - Close the ends making the line continuous
# @returns {Array of floats} New array with the calculated points that was added to the path

def getCurvePoints( points, tension = 0.5, numOfSeg = 25, close = False ):
    i = 1
    l = len(points)
    rPos =  0
    rLen =  (l-2) * numOfSeg + 2 + ( numOfSeg * 2 if close else 0 )
    res =   [0.0] * rLen
    cache = [0.0] * ( (numOfSeg + 2) * 4 )
    cachePtr = 4

    pts = points[:] # for cloning point array

    if close:
        pts.insert( 0, points[l - 1] ) # insert end point as first point
        pts.insert( 0, points[l - 2] )
        pts.append( points[0] ) # first point as last point
        pts.append( points[1] )
    else:
        pts.insert( 0, points[1] ) # copy 1. point and insert at beginning
        pts.insert( 0, points[0] )
        pts.append( points[l - 2] ) # duplicate end-points
        pts.append( points[l - 1] )

    # cache inner-loop calculations as they are based on t alone
    cache[0] = 1 # 1,0,0,0

    for i in range( 1, numOfSeg ):
        st = i / numOfSeg
        st2 = st * st
        st3 = st2 * st
        st23 = st3 * 2
        st32 = st2 * 3

        cache[cachePtr] = st23 - st32 + 1    # c1
        cachePtr += 1
        cache[cachePtr] = st32 - st23        # c2
        cachePtr += 1
        cache[cachePtr] = st3 - 2 * st2 + st # c3
        cachePtr += 1
        cache[cachePtr] = st3 - st2          # c4
        cachePtr += 1

    cachePtr += 1
    cache[cachePtr] = 1 # 0,1,0,0

    def parse(pts, cache, l):
        nonlocal rPos, res
        for i in range( 2, l, 2 ):
            pt1 = pts[i]
            pt2 = pts[i+1]
            pt3 = pts[i+2]
            pt4 = pts[i+3]

            t1x = (pt3 - pts[i-2]) * tension
            t1y = (pt4 - pts[i-1]) * tension
            t2x = (pts[i+4] - pt1) * tension
            t2y = (pts[i+5] - pt2) * tension

            for t in range( 0, numOfSeg ):
                c = t * 4

                c1 = cache[c]
                c2 = cache[c+1]
                c3 = cache[c+2]
                c4 = cache[c+3]

                res[rPos] = c1 * pt1 + c2 * pt3 + c3 * t1x + c4 * t2x
                rPos += 1
                res[rPos] = c1 * pt2 + c2 * pt4 + c3 * t1y + c4 * t2y
                rPos += 1

    # calc. points
    parse(pts, cache, l)

    if close:
        pts = []
        pts.append( points[l - 4] ) # second last and last
        pts.append( points[l - 3] )
        pts.append( points[l - 2] )
        pts.append( points[l - 1] )

        pts.append( points[0] )  # first and second
        pts.append( points[1] )
        pts.append( points[2] )
        pts.append( points[3] )

        parse(pts, cache, 4)

    # add last point
    l = 0 if close else len(points) - 2
    res[rPos] = points[l]
    rPos += 1
    res[rPos] = points[l+1]

    return res
