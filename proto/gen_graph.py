import dataflow_pb2
from google.protobuf.struct_pb2 import ListValue


graph = dataflow_pb2.dataflow()
comp = graph.components.add()
comp.name = 'source'
comp.logical_id = 1
comp.parallelism = 1
comp.branches = 1

lv = ListValue()
for i in range(5):
	lv.add_list().extend(i)
	
comp.child_logical_ids.extend(lv)