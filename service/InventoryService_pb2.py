# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from service import Book_pb2 as Book__pb2
from service import InventoryItem_pb2 as InventoryItem__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16InventoryService.proto\x1a\nBook.proto\x1a\x13InventoryItem.proto\"0\n\x11\x43reateBookRequest\x12\x1b\n\x07newBook\x18\x01 \x01(\x0b\x32\n.book.Book\"%\n\x12\x43reateBookResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"a\n\x0fGetBookResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x1a\n\x05genre\x18\x03 \x01(\x0e\x32\x0b.book.Genre\x12\x13\n\x0bpublishYear\x18\x04 \x01(\x05\x32{\n\x10InventoryService\x12\x37\n\nCreateBook\x12\x12.CreateBookRequest\x1a\x13.CreateBookResponse\"\x00\x12.\n\x07GetBook\x12\x0f.GetBookRequest\x1a\x10.GetBookResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InventoryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBOOKREQUEST._serialized_start=59
  _CREATEBOOKREQUEST._serialized_end=107
  _CREATEBOOKRESPONSE._serialized_start=109
  _CREATEBOOKRESPONSE._serialized_end=146
  _GETBOOKREQUEST._serialized_start=148
  _GETBOOKREQUEST._serialized_end=178
  _GETBOOKRESPONSE._serialized_start=180
  _GETBOOKRESPONSE._serialized_end=277
  _INVENTORYSERVICE._serialized_start=279
  _INVENTORYSERVICE._serialized_end=402
# @@protoc_insertion_point(module_scope)