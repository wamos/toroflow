CFLAGS+=-g -Wall -std=c++17
SO_CFLAGS=-fvisibility=hidden
# See https://github.com/rolsen/demo_symbol_visibility
# for the reason of using -fvisibility=hidden

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	FINAL_EXE_LDFLAGS+=-Wl,-rpath=.
endif

all: test

# -L is the path to the directories containing the libraries. A search path for libraries.
# -l is the name of the library you want to link to.
test: component_driver.cpp libfoo.so
	g++ $(CFLAGS) $(FINAL_EXE_LDFLAGS) -o comp component_driver.cpp -L. -lfoo -ldl

libfoo.so: foo.o
	g++ -o libfoo.so -shared foo.o
foo.o: foo.cpp component_interface.h
	g++ $(CFLAGS) $(SO_CFLAGS) -o foo.o -c -fPIC foo.cpp

clean:
	rm -f comp foo.so *.o