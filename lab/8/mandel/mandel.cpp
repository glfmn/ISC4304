#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <complex>
#include <iostream>

namespace py = boost::python;

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

    py::list render(size_t width, size_t height, const complex &ul, const complex&lr) {
        py::list list;
        for (size_t y = 0; y < height; y++) {
            for (size_t x = 0; x < width; x++) {
                auto c = pixel_to_point(width, height, y, x, ul, lr);

                list.append(255 - mandelbrot::escapes(c, 255, 255));
            }
        }
        return list;
    }
}

BOOST_PYTHON_MODULE(mandel) {
    py::def("escapes", mandelbrot::escapes);
    py::def("render", mandelbrot::render);
}
