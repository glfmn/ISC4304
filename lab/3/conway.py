#!/usr/bin/python
# -*- coding: utf-8

"""
conway [LIFE] [OPTIONS]

LIFE:
    --glider,      place a glider in a random spot
    --gosper,      place a gosper glider gun in a random spot
    --tumbler,     place a tumbler in a random spot
    --coe-ship,    place a coe-ship in a random spot
    --spider,      place a spider ship in a random spot
    --random,      place random cells of life
    --c-heptonimo, place a c-heptonimo methusula in a random spot

OPTIONS:
    --help, -h,    show this message

Conway's Game of Life

Create life from Conway's Game of life, either spawning random life if no
arguments specified, or spawning the specified life.

Example:
   $ conway --glider --glider --gosper --tumbler
"""

from array import array
import os
from random import randint, random
import sys
import time

class Grid:
    def __init__(self, x, y, init=0):
        self.dims = (x,y)
        self._grid = array('H', [int(init) for _ in xrange(x*y)])

    def __iter__(self):
        return self._grid.__iter__()

    def _calculate_index(self, key):
        x,y = key
        return x + y*self.dims[0]

    def _in_range(self, x, y):
        return self.dims[0] > x and x >= 0 and self.dims[1] > y and y >= 0

    def __getitem__(self, key):
        """
        Retrieve a cell from the grid

        Cells outside of the grid boundary are always 0, making it dead space
        """
        if len(key) != 2:
            raise TypeError()

        x,y = key

        # Flatten the periodic index into the array by returning 0 out of bounds
        if self._in_range(x,y):
            return self._grid[self._calculate_index(key)]
        else:
            return 0

    def __setitem__(self, key, value):
        x,y = key
        if self._in_range(x,y):
            self._grid[self._calculate_index(key)] = value

    def __len__(self):
        return len(self._grid)

class Conway:
    def __init__(self, dimensions):
        x,y = dimensions
        self.grid = Grid(x,y)
        self.buffer = Grid(x,y)

    def __setitem__(self, key, value):
        self.grid[key] = 1 if not (value == 0) else 0

    def __getitem__(self, key):
        return self.grid[key]

    def __format__(self, spec):
        "Draw the grid"
        spec = spec
        dx,dy = self.grid.dims
        alive = spec[0] if len(spec) >= 1 else 'X'
        dead = spec[1] if len(spec) >= 2 else ' '
        lines = []
        for y in xrange(dy):
            line = ''
            for x in xrange(dx):
                line += alive if self.is_alive(x,y) else dead
            lines.append(line)

        return "\n".join(lines)

    def is_alive(self, x, y):
        return not (self.grid[(x, y)] == 0)

    def neighbors(self, position):
        """
        Count neighbors of the given cell
        """
        (x, y) = position
        # Cell positions which correspond to the cells around the current cell
        positions = [
            (x-1,y-1), (x,y-1), (x+1,y-1),
            (x-1,y),            (x+1,y),
            (x-1,y+1), (x,y+1), (x+1,y+1),
        ]
        return sum([self.grid[pos] for pos in positions])

    def advance(self):
        """
        Advance the simulation one generation
        """
        dx,dy = self.grid.dims
        for cell in [(x,y) for y in xrange(dy) for x in xrange(dx)]:
            ns = self.neighbors(cell)
            alive = self.is_alive(cell[0], cell[1])

            # Set the corresponding cell in the buffer to the new alive or dead
            # state
            if alive and (ns == 3 or ns == 2):
                self.buffer[cell] = 1
            elif not alive and ns == 3:
                self.buffer[cell] = 1
            else:
                self.buffer[cell] = 0
        print '\n\n\n'

        # Perform buffer swap
        self.grid, self.buffer = self.buffer, self.grid
        return self.grid

    def set_region(self, ps):
        for p in ps:
            self.grid[p] = 1

def glider(x,y):
    direction = randint(0,3)
    print direction
    if direction == 0:
        return [(x, y), (x, y+1), (x, y+2), (x-1, y), (x-2, y+1)]
    elif direction == 1:
        return [(x, y), (x+1, y), (x+2, y), (x, y-1), (x+1, y-2)]
    elif direction == 2:
        return [(x, y), (x+1, y), (x+2, y), (x, y+1), (x+1, y+2)]
    else:
        return [(x, y), (x+1, y), (x+2, y), (x+2, y-1), (x+1, y-2)]

def gosper(x,y):
    return [
        (x+23,y-4),
        (x+21,y-3), (x+23,y-3),
        (x+11,y-2), (x+12,y-2), (x+19,y-2), (x+20,y-2), (x+33,y-2), (x+34,y-2),
        (x+10,y-1), (x+14,y-1), (x+19,y-1), (x+20,y-1), (x+33,y-1), (x+34,y-1),
        (x-1, y), (x, y), (x+9,y), (x+15,y), (x+19,y), (x+20,y),
        (x-1, y+1), (x, y+1), (x+9,y+1), (x+13,y+1), (x+15,y+1), (x+16,y+1), (x+21,y+1), (x+23,y+1),
        (x+9,y+2), (x+15,y+2), (x+23,y+2),
        (x+10,y+3), (x+14,y+3),
        (x+11,y+4), (x+12,y+4),
    ]

def from_specifier(spec, origin):
    """
    Use a string to deine life rather than writing out positions manually
    """
    region = []
    for y,line in enumerate(spec.split('\n')):
        for x,char in enumerate(line):
            if char == '0':
                region.append((origin[0]+x, (origin[1]+y)))

    return region

SPIDER = """
..00.....00.....00.....00...
0...0...0..0...0..0...0...0.
0...0.0.000.....000.0.0...0.
0.....00..000.000..00.....0.
00.000...............000.00.
0.........................0.
.0...0...............0...0..
..0..0...............0..0...
"""

TUMBLER = """
0.....0.
.00.00..
..0.0...
0.....0.
000.000.
"""

COE_SHIP = """
....000000
..00.....0
00.0.....0
....0...0
......0
......00
.....0000
.....00.00
.......00
"""

C_HEPTOMINO = """
.000
000
 0
"""

if __name__ == '__main__':
    height, width = os.popen('stty size', 'r').read().split()
    height, width = int(height)-5, int(width)-2
    game = Conway((width,height))

    if '-h' in sys.argv or '--help' in sys.argv:
        print __doc__
        sys.exit()

    if len(sys.argv) <= 1:
        region = [
            glider(randint(0,width-1),randint(0,height-1)),
            glider(randint(0,width-1),randint(0,height-1)),
            glider(randint(0,width-1),randint(0,height-1)),
            gosper(randint(0,width-35),randint(0,height-1)),
            from_specifier(SPIDER, (randint(0,width-10),randint(5,height-1))),
            from_specifier(TUMBLER, (randint(0,width-1),randint(0,height-1))),
            from_specifier(COE_SHIP, (randint(0,width-1),randint(0,height-1))),
            from_specifier(C_HEPTOMINO, (randint(0,width-1),randint(0,height-1))),
            [(randint(0,width),randint(0,height)) for _ in range(randint(0,width*height))]
        ]

        for r in region:
            if random() < 0.2:
                game.set_region(r)
    else:
        args = ' '.join(sys.argv)
        for _ in xrange(args.count('--glider')):
            game.set_region(glider(randint(0,width-1),randint(0,height-1)))

        args = ' '.join(sys.argv)
        for _ in xrange(args.count('--gosper')):
            game.set_region(gosper(randint(0,width-1),randint(0,height-1)))

        for _ in xrange(args.count('--spider')):
            pos = (randint(0,width-10),randint(5,height-1))
            game.set_region(from_specifier(SPIDER, pos))

        for _ in xrange(args.count('--tumbler')):
            pos = (randint(0,width-10),randint(5,height-1))
            game.set_region(from_specifier(TUMBLER, pos))

        for _ in xrange(args.count('--coe-ship')):
            pos = (randint(0,width-10),randint(5,height-1))
            game.set_region(from_specifier(COE_SHIP, pos))

        for _ in xrange(args.count('--c-heptomino')):
            pos = (randint(0,width-10),randint(5,height-1))
            game.set_region(from_specifier(C_HEPTOMINO, pos))

        for _ in xrange(args.count('--random')):
            game.set_region([(randint(0,width),randint(0,height)) for _ in range(randint(0,width*height))])


    os.system('clear')
    while sum(game.grid._grid) > 0:
        print u"{:$.}".format(game)
        game.advance()
        time.sleep(0.075)
        os.system('clear')
    else:
        print u"{:$}".format(game)
