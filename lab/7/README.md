# Lab 7: Mandel 2

Plot the mandelbrot set using a C++ program to do the heavy lifting, passing the pixel values through stdout to the python script using the subprocess API.

## Usage

See usage information from:

```
$ python2 mandel.py --help
$ python2 mandel.py 1000 750
```

The mandelbrot set only retains the proper proportion if you keep this 4x3 aspect ratio.

## Build

Build the C++ component using make with the `-C` flag to enable building without entering the directory where the C++ project is located.

```
$ make -C mandel/
```
