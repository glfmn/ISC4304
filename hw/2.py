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
Homework 2 for ISC4304, due 25 Jan 2018
"""

import random as rng

def map_divide(xs, d):
    return [x/float(d) for x in xs]

if __name__ == '__main__':

    print "Homework 2: Gwen Lofman"

    # 1. slice the list into its two center elements
    a = [113, 117, 121, 125, 129, 133, 137, 141, 145, 149]
    print "1:", a[len(a)/2-1:len(a)/2+1]

    # 2. produce a 2D list from `a`
    print "2:", [ a[x-1:x+1] for x in xrange(1,len(a),2)]

    # 3. add a number to list `a`
    print "3:", a.append(rng.randint(0,100))

    # 4. prepend a number to list `a`
    print "4:", [rng.randint(0,100)].extend(a)

    # 5. combine two strings
    print "5:", "Gwen" + " Lofman"

    # 6. element-wise division
    print "6:", map_divide([456,45,23,89,56], 23)

    # 7. sum a list, but not using `sum(a)` because that's boring
    print "7:", reduce(lambda a,b: a+b, [113, 117, 121, 125, 129, 133, 137, 141, 145, 149])

    # 8. Produce a list of pairs (i, i-4) for i in 10..16
    print "8:", [(x, x-4) for x in xrange(10,16)]

    # 9. print an example dictionary
    print "9:", {
        'Gwen': 'Lofman',
        'Peter': 'Beerli',
        'Celine': 'Nagales',
        'Barrack': 'Obama',
        'Emmanuel': 'Collins'
    }

    # 10. show only unique numbers in the comprehension below
    print "10:", {int(x)/100 for x in range(1000)}

