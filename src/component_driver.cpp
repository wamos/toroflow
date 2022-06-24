#include "dynamic_library.h"
#include "component_interface.h"

using namespace toroflow;

// this is a temporary main, we'll make this an actaul driver that can launch any .so later
int main(){
	std::string func_library_path_ = "libfoo.so";
	auto func_library_ = utils::DynamicLibrary::Create(func_library_path_);
	// TODO: bug is in LoadSymbol
	auto init_fn_ = func_library_->LoadSymbol<comp_init_fn_t>("comp_init");
	int ret_val = init_fn_(); 
	printf("init_fn_ returns: %d\n", ret_val);
	return 0;	
}

// this will follow closely with the worker_v1_interface.h from Nightcore!
// A component will have all these fucntions, e.g. init_fn, create_fn (faas_create_func_worker), 
// destory_fn (faas_destroy_func_worker), exec_fn (faas_func_call).
// they will be loaded as .so into the component_driver that will put it to run.  

// TODO:
// 1. Before setup and main_loop, the runtime will need to 
//	1a. parse parse protobuf to know what exactly are we launching. this will construct the dataflow graph.
//  1b. the dataflow graph is here, create queues (local not IPC) for components. 
//      these queues will become more complicated but not now. components are not created yet
//  1c. components are created with NULL ptr to their 4 methods/functions.

// TODO:
// 2. follow func_worker.h/.cpp from Nightcore and have a way simpler version of that
//
//	2a. setup: init_fn first loads all 4 functions from .so to components
//      // we don't have the complicated communication (e.g. Nightcore's engine-func_worker) 
//      // and management (config passed from launcher)
//	2b. main_loop: create threads, comp driver calls create_fn once, exec_fn n-times, and
//      destory_fn once at the end.
//      // Nightcore uses only processes to support containers but we don't care for now  
//  2c. join: the threads reach their termination condition, runtime joins these threads. 

// TODO:
// 3. OpenCL/XRT integration:
// this is partly unknown as we don't have access to FPGA devices yet
// the additional functions we needs are 
// 1. init FPGA OpenCL/XRT buffers
// 2. launch OpenCL kernels and collect results
 

// further TODO BUT NOT NOW:
// 1. when we want to support multi-process dataflow (will be a must for Python based component)
// inter process communication: we'll resue a lot from Nightcore's IPC code
// 2. DPDK networking stack for higher throghuput on data path