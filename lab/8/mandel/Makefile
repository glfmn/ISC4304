# location of the Python header files
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

# location of the Boost Python include files and library
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib

# compile
TARGET = mandel

CPPFLAGS=-O3 --std=c++11

all: $(TARGET).so

# compile
$(TARGET).so: $(TARGET).o
	$(CXX) -shared -Wl,--export-dynamic \
	$^ -lpython$(PYTHON_VERSION) -lboost_python -o $@

$(TARGET).o: $(TARGET).cpp
	$(CXX) $(CFLAGS) $(CPPFLAGS) -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c $^ -o $@

clean:
	rm $(TARGET).o $(TARGET).so
