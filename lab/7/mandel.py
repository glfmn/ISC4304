"""Lab 7: Mandelbrot Set part 2

USAGE: mandel.py <width> <height>

Options:
    -h, --help    Show this screen
    --version     Show the version number

Print the mandelbrot set to screen using a C++ utility to generate the data
faster than a native python application can.
"""

from docopt import docopt
import numpy as np
from subprocess import Popen, PIPE
from pylab import imshow, show

if __name__ == '__main__':
    args = docopt(__doc__, version='mandel2 0.1.0')

    width = args["<width>"]
    height = args["<height>"]

    process = Popen([
        "./mandel/mandel",
        width,
        height,
        "(-1.20,0.35)",
        "(-1,0.20)",
    ], stdout=PIPE)
    (output, err) = process.communicate()

    output = output.split(' ')
    del output[-1]
    output = np.array(map(int, output)).reshape(int(height), int(width))

    imshow(output)
    show()
