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

import random

def one():
    """All odd integers between 22 and 0"""
    print [x for x in xrange(1,22) if x % 2 == 1]

def two(n):
    """Output the squares of the numbers from n..0 taking steps of -1"""
    print [x**2 for x in xrange(n,0,-1)]

def three():
    """print 10 random integers in the range [3, 8)"""
    print [random.randint(3,7) for _ in xrange(10)]

def four(dx,dy):
    """print nested lists of ordered pairs which represent their row and column"""
    print [[(x+1,y+1) for x in xrange(dx)] for y in xrange(dy)]

if __name__ == '__main__':
    print 'one:  ',
    one()
    print 'two:  ',
    two(100)
    print 'three:',
    three()
    print 'four: ',
    four(3,3)
