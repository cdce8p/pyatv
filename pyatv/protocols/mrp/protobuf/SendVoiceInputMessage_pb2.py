# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyatv/protocols/mrp/protobuf/SendVoiceInputMessage.proto
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
    'pyatv/protocols/mrp/protobuf/SendVoiceInputMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import AudioFormatSettingsMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_AudioFormatSettingsMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8pyatv/protocols/mrp/protobuf/SendVoiceInputMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a=pyatv/protocols/mrp/protobuf/AudioFormatSettingsMessage.proto\"i\n\x1c\x41udioStreamPacketDescription\x12\x13\n\x0bstartOffset\x18\x01 \x01(\x03\x12\x1e\n\x16variableFramesInPacket\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x61taByteSize\x18\x03 \x01(\r\"\xd0\x01\n\x0b\x41udioBuffer\x12,\n\x0e\x66ormatSettings\x18\x01 \x01(\x0b\x32\x14.AudioFormatSettings\x12\x16\n\x0epacketCapacity\x18\x02 \x01(\x03\x12\x19\n\x11maximumPacketSize\x18\x03 \x01(\x03\x12\x13\n\x0bpacketCount\x18\x04 \x01(\x03\x12\x10\n\x08\x63ontents\x18\x05 \x01(\x0c\x12\x39\n\x12packetDescriptions\x18\x06 \x03(\x0b\x32\x1d.AudioStreamPacketDescription\"2\n\tAudioTime\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x12\n\nsampleRate\x18\x02 \x01(\x01\"V\n\x0e\x41udioDataBlock\x12\x1c\n\x06\x62uffer\x18\x01 \x01(\x0b\x32\x0c.AudioBuffer\x12\x18\n\x04time\x18\x02 \x01(\x0b\x32\n.AudioTime\x12\x0c\n\x04gain\x18\x03 \x01(\x01\";\n\x15SendVoiceInputMessage\x12\"\n\tdataBlock\x18\x01 \x01(\x0b\x32\x0f.AudioDataBlock:G\n\x15sendVoiceInputMessage\x12\x10.ProtocolMessage\x18$ \x01(\x0b\x32\x16.SendVoiceInputMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.SendVoiceInputMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUDIOSTREAMPACKETDESCRIPTION']._serialized_start=175
  _globals['_AUDIOSTREAMPACKETDESCRIPTION']._serialized_end=280
  _globals['_AUDIOBUFFER']._serialized_start=283
  _globals['_AUDIOBUFFER']._serialized_end=491
  _globals['_AUDIOTIME']._serialized_start=493
  _globals['_AUDIOTIME']._serialized_end=543
  _globals['_AUDIODATABLOCK']._serialized_start=545
  _globals['_AUDIODATABLOCK']._serialized_end=631
  _globals['_SENDVOICEINPUTMESSAGE']._serialized_start=633
  _globals['_SENDVOICEINPUTMESSAGE']._serialized_end=692
# @@protoc_insertion_point(module_scope)
