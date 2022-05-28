from collections import deque
import dataflow_pb2
from google.protobuf.struct_pb2 import ListValue
from graph import Graph
from component import ComponentStatus
from sample_component import Source, Sink

# graph = dataflow_pb2.dataflow()
# comp = graph.vertices.add()
# comp.name = 'source'
# comp.logical_id = 1
# comp.parallelism = 1
# comp.branches = 1

# lv = ListValue()
# for i in range(5):
# 	lv.add_list().extend(i)

# comp.child_logical_ids.extend(lv)

# user code here
graph = Graph("cpp_python_comparison")
src = Source()
tensor_queue = "tensors"
src.set_output(tensor_queue, (720,720,3), is_process_parallel=True)
sink =Sink()
sink.set_input(tensor_queue, (720,720,3), is_process_parallel=True)

graph.add_component(src)
graph.add_component(sink)
graph.add_flow(tensor_queue, src, tensor_queue, sink)


protobuf_graph = dataflow_pb2.dataflow()

# Run BFS on the graph to generate the protobuf
ready_queue = deque()
for c in graph.components:
    c._component_status = ComponentStatus.initialized

graph.components[0]._component_status = ComponentStatus.visited
ready_queue.append(graph.components[0])
while len(ready_queue) > 0 :
    comp = ready_queue.popleft()

    protobuf_comp = protobuf_graph.vertices.add()
    protobuf_comp.name = comp.name
    protobuf_comp.logical_id = comp.cid
    protobuf_comp.parallelism = 1    

    for queue_name in comp.write_queues:
        dst_q_list = graph.edges.get((queue_name, comp.name))
        protobuf_comp.branches =  len(dst_q_list)

        for dst_queue_name , dst_comp_name in dst_q_list:
            edge = protobuf_comp.edges.add()  
            edge.src_name  = comp.name            
            edge.src_queue.name = queue_name
            shape, _ = comp.output_queues[queue_name]
            edge.src_queue.shape.extend(shape)
            edge.src_queue.data_type = "float"
            ## TODO: find it in either output or state queues
            ## this will help us define the queue type
            dst_comp = graph.get_component_byname(dst_comp_name)
            edge.dst_name = dst_comp_name
            edge.dst_queue.name =  dst_queue_name
            shape, _ = dst_comp.input_queues[queue_name]
            edge.dst_queue.shape.extend(shape)
            edge.dst_queue.data_type =  "float"
            print(edge.src_queue.shape)
            print(edge.dst_queue.shape)
            
            if dst_comp.component_status == ComponentStatus.initialized and \
                dst_comp not in ready_queue:
                dst_comp.component_status = ComponentStatus.visited
                ready_queue.append(dst_comp)



    
