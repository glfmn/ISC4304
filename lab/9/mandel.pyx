cimport cython
import numpy as np
cimport numpy as np


cdef int escape(double x, double y, int max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    # use x as real and y as imaginary part
    cdef np.complex128_t c = np.complex(x, y)
    cdef np.complex128_t z = 0.0j
    cdef int i
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters


@cython.boundscheck(False)
@cython.wraparound(False)
def render(
        double min_x,
        double max_x,
        double min_y,
        double max_y,
        np.ndarray[np.uint_t, ndim=2] image,
        int iters
    ):
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]

    cdef double pixel_size_x = (max_x - min_x) / float(width)
    cdef double pixel_size_y = (max_y - min_y) / float(height)

    # For each pixel, calculate the real part which corresponds to the x
    # coordinate, and the imaginary part which corresponds to ty y coordinate.
    cdef int x, y
    cdef double real, imag
    for x in range(width):
        real= min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            # Use the value from the mandelbrot set to determine the color
            # Save the color in the passed image buffer
            image[y, x] = escape(real, imag, iters)
