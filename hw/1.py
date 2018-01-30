#!/usr/bin/env python
"""
Homework 1
"""

from random import random

def one():
    print([2*x if 2*x != 14 else 16 for x in range(1,8)])

def two():
    print([x for x in range(201,151,-10)])

def three():
    print("hello" + " world")

def four():
    xs = [random() for _ in range(10)]
    print xs," sum ",sum(xs)

def five(n):
    print sum([1./k for k in xrange(1,n)])

if __name__ == "__main__":
    one()
    two()
    three()
    four()
    five(10)
    five(100)
    five(1000)
