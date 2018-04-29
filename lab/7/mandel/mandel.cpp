/// Write the Mandelbrot Set to a portable pixmap (PPM) image

#include <cassert>
#include <complex>
#include <fstream>
#include <iostream>
#include <sstream>
#include <utility>
#include <vector>


namespace mandelbrot {
    typedef std::complex<double> complex;

    unsigned char escapes(const complex &c, const unsigned &limit, const unsigned empty) {
        auto z = complex{0, 0};
        for (unsigned i = 0; i < limit; i++) {
            z = z*z + c;
            if (z.real()*z.real() + z.imag()*z.imag() >= 4) {
                return i;
            }
        }
        return empty;
    }
}


inline std::complex<double> pixel_to_point(
    size_t width, size_t height,
    size_t x, size_t y,
    std::complex<double> upper_left,
    std::complex<double> lower_right
) {
    double range_x = lower_right.real() - upper_left.real();
    double range_y = upper_left.imag() - lower_right.imag();
    return std::complex<double>{
        upper_left.real() + double(x) * range_x / double(width),
        upper_left.imag() - double(y) * range_y / double(height)
    };
}


int main(int argc, char* argv[]) {
    if (argc < 5) {
        std::cerr
            << "Usage: " << argv[0]
            << " <file> <width> <height> <upper-left> <lower-right>\n"
            << "\nARGS:\n"
            << "    width        the number of pixels wide to make the image\n"
            << "    height       the number of pixels tall to make the image\n"
            << "    upper-left   complex number (REAL,IMAG) to map to the upper-right corner\n"
            << "    lower-right  complex number (REAL,IMAG) to map to the lower-left corner"
            << std::endl;
        return 1;
    }

    long int width = atol(argv[1]);
    long int height = atol(argv[2]);
    std::complex<double> ul;
    std::complex<double> lr;

    std::stringstream(argv[3]) >> ul;
    std::stringstream(argv[4]) >> lr;

    for (size_t y = 0; y < height; y++) {
        for (size_t x = 0; x < width; x++) {
            auto c = pixel_to_point(width, height, y, x, ul, lr);

            std::cout << 255 - mandelbrot::escapes(c, 255, 255) << ' ';
        }
    }

    return 0;
}
