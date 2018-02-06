#!/usr/bin/env python
#
# Copyright (c) 2018 Gwen Lofman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Lab 2: Plotting

Lab from ISC4304, taught by Peter Beerli:

> The task is to construct a plot that shows the distribution of x and y in a
> contour or density plot (for example use matplotlib with hist2d) and show the
> marginal histograms of the x and y values.
"""

import math
import matplotlib.pyplot as plot
from numpy import random as rng
from numpy import histogram2d as hist2d
import numpy

if __name__ == "__main__":
    # 1. Generate 5000 random X values from a Normal distribution (numpy)
    #    - mean 10
    #    - standard deviation 20
    # 2. generate 5000 Y values from a gamma distribution (numpy)
    #    - shape a = 5
    #    - scale b = 2.

    n = 5000
    x, y = rng.normal(10, 20, n), rng.gamma(5, 2, n)

    # Generate a density histogram of the X,Y coordinates, for example with
    # hist2d

    H, xe, ye, = hist2d(x,y, math.sqrt(5000))
    X, Y = numpy.meshgrid(xe, ye)

    plot.figure(figsize=(8, 6))
    plot.subplot(2, 2, 3, title='Density histogram')
    plot.pcolormesh(X, Y, H, cmap='RdBu')
    plot.colorbar()

    # Calculate a good number of bins
    bins=int(math.sqrt(n))

    # Plot the x distribution
    plot.subplot(2, 2, 1, title='X distribution')
    plot.hist(x, bins=bins, histtype='stepfilled', normed=True, color='r')

    # Plot the y distribution
    plot.subplot(2, 2, 4, title='Y distribution')
    plot.hist(y, bins=bins, histtype='stepfilled', normed=True, color='r', orientation="horizontal")

    plot.show()
