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
middlesquare: generate 100 random numbers with the von Neumann generator

USAGE:
    middelsquare [N] [SEED]

ARGS:
    [N] The number random numbers to generate, [default 100]
    [SEED] a 6 digit number with no zeros to start the sequence [default 123456]

Print out 100 random "Von Neumann" numbers, or the desired number of numbers,

Von Neumann generators are terrible for most random number purposes, this is just
a toy example.
"""

from __future__ import print_function
import sys

class VonNeumann:
    """
    von Neumann generator for random numbers
    """

    def __init__(self, seed, stop=None):
        """
        Construct a von Neumann random number sequence, which never ends
        """
        self.state = int(seed)
        self.stop = int(stop)
        self.current = 0


    def __iter__(self):
        return self

    def next(self):
        """
        The next von Neumann pseudo-random number
        """

        # Take the square of our state and convert to a string
        n = str(self.state**2)

        # take the midpoint, grab the middle six digits, and convert back to int
        mid = int(len(n)/2)
        self.state = int(n[mid-3:mid+3])

        # If we have specified an end and have passed it, stop
        if self.stop is not None:
            if self.current > self.stop:
                raise StopIteration

        self.current += 1

        return self.state


if __name__ == '__main__':
    if len(sys.argv) > 3 or (len(sys.argv) > 1 and sys.argv[1] in {'-h', '--help'}):
        # print usage if things go wrong or if help is requested
        print(__doc__)
    else:
        # Handle default arguments
        if len(sys.argv) < 2:
            n = 100
        else:
            n = int(sys.argv[1])
        if len(sys.argv) < 3:
            seed = 123456
        else:
            seed = int(sys.argv[2])

        # print random numbers
        for f in VonNeumann(seed, n):
            print(f, end=" ")

        print("")
