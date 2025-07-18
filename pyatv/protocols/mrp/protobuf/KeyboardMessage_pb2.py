# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyatv/protocols/mrp/protobuf/KeyboardMessage.proto
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
    'pyatv/protocols/mrp/protobuf/KeyboardMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2pyatv/protocols/mrp/protobuf/KeyboardMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"\x8a\x01\n\rKeyboardState\"y\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\x0e\n\nNotEditing\x10\x01\x12\x13\n\x0f\x44idBeginEditing\x10\x02\x12\x0b\n\x07\x45\x64iting\x10\x03\x12\x11\n\rTextDidChange\x10\x04\x12\x11\n\rDidEndEditing\x10\x05\x12\x0c\n\x08Response\x10\x06\"W\n\x16\x41utocapitalizationType\"=\n\x04\x45num\x12\x08\n\x04None\x10\x00\x12\t\n\x05Words\x10\x01\x12\r\n\tSentences\x10\x02\x12\x11\n\rAllCharacters\x10\x03\"\xe7\x01\n\x0cKeyboardType\"\xd6\x01\n\x04\x45num\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x11\n\rASCII_Capable\x10\x01\x12\x19\n\x15NumbersAndPunctuation\x10\x02\x12\x07\n\x03URL\x10\x03\x12\r\n\tNumberPad\x10\x04\x12\x0c\n\x08PhonePad\x10\x05\x12\x10\n\x0cNamePhonePad\x10\x06\x12\x10\n\x0c\x45mailAddress\x10\x07\x12\x0e\n\nDecimalPad\x10\x08\x12\x0b\n\x07Twitter\x10\t\x12\r\n\tWebSearch\x10\n\x12\x0c\n\x08\x41lphanet\x10\x0b\x12\x0f\n\x0bPasscodePad\x10\x0c\"\xa4\x01\n\rReturnKeyType\"\x92\x01\n\x04\x45num\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x06\n\x02Go\x10\x01\x12\n\n\x06Google\x10\x02\x12\x08\n\x04Join\x10\x03\x12\x08\n\x04Next\x10\x04\x12\t\n\x05Route\x10\x05\x12\n\n\x06Search\x10\x06\x12\x08\n\x04Send\x10\x07\x12\t\n\x05Yahoo\x10\x08\x12\x08\n\x04\x44one\x10\t\x12\x11\n\rEmergencyCall\x10\n\x12\x0c\n\x08\x43ontinue\x10\x0b\"\xf4\x02\n\x0fTextInputTraits\x12<\n\x16\x61utocapitalizationType\x18\x01 \x01(\x0e\x32\x1c.AutocapitalizationType.Enum\x12(\n\x0ckeyboardType\x18\x02 \x01(\x0e\x32\x12.KeyboardType.Enum\x12*\n\rreturnKeyType\x18\x03 \x01(\x0e\x32\x13.ReturnKeyType.Enum\x12\x16\n\x0e\x61utocorrection\x18\x04 \x01(\x08\x12\x15\n\rspellchecking\x18\x05 \x01(\x08\x12%\n\x1d\x65nablesReturnKeyAutomatically\x18\x06 \x01(\x08\x12\x17\n\x0fsecureTextEntry\x18\x07 \x01(\x08\x12\x1e\n\x16validTextRangeLocation\x18\x08 \x01(\x04\x12\x1c\n\x14validTextRangeLength\x18\t \x01(\x04\x12 \n\x18pINEntrySeparatorIndexes\x18\n \x03(\x04\"]\n\x15TextEditingAttributes\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12%\n\x0binputTraits\x18\x03 \x01(\x0b\x32\x10.TextInputTraits\"\x82\x01\n\x0fKeyboardMessage\x12\"\n\x05state\x18\x01 \x01(\x0e\x32\x13.KeyboardState.Enum\x12*\n\nattributes\x18\x03 \x01(\x0b\x32\x16.TextEditingAttributes\x12\x1f\n\x17\x65ncryptedTextCyphertext\x18\x04 \x01(\x0c:;\n\x0fkeyboardMessage\x12\x10.ProtocolMessage\x18\x1c \x01(\x0b\x32\x10.KeyboardMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.KeyboardMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KEYBOARDSTATE']._serialized_start=107
  _globals['_KEYBOARDSTATE']._serialized_end=245
  _globals['_KEYBOARDSTATE_ENUM']._serialized_start=124
  _globals['_KEYBOARDSTATE_ENUM']._serialized_end=245
  _globals['_AUTOCAPITALIZATIONTYPE']._serialized_start=247
  _globals['_AUTOCAPITALIZATIONTYPE']._serialized_end=334
  _globals['_AUTOCAPITALIZATIONTYPE_ENUM']._serialized_start=273
  _globals['_AUTOCAPITALIZATIONTYPE_ENUM']._serialized_end=334
  _globals['_KEYBOARDTYPE']._serialized_start=337
  _globals['_KEYBOARDTYPE']._serialized_end=568
  _globals['_KEYBOARDTYPE_ENUM']._serialized_start=354
  _globals['_KEYBOARDTYPE_ENUM']._serialized_end=568
  _globals['_RETURNKEYTYPE']._serialized_start=571
  _globals['_RETURNKEYTYPE']._serialized_end=735
  _globals['_RETURNKEYTYPE_ENUM']._serialized_start=589
  _globals['_RETURNKEYTYPE_ENUM']._serialized_end=735
  _globals['_TEXTINPUTTRAITS']._serialized_start=738
  _globals['_TEXTINPUTTRAITS']._serialized_end=1110
  _globals['_TEXTEDITINGATTRIBUTES']._serialized_start=1112
  _globals['_TEXTEDITINGATTRIBUTES']._serialized_end=1205
  _globals['_KEYBOARDMESSAGE']._serialized_start=1208
  _globals['_KEYBOARDMESSAGE']._serialized_end=1338
# @@protoc_insertion_point(module_scope)
