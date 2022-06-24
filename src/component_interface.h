#ifndef COMP_INTERFACE_H_
#define COMP_INTERFACE_H_

#define API_EXPORT __attribute__ ((visibility ("default")))

// n
#ifdef __cplusplus
extern "C" {
#endif  // __cplusplus

API_EXPORT int comp_init();
typedef decltype(comp_init)* comp_init_fn_t;

#ifdef __cplusplus
}
#endif  // __cplusplus

#endif  // COMP_INTERFACE_H_