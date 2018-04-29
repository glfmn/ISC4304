# Lab 8: Mandel 3

Plot the mandelbrot set using a C++ program to do the heavy lifting, passing the pixel values through stdout to the python script using the subprocess API.

## Usage

See usage information from:

```
$ python2 mandel.py --help
$ python2 mandel.py 1000 750 '(-1.20+0.35j)' '(-1+0.2j)'
```

The mandelbrot set only retains the proper proportion if you keep this 4x3 aspect ratio.

## Build

Build the C++ component using make with the `-C` flag to enable building without entering the directory where the C++ project is located and then copy the library to the root directory for the lab.

```
$ make -C mandel/
$ cp mandel/mandel.so .
```
