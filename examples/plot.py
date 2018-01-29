#!/usr/bin/env python
#
#
# (c) Gwen Lofman MIT opensource license
#
"""
Examples of plots and combined plots using `matplotlib.pyplot` in combination
with some other modules.
"""

import matplotlib.pyplot as plt
import numpy.random as rng
import math as m
import itertools

def peek(iterator, eoi=None):
    iterator = iter(iterator)

    prev = next(iterator)

    for elm in iterator:
        yield prev, elm
        prev = elm

    yield prev, eoi

def smooth(ys):
    """Smooth histogram bins by averaging the edges"""
    return [abs(b-a)/2.0 for (a,b) in peek(iter(ys))]

if __name__ == '__main__':
    n = 1000

    # Generate random numbers of two types
    normal = rng.normal(size=n)
    uniform = rng.uniform(size=n*10)

    binvals, bins, patches = plt.hist(normal, 30, histtype='step', color='b', label='Gaussian')

    print bins
    print smooth(bins)
