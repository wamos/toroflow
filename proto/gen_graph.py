import dataflow_pb2
from google.protobuf.struct_pb2 import ListValue
from .graph import Graph
from .component import Component
from .sample_component import Source, Sink


# graph = dataflow_pb2.dataflow()
# comp = graph.components.add()
# comp.name = 'source'
# comp.logical_id = 1
# comp.parallelism = 1
# comp.branches = 1

# lv = ListValue()
# for i in range(5):
# 	lv.add_list().extend(i)

# comp.child_logical_ids.extend(lv)

bench = Graph("cpp_python_comparison")
src = Source()
tensor_queue = "tensors"
src.set_output(tensor_queue, (720,720,3), is_process_parallel=True)

sink =Sink()
sink.set_input(tensor_queue, (720,720,3), is_process_parallel=True)

bench.add_component(src)
bench.add_component(sink)

bench.add_flow(tensor_queue, src, tensor_queue, sink)


graph = dataflow_pb2.dataflow()


# Run BFS on the graph to generate the protobuf
# comp = graph.components.add()
# comp.name = c.name
# comp.logical_id = c.cid
# comp.parallelism = 1 # as default
# comp.branches = 1
    
