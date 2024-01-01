from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetVersions(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("versions",)
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        versions: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, versions: _Optional[_Iterable[int]] = ...) -> None: ...
    def __init__(self) -> None: ...
