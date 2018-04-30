#! /bin/env python
'''
USAGE python2 lab.py

Plot the mandelbrot set

References:
- http://nbviewer.jupyter.org/gist/harrism/f5707335f40af9463c43
'''

import math
import numpy as np
from pylab import imshow, show
import matplotlib.pyplot as plot
from timeit import default_timer as timer
import mandel

if __name__ == '__main__':
    # Create the image buffer of size (1024x1536)
    size = (1024, 1536)
    image = np.zeros(size, dtype = np.uint)
    # Time how long it takes to calcuate the image buffer
    start = timer()
    mandel.render(-2.0, 1.0, -1.0, 1.0, image, 20)
    dt = timer() - start
    print(dt)

    # Print the time taken an show the resulting fractal
    imshow(image)
    show()
