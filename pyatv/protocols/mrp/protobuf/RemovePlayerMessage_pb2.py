# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import PlayerPath_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a-pyatv/protocols/mrp/protobuf/PlayerPath.proto\"6\n\x13RemovePlayerMessage\x12\x1f\n\nplayerPath\x18\x01 \x01(\x0b\x32\x0b.PlayerPath:C\n\x13removePlayerMessage\x12\x10.ProtocolMessage\x18: \x01(\x0b\x32\x14.RemovePlayerMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.RemovePlayerMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOVEPLAYERMESSAGE']._serialized_start=157
  _globals['_REMOVEPLAYERMESSAGE']._serialized_end=211
# @@protoc_insertion_point(module_scope)
