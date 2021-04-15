# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_datastreams_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos.draft import datastreams_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_datastreams_v1.proto',
  package='Ydb.DataStreams.V1',
  syntax='proto3',
  serialized_pb=_b('\n5kikimr/public/api/grpc/draft/ydb_datastreams_v1.proto\x12\x12Ydb.DataStreams.V1\x1a\x30kikimr/public/api/protos/draft/datastreams.proto2\xe5\x1a\n\x12\x44\x61taStreamsService\x12\x61\n\x0c\x43reateStream\x12\'.Ydb.DataStreams.V1.CreateStreamRequest\x1a(.Ydb.DataStreams.V1.CreateStreamResponse\x12^\n\x0bListStreams\x12&.Ydb.DataStreams.V1.ListStreamsRequest\x1a\'.Ydb.DataStreams.V1.ListStreamsResponse\x12\x61\n\x0c\x44\x65leteStream\x12\'.Ydb.DataStreams.V1.DeleteStreamRequest\x1a(.Ydb.DataStreams.V1.DeleteStreamResponse\x12g\n\x0e\x44\x65scribeStream\x12).Ydb.DataStreams.V1.DescribeStreamRequest\x1a*.Ydb.DataStreams.V1.DescribeStreamResponse\x12[\n\nListShards\x12%.Ydb.DataStreams.V1.ListShardsRequest\x1a&.Ydb.DataStreams.V1.ListShardsResponse\x12\x64\n\rSetWriteQuota\x12(.Ydb.DataStreams.V1.SetWriteQuotaRequest\x1a).Ydb.DataStreams.V1.SetWriteQuotaResponse\x12\x61\n\x0cUpdateStream\x12\'.Ydb.DataStreams.V1.UpdateStreamRequest\x1a(.Ydb.DataStreams.V1.UpdateStreamResponse\x12X\n\tPutRecord\x12$.Ydb.DataStreams.V1.PutRecordRequest\x1a%.Ydb.DataStreams.V1.PutRecordResponse\x12[\n\nPutRecords\x12%.Ydb.DataStreams.V1.PutRecordsRequest\x1a&.Ydb.DataStreams.V1.PutRecordsResponse\x12[\n\nGetRecords\x12%.Ydb.DataStreams.V1.GetRecordsRequest\x1a&.Ydb.DataStreams.V1.GetRecordsResponse\x12m\n\x10GetShardIterator\x12+.Ydb.DataStreams.V1.GetShardIteratorRequest\x1a,.Ydb.DataStreams.V1.GetShardIteratorResponse\x12o\n\x10SubscribeToShard\x12+.Ydb.DataStreams.V1.SubscribeToShardRequest\x1a,.Ydb.DataStreams.V1.SubscribeToShardResponse0\x01\x12g\n\x0e\x44\x65scribeLimits\x12).Ydb.DataStreams.V1.DescribeLimitsRequest\x1a*.Ydb.DataStreams.V1.DescribeLimitsResponse\x12|\n\x15\x44\x65scribeStreamSummary\x12\x30.Ydb.DataStreams.V1.DescribeStreamSummaryRequest\x1a\x31.Ydb.DataStreams.V1.DescribeStreamSummaryResponse\x12\x94\x01\n\x1d\x44\x65\x63reaseStreamRetentionPeriod\x12\x38.Ydb.DataStreams.V1.DecreaseStreamRetentionPeriodRequest\x1a\x39.Ydb.DataStreams.V1.DecreaseStreamRetentionPeriodResponse\x12\x94\x01\n\x1dIncreaseStreamRetentionPeriod\x12\x38.Ydb.DataStreams.V1.IncreaseStreamRetentionPeriodRequest\x1a\x39.Ydb.DataStreams.V1.IncreaseStreamRetentionPeriodResponse\x12m\n\x10UpdateShardCount\x12+.Ydb.DataStreams.V1.UpdateShardCountRequest\x1a,.Ydb.DataStreams.V1.UpdateShardCountResponse\x12\x7f\n\x16RegisterStreamConsumer\x12\x31.Ydb.DataStreams.V1.RegisterStreamConsumerRequest\x1a\x32.Ydb.DataStreams.V1.RegisterStreamConsumerResponse\x12\x85\x01\n\x18\x44\x65registerStreamConsumer\x12\x33.Ydb.DataStreams.V1.DeregisterStreamConsumerRequest\x1a\x34.Ydb.DataStreams.V1.DeregisterStreamConsumerResponse\x12\x7f\n\x16\x44\x65scribeStreamConsumer\x12\x31.Ydb.DataStreams.V1.DescribeStreamConsumerRequest\x1a\x32.Ydb.DataStreams.V1.DescribeStreamConsumerResponse\x12v\n\x13ListStreamConsumers\x12..Ydb.DataStreams.V1.ListStreamConsumersRequest\x1a/.Ydb.DataStreams.V1.ListStreamConsumersResponse\x12j\n\x0f\x41\x64\x64TagsToStream\x12*.Ydb.DataStreams.V1.AddTagsToStreamRequest\x1a+.Ydb.DataStreams.V1.AddTagsToStreamResponse\x12\x88\x01\n\x19\x44isableEnhancedMonitoring\x12\x34.Ydb.DataStreams.V1.DisableEnhancedMonitoringRequest\x1a\x35.Ydb.DataStreams.V1.DisableEnhancedMonitoringResponse\x12\x85\x01\n\x18\x45nableEnhancedMonitoring\x12\x33.Ydb.DataStreams.V1.EnableEnhancedMonitoringRequest\x1a\x34.Ydb.DataStreams.V1.EnableEnhancedMonitoringResponse\x12p\n\x11ListTagsForStream\x12,.Ydb.DataStreams.V1.ListTagsForStreamRequest\x1a-.Ydb.DataStreams.V1.ListTagsForStreamResponse\x12^\n\x0bMergeShards\x12&.Ydb.DataStreams.V1.MergeShardsRequest\x1a\'.Ydb.DataStreams.V1.MergeShardsResponse\x12y\n\x14RemoveTagsFromStream\x12/.Ydb.DataStreams.V1.RemoveTagsFromStreamRequest\x1a\x30.Ydb.DataStreams.V1.RemoveTagsFromStreamResponse\x12[\n\nSplitShard\x12%.Ydb.DataStreams.V1.SplitShardRequest\x1a&.Ydb.DataStreams.V1.SplitShardResponse\x12|\n\x15StartStreamEncryption\x12\x30.Ydb.DataStreams.V1.StartStreamEncryptionRequest\x1a\x31.Ydb.DataStreams.V1.StartStreamEncryptionResponse\x12y\n\x14StopStreamEncryption\x12/.Ydb.DataStreams.V1.StopStreamEncryptionRequest\x1a\x30.Ydb.DataStreams.V1.StopStreamEncryptionResponseB\"\n\x1d\x63om.yandex.ydb.datastreams.v1\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035com.yandex.ydb.datastreams.v1\370\001\001'))

_DATASTREAMSSERVICE = _descriptor.ServiceDescriptor(
  name='DataStreamsService',
  full_name='Ydb.DataStreams.V1.DataStreamsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=128,
  serialized_end=3557,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.CreateStream',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._CREATESTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._CREATESTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListStreams',
    full_name='Ydb.DataStreams.V1.DataStreamsService.ListStreams',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSTREAMSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSTREAMSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DeleteStream',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DELETESTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DELETESTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DescribeStream',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListShards',
    full_name='Ydb.DataStreams.V1.DataStreamsService.ListShards',
    index=4,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSHARDSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSHARDSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetWriteQuota',
    full_name='Ydb.DataStreams.V1.DataStreamsService.SetWriteQuota',
    index=5,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SETWRITEQUOTAREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SETWRITEQUOTARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.UpdateStream',
    index=6,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._UPDATESTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._UPDATESTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutRecord',
    full_name='Ydb.DataStreams.V1.DataStreamsService.PutRecord',
    index=7,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._PUTRECORDREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._PUTRECORDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutRecords',
    full_name='Ydb.DataStreams.V1.DataStreamsService.PutRecords',
    index=8,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._PUTRECORDSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._PUTRECORDSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRecords',
    full_name='Ydb.DataStreams.V1.DataStreamsService.GetRecords',
    index=9,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._GETRECORDSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._GETRECORDSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShardIterator',
    full_name='Ydb.DataStreams.V1.DataStreamsService.GetShardIterator',
    index=10,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._GETSHARDITERATORREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._GETSHARDITERATORRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeToShard',
    full_name='Ydb.DataStreams.V1.DataStreamsService.SubscribeToShard',
    index=11,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SUBSCRIBETOSHARDREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SUBSCRIBETOSHARDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeLimits',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DescribeLimits',
    index=12,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBELIMITSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBELIMITSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeStreamSummary',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DescribeStreamSummary',
    index=13,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMSUMMARYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMSUMMARYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DecreaseStreamRetentionPeriod',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DecreaseStreamRetentionPeriod',
    index=14,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DECREASESTREAMRETENTIONPERIODREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DECREASESTREAMRETENTIONPERIODRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IncreaseStreamRetentionPeriod',
    full_name='Ydb.DataStreams.V1.DataStreamsService.IncreaseStreamRetentionPeriod',
    index=15,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._INCREASESTREAMRETENTIONPERIODREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._INCREASESTREAMRETENTIONPERIODRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateShardCount',
    full_name='Ydb.DataStreams.V1.DataStreamsService.UpdateShardCount',
    index=16,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._UPDATESHARDCOUNTREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._UPDATESHARDCOUNTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterStreamConsumer',
    full_name='Ydb.DataStreams.V1.DataStreamsService.RegisterStreamConsumer',
    index=17,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._REGISTERSTREAMCONSUMERREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._REGISTERSTREAMCONSUMERRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeregisterStreamConsumer',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DeregisterStreamConsumer',
    index=18,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DEREGISTERSTREAMCONSUMERREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DEREGISTERSTREAMCONSUMERRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeStreamConsumer',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DescribeStreamConsumer',
    index=19,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMCONSUMERREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DESCRIBESTREAMCONSUMERRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListStreamConsumers',
    full_name='Ydb.DataStreams.V1.DataStreamsService.ListStreamConsumers',
    index=20,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSTREAMCONSUMERSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTSTREAMCONSUMERSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTagsToStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.AddTagsToStream',
    index=21,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._ADDTAGSTOSTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._ADDTAGSTOSTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DisableEnhancedMonitoring',
    full_name='Ydb.DataStreams.V1.DataStreamsService.DisableEnhancedMonitoring',
    index=22,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DISABLEENHANCEDMONITORINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._DISABLEENHANCEDMONITORINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnableEnhancedMonitoring',
    full_name='Ydb.DataStreams.V1.DataStreamsService.EnableEnhancedMonitoring',
    index=23,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._ENABLEENHANCEDMONITORINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._ENABLEENHANCEDMONITORINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTagsForStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.ListTagsForStream',
    index=24,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTTAGSFORSTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._LISTTAGSFORSTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MergeShards',
    full_name='Ydb.DataStreams.V1.DataStreamsService.MergeShards',
    index=25,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._MERGESHARDSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._MERGESHARDSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveTagsFromStream',
    full_name='Ydb.DataStreams.V1.DataStreamsService.RemoveTagsFromStream',
    index=26,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._REMOVETAGSFROMSTREAMREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._REMOVETAGSFROMSTREAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SplitShard',
    full_name='Ydb.DataStreams.V1.DataStreamsService.SplitShard',
    index=27,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SPLITSHARDREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._SPLITSHARDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartStreamEncryption',
    full_name='Ydb.DataStreams.V1.DataStreamsService.StartStreamEncryption',
    index=28,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._STARTSTREAMENCRYPTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._STARTSTREAMENCRYPTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopStreamEncryption',
    full_name='Ydb.DataStreams.V1.DataStreamsService.StopStreamEncryption',
    index=29,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._STOPSTREAMENCRYPTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_datastreams__pb2._STOPSTREAMENCRYPTIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASTREAMSSERVICE)

DESCRIPTOR.services_by_name['DataStreamsService'] = _DATASTREAMSSERVICE

# @@protoc_insertion_point(module_scope)
