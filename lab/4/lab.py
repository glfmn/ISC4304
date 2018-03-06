#!/usr/bin/python
# -*- coding: utf-8

from itertools import chain

def hilbert(origin, xb, yb, n):
    """
    H = hilbert(origin, xb, yb, n) where
    INPUT
        origin - the start of the hilbert curve
        xb     - x-basis vector of the hilbert curve, a tuple or array of len 2
        yb     - y-basis vector of the hilbert curve, a tuple or array of len 2
        n      - the recursion depth of the hilbert curve
    OUTPUT
        H      - a list of typles which are points on the hilbert curve
    """
    if n <= 0:
        # Calculate the actual point on the hilbert curve
        return (origin[0] + (xb[0] + yb[0])/2, origin[1] + (xb[1] + yb[1])/2)
    else:
        # Unpack the values to prevent reading them multiple times
        x,y   = origin
        xi,xj = xb
        yi,yj = yb
        # Recursively build list of hilbert points
        points = [
            hilbert((x,           y          ), ( yi/2, yj/2), ( xi/2,  xj/2), n-1),
            hilbert((x+xi/2,      y+xj/2     ), ( xi/2, xj/2), ( yi/2,  yj/2), n-1),
            hilbert((x+xi/2+yi/2, y+xj/2+yj/2), ( xi/2, xj/2), ( yi/2,  yj/2), n-1),
            hilbert((x+xi/2+yi,   y+xj/2+yj  ), (-yi/2,-yj/2), (-xi/2, -xj/2), n-1),
        ]
        # We don't want to break the tuples of points, don't flatten the tuples
        if n > 1:
            # Flatten iterables of arbitrary depth into a single list, but only
            # when one step above the actual points to prevent unpacking tuples
            points = list(chain.from_iterable(points))
        return points

if __name__ == '__main__':
    H = hilbert((0.0, 0.0), (1.0, 0.0), (0.0, 1.0), 4)

    print(H)
