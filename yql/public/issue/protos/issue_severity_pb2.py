# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yql/public/issue/protos/issue_severity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yql/public/issue/protos/issue_severity.proto',
  package='NYql',
  syntax='proto3',
  serialized_pb=_b('\n,yql/public/issue/protos/issue_severity.proto\x12\x04NYql\"R\n\x0cTSeverityIds\"B\n\x0b\x45SeverityId\x12\x0b\n\x07S_FATAL\x10\x00\x12\x0b\n\x07S_ERROR\x10\x01\x12\r\n\tS_WARNING\x10\x02\x12\n\n\x06S_INFO\x10\x03\x42\x15\n\x13ru.yandex.yql.protob\x06proto3')
)



_TSEVERITYIDS_ESEVERITYID = _descriptor.EnumDescriptor(
  name='ESeverityId',
  full_name='NYql.TSeverityIds.ESeverityId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='S_FATAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_INFO', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=70,
  serialized_end=136,
)
_sym_db.RegisterEnumDescriptor(_TSEVERITYIDS_ESEVERITYID)


_TSEVERITYIDS = _descriptor.Descriptor(
  name='TSeverityIds',
  full_name='NYql.TSeverityIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TSEVERITYIDS_ESEVERITYID,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=136,
)

_TSEVERITYIDS_ESEVERITYID.containing_type = _TSEVERITYIDS
DESCRIPTOR.message_types_by_name['TSeverityIds'] = _TSEVERITYIDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TSeverityIds = _reflection.GeneratedProtocolMessageType('TSeverityIds', (_message.Message,), dict(
  DESCRIPTOR = _TSEVERITYIDS,
  __module__ = 'yql.public.issue.protos.issue_severity_pb2'
  # @@protoc_insertion_point(class_scope:NYql.TSeverityIds)
  ))
_sym_db.RegisterMessage(TSeverityIds)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023ru.yandex.yql.proto'))
# @@protoc_insertion_point(module_scope)
