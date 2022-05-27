### generate protobuf code for Python and C++

```{bash}
protoc -I=. --python_out=. dataflow.proto
protoc -I=. --cpp_out=. dataflow.proto
```

The Python code is for the input, as we'll specify the dataflow graph using python code. The C++ runtime will read the protobuf and launch threads or processes for the execution. 

