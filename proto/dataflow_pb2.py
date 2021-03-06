# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataflow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64\x61taflow.proto\x12\x08toroflow\"d\n\tDataQueue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\nqueue_type\x18\x02 \x01(\x0e\x32\x13.toroflow.QueueType\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\r\n\x05shape\x18\x04 \x03(\r\"z\n\x04\x45\x64ge\x12\x10\n\x08src_name\x18\x01 \x01(\t\x12&\n\tsrc_queue\x18\x02 \x01(\x0b\x32\x13.toroflow.DataQueue\x12\x10\n\x08\x64st_name\x18\x03 \x01(\t\x12&\n\tdst_queue\x18\x04 \x01(\x0b\x32\x13.toroflow.DataQueue\"\x87\x02\n\x06Vertex\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nlogical_id\x18\x02 \x01(\r\x12\x13\n\x0bparallelism\x18\x03 \x01(\r\x12\x10\n\x08\x62ranches\x18\x04 \x01(\r\x12\x1d\n\x05\x65\x64ges\x18\x05 \x03(\x0b\x32\x0e.toroflow.Edge\x12\x16\n\x0eis_accelerated\x18\x06 \x01(\x08\x12\x12\n\naccel_impl\x18\x07 \x01(\t\x12\x13\n\x0btarget_impl\x18\x08 \x01(\t\x12\x15\n\rcpp_impl_file\x18\t \x01(\t\x12\x13\n\x0b\x63pp_impl_fn\x18\n \x01(\t\x12\x14\n\x0cpy_impl_file\x18\x0b \x01(\t\x12\x12\n\npy_impl_fn\x18\x0c \x01(\t\".\n\x08\x64\x61taflow\x12\"\n\x08vertices\x18\x01 \x03(\x0b\x32\x10.toroflow.Vertex*:\n\tQueueType\x12\t\n\x05input\x10\x00\x12\n\n\x06output\x10\x01\x12\t\n\x05state\x10\x02\x12\x0b\n\x07special\x10\x03\x62\x06proto3')

_QUEUETYPE = DESCRIPTOR.enum_types_by_name['QueueType']
QueueType = enum_type_wrapper.EnumTypeWrapper(_QUEUETYPE)
input = 0
output = 1
state = 2
special = 3


_DATAQUEUE = DESCRIPTOR.message_types_by_name['DataQueue']
_EDGE = DESCRIPTOR.message_types_by_name['Edge']
_VERTEX = DESCRIPTOR.message_types_by_name['Vertex']
_DATAFLOW = DESCRIPTOR.message_types_by_name['dataflow']
DataQueue = _reflection.GeneratedProtocolMessageType('DataQueue', (_message.Message,), {
  'DESCRIPTOR' : _DATAQUEUE,
  '__module__' : 'dataflow_pb2'
  # @@protoc_insertion_point(class_scope:toroflow.DataQueue)
  })
_sym_db.RegisterMessage(DataQueue)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {
  'DESCRIPTOR' : _EDGE,
  '__module__' : 'dataflow_pb2'
  # @@protoc_insertion_point(class_scope:toroflow.Edge)
  })
_sym_db.RegisterMessage(Edge)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), {
  'DESCRIPTOR' : _VERTEX,
  '__module__' : 'dataflow_pb2'
  # @@protoc_insertion_point(class_scope:toroflow.Vertex)
  })
_sym_db.RegisterMessage(Vertex)

dataflow = _reflection.GeneratedProtocolMessageType('dataflow', (_message.Message,), {
  'DESCRIPTOR' : _DATAFLOW,
  '__module__' : 'dataflow_pb2'
  # @@protoc_insertion_point(class_scope:toroflow.dataflow)
  })
_sym_db.RegisterMessage(dataflow)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUEUETYPE._serialized_start=568
  _QUEUETYPE._serialized_end=626
  _DATAQUEUE._serialized_start=28
  _DATAQUEUE._serialized_end=128
  _EDGE._serialized_start=130
  _EDGE._serialized_end=252
  _VERTEX._serialized_start=255
  _VERTEX._serialized_end=518
  _DATAFLOW._serialized_start=520
  _DATAFLOW._serialized_end=566
# @@protoc_insertion_point(module_scope)
