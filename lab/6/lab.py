#! /bin/env python
\
'''
USAGE python2 lab.py

Plots the mandelbrot set, and once the figure for the mandelbrot set is closed, plots the time for computing the mandelbrot set against the proportional number of pixels used in the computation to show that the method used has linear time complexity with respect to the number of pixels.

References:
- http://nbviewer.jupyter.org/gist/harrism/f5707335f40af9463c43
'''

import math
import numpy as np
from pylab import imshow, show
import matplotlib.pyplot as plot
from timeit import default_timer as timer

def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    # use x as real and y as imaginary part
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters


def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    # For each pixel, calculate the real part which corresponds to the x
    # coordinate, and the imaginary part which corresponds to ty y coordinate.
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            # Use the value from the mandelbrot set to determine the color
            color = mandel(real, imag, iters)
            # Save the color in the passed image buffer
            image[y, x] = color


if __name__ == '__main__':
    # Create the image buffer of size (1024x1536)
    size = (1024, 1536)
    image = np.zeros(size, dtype = np.uint8)
    # Time how long it takes to calcuate the image buffer
    start = timer()
    create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
    dt = timer() - start

    # Print the time taken an show the resulting fractal
    print "Mandelbrot created in %f s" % dt
    imshow(image)
    show()

    ts = []
    ss = []
    # calculate the time it takes to render each mandelbrot set with linearly
    # increasing number of pixels
    for p in [x/10.0 + 0.1 for x in xrange(0,10)]:
        s = (
            int(math.ceil(size[0]*math.sqrt(p))),
            int(math.ceil(size[1]*math.sqrt(p))),
        )
        ss.append(s)
        image = np.zeros(s, dtype = np.uint8)
        start = timer()
        create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
        ts.append(timer() - start)

    # Calculate the proportional ammount in pixels
    ps = [s[0]*s[1]/float(size[0]*size[1]) for s in ss]

    # Plot time complexity relative to number of pixels
    plot.plot(ps,ts)
    plot.xlabel('Proportional number of pixels')
    plot.ylabel('Computation time time (s)')
    plot.title('Time Complexity of Mandelbrot')
    plot.show()
