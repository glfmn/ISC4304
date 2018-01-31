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
fibonacci: generate fibonacci numbers and print them to the terminal.

USAGE:
    fibbonacci <N>

ARGS:
    <N> The number of fibonacci numbers to print to terminal

Print numbers of the fibonacci sequence up to the Nth element, each separated by
a single space.
"""

from __future__ import print_function
import sys

class fibonacci:
    """
    Memoized fibonacci iterator

    Using dynamic programming, create an iterator over fibonacci elements which
    has O(n) time and space complexity.
    """


    def __init__(self, start=0, stop=None):
        """
        Construct a fibonacci sequence, by default start at 0 and never end.
        """
        self.start=start
        self.stop=stop
        self.current=0
        self.fib = [0, 1]

        # initialize fibonacci sequence to the start element
        for _ in range(start):
            self.next()


    def __iter__(self):
        return self


    def next(self):
        if self.current > 1:
            self.fib.append(self.fib[self.current-1] + self.fib[self.current-2])

        self.current += 1

        if self.stop is not None:
            if self.current > self.stop:
                raise StopIteration

        return self.fib[self.current-1]


    def imperative(n):
        """
        "regular" memoized implementation of the fibonacci series

        Returns a list of the fibonacci elements up to the nth element.
        """
        fib = [0, 1]
        for i in range(0,n):
            if i > 1:
                fib.append(fib[i-1] + fib[i-2])

            i += 1

        return fib


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # print usage if things go wrong
        print(__doc__)
    else:
        # print fibonacci elements
        n = int(sys.argv[1])
        for f in fibonacci(0,n):
            print(f, end=" ")

        print("")
