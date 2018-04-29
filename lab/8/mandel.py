"""Lab 7: Mandelbrot Set part 2

USAGE: mandel.py <width> <height> <upper-left> <lower-right>

Options:
    -h, --help    Show this screen
    --version     Show the version number

Print the mandelbrot set to screen using a C++ utility to generate the data
faster than a native python application can.
"""

from docopt import docopt
import numpy as np
from pylab import imshow, show
import time
import mandel


def pixel_to_point(width, height, x, y, ul, lr):
    range_x = lr.real - ul.real
    range_y = ul.imag - lr.imag
    return complex(
        ul.real + float(x) * range_x / float(width),
        ul.imag - float(y) * range_y / float(height)
    )


if __name__ == '__main__':
    args = docopt(__doc__, version='mandel2 0.1.0')

    width = int(args["<width>"])
    height = int(args["<height>"])
    upper_left = complex(args["<upper-left>"])
    lower_right = complex(args["<lower-right>"])

    #
    start = time.time()

    image = np.zeros((height, width), dtype=np.int16)
    for y in xrange(0, height):
        for x in xrange(0, width):
            z = pixel_to_point(width, height, y, x, upper_left, lower_right)
            image[y,x] = 255 - mandel.escapes(z, 255, 255)

    end = time.time()
    elapsed = end - start
    print "C++ inner parts: ", elapsed


    imshow(image)
    show()

    del image

    #
    start = time.time()

    image = np.array(
        mandel.render(width, height, upper_left, lower_right)
    ).reshape(height, width)

    end = time.time()
    elapsed = end - start
    print "C++ for loop:    ", elapsed

    imshow(image)
    show()
