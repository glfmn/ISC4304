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
Write very short python fragments to do the following:

- Print a list of all odd numbers from 1 to 21 using two lines (1 line list comprehension, one line "print")
- Print a list of square numbers from the largest to the smallest (start with x2 = 100)
- Print a list of 10 random integer numbers drawn from a uniform distribution [3, 8), (a) show the result, (b) get all unique numbers from your list.
- Generate a 2D grid of where each element is the tupel of the row and column, print the result
"""

import random

def one():
    print [x for x in xrange(1,22) if x % 2 == 1]

def two():
    print [x**2 for x in xrange(100,0,-1)]

def three():
    print [random.randint(3,7) for _ in xrange(10)]

def four(dx,dy):
    print [[(x+1,y+1) for x in xrange(dx)] for y in xrange(dy)]

if __name__ == '__main__':
    one()
    two()
    three()
    four(3,3)
