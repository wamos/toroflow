#include "component_interface.h"
#include <stdio.h>


// we'll need this "extern "C" {}"" to avoid C++ name-mangling
// so the driver code can call comp_init() instead of whatever 
// namae C++ has messed up, e.g. _Z9comp_initv.
#ifdef __cplusplus
extern "C" {
#endif  // __cplusplus

API_EXPORT int comp_init(){
	printf("foo init is called\n");
	return 1;
}

#ifdef __cplusplus
}
#endif  // __cplusplus