# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_scripting_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_scripting_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__scripting__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_scripting_v1.proto',
  package='Ydb.Scripting.V1',
  syntax='proto3',
  serialized_pb=_b('\n-kikimr/public/api/grpc/ydb_scripting_v1.proto\x12\x10Ydb.Scripting.V1\x1a,kikimr/public/api/protos/ydb_scripting.proto2e\n\x10ScriptingService\x12Q\n\nExecuteYql\x12 .Ydb.Scripting.ExecuteYqlRequest\x1a!.Ydb.Scripting.ExecuteYqlResponseB\x1c\n\x1aru.yandex.ydb.scripting.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__scripting__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032ru.yandex.ydb.scripting.v1'))

_SCRIPTINGSERVICE = _descriptor.ServiceDescriptor(
  name='ScriptingService',
  full_name='Ydb.Scripting.V1.ScriptingService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=113,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteYql',
    full_name='Ydb.Scripting.V1.ScriptingService.ExecuteYql',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scripting__pb2._EXECUTEYQLREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scripting__pb2._EXECUTEYQLRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCRIPTINGSERVICE)

DESCRIPTOR.services_by_name['ScriptingService'] = _SCRIPTINGSERVICE

# @@protoc_insertion_point(module_scope)