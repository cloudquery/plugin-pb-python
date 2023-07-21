from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetName(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetVersion(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["version"]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        version: str
        def __init__(self, version: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class Init(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["spec", "no_connection"]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        NO_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        spec: bytes
        no_connection: bool
        def __init__(self, spec: _Optional[bytes] = ..., no_connection: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class GetTables(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["tables", "skip_tables"]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_TABLES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        skip_tables: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., skip_tables: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["tables"]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, tables: _Optional[_Iterable[bytes]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Sync(_message.Message):
    __slots__ = []
    class MessageInsert(_message.Message):
        __slots__ = ["record"]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    class MessageMigrateTable(_message.Message):
        __slots__ = ["table"]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        def __init__(self, table: _Optional[bytes] = ...) -> None: ...
    class BackendOptions(_message.Message):
        __slots__ = ["table_name", "connection"]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        connection: str
        def __init__(self, table_name: _Optional[str] = ..., connection: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ["tables", "skip_tables", "skip_dependent_tables", "deterministic_cq_id", "backend"]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_DEPENDENT_TABLES_FIELD_NUMBER: _ClassVar[int]
        DETERMINISTIC_CQ_ID_FIELD_NUMBER: _ClassVar[int]
        BACKEND_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        skip_tables: _containers.RepeatedScalarFieldContainer[str]
        skip_dependent_tables: bool
        deterministic_cq_id: bool
        backend: Sync.BackendOptions
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., skip_tables: _Optional[_Iterable[str]] = ..., skip_dependent_tables: bool = ..., deterministic_cq_id: bool = ..., backend: _Optional[_Union[Sync.BackendOptions, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["migrate_table", "insert"]
        MIGRATE_TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        migrate_table: Sync.MessageMigrateTable
        insert: Sync.MessageInsert
        def __init__(self, migrate_table: _Optional[_Union[Sync.MessageMigrateTable, _Mapping]] = ..., insert: _Optional[_Union[Sync.MessageInsert, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Read(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["table"]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        def __init__(self, table: _Optional[bytes] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["record"]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class Write(_message.Message):
    __slots__ = []
    class MessageMigrateTable(_message.Message):
        __slots__ = ["table", "migrate_force"]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_FORCE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        migrate_force: bool
        def __init__(self, table: _Optional[bytes] = ..., migrate_force: bool = ...) -> None: ...
    class MessageInsert(_message.Message):
        __slots__ = ["record"]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    class MessageDeleteStale(_message.Message):
        __slots__ = ["table", "source_name", "sync_time", "table_name"]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        source_name: str
        sync_time: _timestamp_pb2.Timestamp
        table_name: str
        def __init__(self, table: _Optional[bytes] = ..., source_name: _Optional[str] = ..., sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., table_name: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ["migrate_table", "insert", "delete"]
        MIGRATE_TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        migrate_table: Write.MessageMigrateTable
        insert: Write.MessageInsert
        delete: Write.MessageDeleteStale
        def __init__(self, migrate_table: _Optional[_Union[Write.MessageMigrateTable, _Mapping]] = ..., insert: _Optional[_Union[Write.MessageInsert, _Mapping]] = ..., delete: _Optional[_Union[Write.MessageDeleteStale, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class Close(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
