from collections import deque
import dataflow_pb2
from google.protobuf.struct_pb2 import ListValue
from graph import Graph
from component import ComponentStatus
from sample_component import Source, Sink

# user code here
graph = Graph("cpp_python_comparison")
src = Source()
tensor_queue = "tensors"
src.set_output(tensor_queue, (720,720,3), is_process_parallel=True)
sink = Sink()
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
            # https://stackoverflow.com/questions/18376190/attributeerror-assignment-not-allowed-to-composite-field-task-in-protocol-mes
            # https://developers.google.com/protocol-buffers/docs/reference/python-generated#embedded_message            
            # we need to assign directly to edge.src_queue.name
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
            # print(edge.src_queue.shape)
            # print(edge.dst_queue.shape)
            # print(edge)
            
            if dst_comp.component_status == ComponentStatus.initialized and \
                dst_comp not in ready_queue:
                dst_comp.component_status = ComponentStatus.visited
                ready_queue.append(dst_comp)
    print(protobuf_comp)
    f = open("test_graph.protobuf", "wb")
    f.write(protobuf_comp.SerializeToString())
    f.close()

    
