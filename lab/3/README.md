# Conway's Game of Life

Cellular automata using Conway's Game of Life; a simple command-line utility to spawn and watch life play out it's course.

# Usage

```
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
```
