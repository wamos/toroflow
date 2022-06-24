#pragma once

#include "macro.h"
#include <iostream>
#include <memory>
#include <dlfcn.h>

namespace toroflow {
namespace utils {

class DynamicLibrary {
public:
    ~DynamicLibrary() {
        if (dlclose(handle_) != 0) {
            std::cout << "Failed to close dynamic library: " << dlerror() << "\n";
        }
    }

    static std::unique_ptr<DynamicLibrary> Create(std::string_view path) {
		// std::cout << std::string(path).c_str() << "\n";
        void* handle = dlopen(std::string(path).c_str(), RTLD_LAZY);
        if (handle == nullptr) {
            std::cout << "Failed to open dynamic library " << path << ": " << dlerror() << "\n";
        }
        DynamicLibrary* dynamic_library = new DynamicLibrary(handle);
        return std::unique_ptr<DynamicLibrary>(dynamic_library);
    }

    template<class T>
    T LoadSymbol(std::string_view name) {
		// std::cout << std::string(name).c_str() << "\n";
        void* ptr = dlsym(handle_, std::string(name).c_str());
		// BUG: we saw this, why?  
        if (ptr == nullptr) {
            std::cout << "Cannot load symbol " << name << " from the dynamic library" << "\n";
			std::cout << "dlerror:" << dlerror() << "\n";
        }
        return reinterpret_cast<T>(ptr);
    }

private:
    void* handle_;
    explicit DynamicLibrary(void* handle): handle_(handle) {}
    DISALLOW_COPY_AND_ASSIGN(DynamicLibrary);
};

}  // namespace utils
}  // namespace toroflow
