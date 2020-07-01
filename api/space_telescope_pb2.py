# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/space_telescope.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/space_telescope.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x61pi/space_telescope.proto\"\x1a\n\x0cImageRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x9a\x01\n\nImageReply\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0crelease_date\x18\x03 \x01(\t\x12\x18\n\x10related_releases\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0e\n\x06\x63redit\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t2<\n\x05Image\x12\x33\n\x13GetImageInformation\x12\r.ImageRequest\x1a\x0b.ImageReply\"\x00\x62\x06proto3')
)




_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ImageRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=55,
)


_IMAGEREPLY = _descriptor.Descriptor(
  name='ImageReply',
  full_name='ImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ImageReply.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ImageReply.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_date', full_name='ImageReply.release_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='related_releases', full_name='ImageReply.related_releases', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='ImageReply.width', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='ImageReply.height', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credit', full_name='ImageReply.credit', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ImageReply.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=212,
)

DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['ImageReply'] = _IMAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'api.space_telescope_pb2'
  # @@protoc_insertion_point(class_scope:ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

ImageReply = _reflection.GeneratedProtocolMessageType('ImageReply', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREPLY,
  '__module__' : 'api.space_telescope_pb2'
  # @@protoc_insertion_point(class_scope:ImageReply)
  })
_sym_db.RegisterMessage(ImageReply)



_IMAGE = _descriptor.ServiceDescriptor(
  name='Image',
  full_name='Image',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=214,
  serialized_end=274,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImageInformation',
    full_name='Image.GetImageInformation',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGE)

DESCRIPTOR.services_by_name['Image'] = _IMAGE

# @@protoc_insertion_point(module_scope)