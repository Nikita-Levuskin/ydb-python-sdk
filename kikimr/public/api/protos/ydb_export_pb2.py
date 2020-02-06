# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_export.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos.validation import validation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_validation_dot_validation__pb2
from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_export.proto',
  package='Ydb.Export',
  syntax='proto3',
  serialized_pb=_b('\n)kikimr/public/api/protos/ydb_export.proto\x12\nYdb.Export\x1a\x34kikimr/public/api/protos/validation/validation.proto\x1a,kikimr/public/api/protos/ydb_operation.proto\"\xb1\x01\n\x0e\x45xportProgress\"\x9e\x01\n\x08Progress\x12\x18\n\x14PROGRESS_UNSPECIFIED\x10\x00\x12\x16\n\x12PROGRESS_PREPARING\x10\x01\x12\x1a\n\x16PROGRESS_TRANSFER_DATA\x10\x02\x12\x11\n\rPROGRESS_DONE\x10\x03\x12\x19\n\x15PROGRESS_CANCELLATION\x10\x04\x12\x16\n\x12PROGRESS_CANCELLED\x10\x05\"\x83\x02\n\x12\x45xportToYtSettings\x12\x12\n\x04host\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x13\n\x05token\x18\x03 \x01(\tB\x04\x90\xe6*\x01\x12:\n\x05items\x18\x04 \x03(\x0b\x32#.Ydb.Export.ExportToYtSettings.ItemB\x06\x9a\xe6*\x02(\x01\x12\x1c\n\x0b\x64\x65scription\x18\x05 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x19\n\x11number_of_retries\x18\x06 \x01(\r\x1a\x41\n\x04Item\x12\x19\n\x0bsource_path\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x1e\n\x10\x64\x65stination_path\x18\x02 \x01(\tB\x04\x90\xe6*\x01\"\x12\n\x10\x45xportToYtResult\"}\n\x12\x45xportToYtMetadata\x12\x30\n\x08settings\x18\x01 \x01(\x0b\x32\x1e.Ydb.Export.ExportToYtSettings\x12\x35\n\x08progress\x18\x02 \x01(\x0e\x32#.Ydb.Export.ExportProgress.Progress\"\x86\x01\n\x11\x45xportToYtRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x36\n\x08settings\x18\x02 \x01(\x0b\x32\x1e.Ydb.Export.ExportToYtSettingsB\x04\x90\xe6*\x01\"B\n\x12\x45xportToYtResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xe9\x02\n\x12\x45xportToS3Settings\x12\x16\n\x08\x65ndpoint\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x35\n\x06scheme\x18\x02 \x01(\x0e\x32%.Ydb.Export.ExportToS3Settings.Scheme\x12\x14\n\x06\x62ucket\x18\x03 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\naccess_key\x18\x04 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\nsecret_key\x18\x05 \x01(\tB\x04\x90\xe6*\x01\x12:\n\x05items\x18\x06 \x03(\x0b\x32#.Ydb.Export.ExportToS3Settings.ItemB\x06\x9a\xe6*\x02(\x01\x12\x1c\n\x0b\x64\x65scription\x18\x07 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x1a\x41\n\x04Item\x12\x19\n\x0bsource_path\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x1e\n\x10\x64\x65stination_file\x18\x02 \x01(\tB\x04\x90\xe6*\x01\"\x1d\n\x06Scheme\x12\x08\n\x04HTTP\x10\x00\x12\t\n\x05HTTPS\x10\x01\"\x12\n\x10\x45xportToS3Result\"}\n\x12\x45xportToS3Metadata\x12\x30\n\x08settings\x18\x01 \x01(\x0b\x32\x1e.Ydb.Export.ExportToS3Settings\x12\x35\n\x08progress\x18\x02 \x01(\x0e\x32#.Ydb.Export.ExportProgress.Progress\"\x86\x01\n\x11\x45xportToS3Request\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x36\n\x08settings\x18\x02 \x01(\x0b\x32\x1e.Ydb.Export.ExportToS3SettingsB\x04\x90\xe6*\x01\"B\n\x12\x45xportToS3Response\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.OperationB\x1a\n\x15\x63om.yandex.ydb.export\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_validation_dot_validation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,])



_EXPORTPROGRESS_PROGRESS = _descriptor.EnumDescriptor(
  name='Progress',
  full_name='Ydb.Export.ExportProgress.Progress',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_PREPARING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_TRANSFER_DATA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_DONE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_CANCELLATION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_CANCELLED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=177,
  serialized_end=335,
)
_sym_db.RegisterEnumDescriptor(_EXPORTPROGRESS_PROGRESS)

_EXPORTTOS3SETTINGS_SCHEME = _descriptor.EnumDescriptor(
  name='Scheme',
  full_name='Ydb.Export.ExportToS3Settings.Scheme',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTPS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1284,
  serialized_end=1313,
)
_sym_db.RegisterEnumDescriptor(_EXPORTTOS3SETTINGS_SCHEME)


_EXPORTPROGRESS = _descriptor.Descriptor(
  name='ExportProgress',
  full_name='Ydb.Export.ExportProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPORTPROGRESS_PROGRESS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=335,
)


_EXPORTTOYTSETTINGS_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Ydb.Export.ExportToYtSettings.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_path', full_name='Ydb.Export.ExportToYtSettings.Item.source_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='destination_path', full_name='Ydb.Export.ExportToYtSettings.Item.destination_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=597,
)

_EXPORTTOYTSETTINGS = _descriptor.Descriptor(
  name='ExportToYtSettings',
  full_name='Ydb.Export.ExportToYtSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='Ydb.Export.ExportToYtSettings.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='port', full_name='Ydb.Export.ExportToYtSettings.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='Ydb.Export.ExportToYtSettings.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='items', full_name='Ydb.Export.ExportToYtSettings.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\232\346*\002(\001'))),
    _descriptor.FieldDescriptor(
      name='description', full_name='Ydb.Export.ExportToYtSettings.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\242\346*\003\030\200\001'))),
    _descriptor.FieldDescriptor(
      name='number_of_retries', full_name='Ydb.Export.ExportToYtSettings.number_of_retries', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXPORTTOYTSETTINGS_ITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=597,
)


_EXPORTTOYTRESULT = _descriptor.Descriptor(
  name='ExportToYtResult',
  full_name='Ydb.Export.ExportToYtResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=617,
)


_EXPORTTOYTMETADATA = _descriptor.Descriptor(
  name='ExportToYtMetadata',
  full_name='Ydb.Export.ExportToYtMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Export.ExportToYtMetadata.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='Ydb.Export.ExportToYtMetadata.progress', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=744,
)


_EXPORTTOYTREQUEST = _descriptor.Descriptor(
  name='ExportToYtRequest',
  full_name='Ydb.Export.ExportToYtRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Export.ExportToYtRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Export.ExportToYtRequest.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=747,
  serialized_end=881,
)


_EXPORTTOYTRESPONSE = _descriptor.Descriptor(
  name='ExportToYtResponse',
  full_name='Ydb.Export.ExportToYtResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Export.ExportToYtResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=949,
)


_EXPORTTOS3SETTINGS_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Ydb.Export.ExportToS3Settings.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_path', full_name='Ydb.Export.ExportToS3Settings.Item.source_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='destination_file', full_name='Ydb.Export.ExportToS3Settings.Item.destination_file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1217,
  serialized_end=1282,
)

_EXPORTTOS3SETTINGS = _descriptor.Descriptor(
  name='ExportToS3Settings',
  full_name='Ydb.Export.ExportToS3Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='Ydb.Export.ExportToS3Settings.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='scheme', full_name='Ydb.Export.ExportToS3Settings.scheme', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='Ydb.Export.ExportToS3Settings.bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='Ydb.Export.ExportToS3Settings.access_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='Ydb.Export.ExportToS3Settings.secret_key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
    _descriptor.FieldDescriptor(
      name='items', full_name='Ydb.Export.ExportToS3Settings.items', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\232\346*\002(\001'))),
    _descriptor.FieldDescriptor(
      name='description', full_name='Ydb.Export.ExportToS3Settings.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\242\346*\003\030\200\001'))),
  ],
  extensions=[
  ],
  nested_types=[_EXPORTTOS3SETTINGS_ITEM, ],
  enum_types=[
    _EXPORTTOS3SETTINGS_SCHEME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=952,
  serialized_end=1313,
)


_EXPORTTOS3RESULT = _descriptor.Descriptor(
  name='ExportToS3Result',
  full_name='Ydb.Export.ExportToS3Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1315,
  serialized_end=1333,
)


_EXPORTTOS3METADATA = _descriptor.Descriptor(
  name='ExportToS3Metadata',
  full_name='Ydb.Export.ExportToS3Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Export.ExportToS3Metadata.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='Ydb.Export.ExportToS3Metadata.progress', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1335,
  serialized_end=1460,
)


_EXPORTTOS3REQUEST = _descriptor.Descriptor(
  name='ExportToS3Request',
  full_name='Ydb.Export.ExportToS3Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Export.ExportToS3Request.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Export.ExportToS3Request.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1463,
  serialized_end=1597,
)


_EXPORTTOS3RESPONSE = _descriptor.Descriptor(
  name='ExportToS3Response',
  full_name='Ydb.Export.ExportToS3Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Export.ExportToS3Response.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1599,
  serialized_end=1665,
)

_EXPORTPROGRESS_PROGRESS.containing_type = _EXPORTPROGRESS
_EXPORTTOYTSETTINGS_ITEM.containing_type = _EXPORTTOYTSETTINGS
_EXPORTTOYTSETTINGS.fields_by_name['items'].message_type = _EXPORTTOYTSETTINGS_ITEM
_EXPORTTOYTMETADATA.fields_by_name['settings'].message_type = _EXPORTTOYTSETTINGS
_EXPORTTOYTMETADATA.fields_by_name['progress'].enum_type = _EXPORTPROGRESS_PROGRESS
_EXPORTTOYTREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_EXPORTTOYTREQUEST.fields_by_name['settings'].message_type = _EXPORTTOYTSETTINGS
_EXPORTTOYTRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_EXPORTTOS3SETTINGS_ITEM.containing_type = _EXPORTTOS3SETTINGS
_EXPORTTOS3SETTINGS.fields_by_name['scheme'].enum_type = _EXPORTTOS3SETTINGS_SCHEME
_EXPORTTOS3SETTINGS.fields_by_name['items'].message_type = _EXPORTTOS3SETTINGS_ITEM
_EXPORTTOS3SETTINGS_SCHEME.containing_type = _EXPORTTOS3SETTINGS
_EXPORTTOS3METADATA.fields_by_name['settings'].message_type = _EXPORTTOS3SETTINGS
_EXPORTTOS3METADATA.fields_by_name['progress'].enum_type = _EXPORTPROGRESS_PROGRESS
_EXPORTTOS3REQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_EXPORTTOS3REQUEST.fields_by_name['settings'].message_type = _EXPORTTOS3SETTINGS
_EXPORTTOS3RESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['ExportProgress'] = _EXPORTPROGRESS
DESCRIPTOR.message_types_by_name['ExportToYtSettings'] = _EXPORTTOYTSETTINGS
DESCRIPTOR.message_types_by_name['ExportToYtResult'] = _EXPORTTOYTRESULT
DESCRIPTOR.message_types_by_name['ExportToYtMetadata'] = _EXPORTTOYTMETADATA
DESCRIPTOR.message_types_by_name['ExportToYtRequest'] = _EXPORTTOYTREQUEST
DESCRIPTOR.message_types_by_name['ExportToYtResponse'] = _EXPORTTOYTRESPONSE
DESCRIPTOR.message_types_by_name['ExportToS3Settings'] = _EXPORTTOS3SETTINGS
DESCRIPTOR.message_types_by_name['ExportToS3Result'] = _EXPORTTOS3RESULT
DESCRIPTOR.message_types_by_name['ExportToS3Metadata'] = _EXPORTTOS3METADATA
DESCRIPTOR.message_types_by_name['ExportToS3Request'] = _EXPORTTOS3REQUEST
DESCRIPTOR.message_types_by_name['ExportToS3Response'] = _EXPORTTOS3RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExportProgress = _reflection.GeneratedProtocolMessageType('ExportProgress', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTPROGRESS,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportProgress)
  ))
_sym_db.RegisterMessage(ExportProgress)

ExportToYtSettings = _reflection.GeneratedProtocolMessageType('ExportToYtSettings', (_message.Message,), dict(

  Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
    DESCRIPTOR = _EXPORTTOYTSETTINGS_ITEM,
    __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtSettings.Item)
    ))
  ,
  DESCRIPTOR = _EXPORTTOYTSETTINGS,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtSettings)
  ))
_sym_db.RegisterMessage(ExportToYtSettings)
_sym_db.RegisterMessage(ExportToYtSettings.Item)

ExportToYtResult = _reflection.GeneratedProtocolMessageType('ExportToYtResult', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOYTRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtResult)
  ))
_sym_db.RegisterMessage(ExportToYtResult)

ExportToYtMetadata = _reflection.GeneratedProtocolMessageType('ExportToYtMetadata', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOYTMETADATA,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtMetadata)
  ))
_sym_db.RegisterMessage(ExportToYtMetadata)

ExportToYtRequest = _reflection.GeneratedProtocolMessageType('ExportToYtRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOYTREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtRequest)
  ))
_sym_db.RegisterMessage(ExportToYtRequest)

ExportToYtResponse = _reflection.GeneratedProtocolMessageType('ExportToYtResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOYTRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToYtResponse)
  ))
_sym_db.RegisterMessage(ExportToYtResponse)

ExportToS3Settings = _reflection.GeneratedProtocolMessageType('ExportToS3Settings', (_message.Message,), dict(

  Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
    DESCRIPTOR = _EXPORTTOS3SETTINGS_ITEM,
    __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Settings.Item)
    ))
  ,
  DESCRIPTOR = _EXPORTTOS3SETTINGS,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Settings)
  ))
_sym_db.RegisterMessage(ExportToS3Settings)
_sym_db.RegisterMessage(ExportToS3Settings.Item)

ExportToS3Result = _reflection.GeneratedProtocolMessageType('ExportToS3Result', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOS3RESULT,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Result)
  ))
_sym_db.RegisterMessage(ExportToS3Result)

ExportToS3Metadata = _reflection.GeneratedProtocolMessageType('ExportToS3Metadata', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOS3METADATA,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Metadata)
  ))
_sym_db.RegisterMessage(ExportToS3Metadata)

ExportToS3Request = _reflection.GeneratedProtocolMessageType('ExportToS3Request', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOS3REQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Request)
  ))
_sym_db.RegisterMessage(ExportToS3Request)

ExportToS3Response = _reflection.GeneratedProtocolMessageType('ExportToS3Response', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTTOS3RESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_export_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Export.ExportToS3Response)
  ))
_sym_db.RegisterMessage(ExportToS3Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.yandex.ydb.export\370\001\001'))
_EXPORTTOYTSETTINGS_ITEM.fields_by_name['source_path'].has_options = True
_EXPORTTOYTSETTINGS_ITEM.fields_by_name['source_path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOYTSETTINGS_ITEM.fields_by_name['destination_path'].has_options = True
_EXPORTTOYTSETTINGS_ITEM.fields_by_name['destination_path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOYTSETTINGS.fields_by_name['host'].has_options = True
_EXPORTTOYTSETTINGS.fields_by_name['host']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOYTSETTINGS.fields_by_name['token'].has_options = True
_EXPORTTOYTSETTINGS.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOYTSETTINGS.fields_by_name['items'].has_options = True
_EXPORTTOYTSETTINGS.fields_by_name['items']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\232\346*\002(\001'))
_EXPORTTOYTSETTINGS.fields_by_name['description'].has_options = True
_EXPORTTOYTSETTINGS.fields_by_name['description']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\242\346*\003\030\200\001'))
_EXPORTTOYTREQUEST.fields_by_name['settings'].has_options = True
_EXPORTTOYTREQUEST.fields_by_name['settings']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS_ITEM.fields_by_name['source_path'].has_options = True
_EXPORTTOS3SETTINGS_ITEM.fields_by_name['source_path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS_ITEM.fields_by_name['destination_file'].has_options = True
_EXPORTTOS3SETTINGS_ITEM.fields_by_name['destination_file']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS.fields_by_name['endpoint'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['endpoint']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS.fields_by_name['bucket'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['bucket']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS.fields_by_name['access_key'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['access_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS.fields_by_name['secret_key'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['secret_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
_EXPORTTOS3SETTINGS.fields_by_name['items'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['items']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\232\346*\002(\001'))
_EXPORTTOS3SETTINGS.fields_by_name['description'].has_options = True
_EXPORTTOS3SETTINGS.fields_by_name['description']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\242\346*\003\030\200\001'))
_EXPORTTOS3REQUEST.fields_by_name['settings'].has_options = True
_EXPORTTOS3REQUEST.fields_by_name['settings']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\346*\001'))
# @@protoc_insertion_point(module_scope)
