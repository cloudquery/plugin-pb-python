from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetName(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetVersion(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("version",)
        VERSION_FIELD_NUMBER: _ClassVar[int]
        version: str
        def __init__(self, version: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetSpecSchema(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("json_schema",)
        JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        json_schema: str
        def __init__(self, json_schema: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class Init(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("spec", "no_connection", "invocation_id")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        NO_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        spec: bytes
        no_connection: bool
        invocation_id: str
        def __init__(self, spec: _Optional[bytes] = ..., no_connection: bool = ..., invocation_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class GetTables(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("tables", "skip_tables", "skip_dependent_tables")
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_DEPENDENT_TABLES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        skip_tables: _containers.RepeatedScalarFieldContainer[str]
        skip_dependent_tables: bool
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., skip_tables: _Optional[_Iterable[str]] = ..., skip_dependent_tables: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("tables",)
        TABLES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, tables: _Optional[_Iterable[bytes]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Sync(_message.Message):
    __slots__ = ()
    class MessageInsert(_message.Message):
        __slots__ = ("record",)
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    class MessageMigrateTable(_message.Message):
        __slots__ = ("table",)
        TABLE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        def __init__(self, table: _Optional[bytes] = ...) -> None: ...
    class MessageDeleteRecord(_message.Message):
        __slots__ = ("table_name", "where_clause", "table_relations")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
        TABLE_RELATIONS_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        where_clause: _containers.RepeatedCompositeFieldContainer[PredicatesGroup]
        table_relations: _containers.RepeatedCompositeFieldContainer[TableRelation]
        def __init__(self, table_name: _Optional[str] = ..., where_clause: _Optional[_Iterable[_Union[PredicatesGroup, _Mapping]]] = ..., table_relations: _Optional[_Iterable[_Union[TableRelation, _Mapping]]] = ...) -> None: ...
    class BackendOptions(_message.Message):
        __slots__ = ("table_name", "connection")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        connection: str
        def __init__(self, table_name: _Optional[str] = ..., connection: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ("tables", "skip_tables", "skip_dependent_tables", "deterministic_cq_id", "backend", "shard")
        class Shard(_message.Message):
            __slots__ = ("num", "total")
            NUM_FIELD_NUMBER: _ClassVar[int]
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            num: int
            total: int
            def __init__(self, num: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_TABLES_FIELD_NUMBER: _ClassVar[int]
        SKIP_DEPENDENT_TABLES_FIELD_NUMBER: _ClassVar[int]
        DETERMINISTIC_CQ_ID_FIELD_NUMBER: _ClassVar[int]
        BACKEND_FIELD_NUMBER: _ClassVar[int]
        SHARD_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        skip_tables: _containers.RepeatedScalarFieldContainer[str]
        skip_dependent_tables: bool
        deterministic_cq_id: bool
        backend: Sync.BackendOptions
        shard: Sync.Request.Shard
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., skip_tables: _Optional[_Iterable[str]] = ..., skip_dependent_tables: bool = ..., deterministic_cq_id: bool = ..., backend: _Optional[_Union[Sync.BackendOptions, _Mapping]] = ..., shard: _Optional[_Union[Sync.Request.Shard, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("migrate_table", "insert", "delete_record")
        MIGRATE_TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        DELETE_RECORD_FIELD_NUMBER: _ClassVar[int]
        migrate_table: Sync.MessageMigrateTable
        insert: Sync.MessageInsert
        delete_record: Sync.MessageDeleteRecord
        def __init__(self, migrate_table: _Optional[_Union[Sync.MessageMigrateTable, _Mapping]] = ..., insert: _Optional[_Union[Sync.MessageInsert, _Mapping]] = ..., delete_record: _Optional[_Union[Sync.MessageDeleteRecord, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Read(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("table",)
        TABLE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        def __init__(self, table: _Optional[bytes] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("record",)
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class TableRelation(_message.Message):
    __slots__ = ("table_name", "parent_table")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_TABLE_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    parent_table: str
    def __init__(self, table_name: _Optional[str] = ..., parent_table: _Optional[str] = ...) -> None: ...

class Predicate(_message.Message):
    __slots__ = ("operator", "column", "record")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EQ: _ClassVar[Predicate.Operator]
    EQ: Predicate.Operator
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    operator: Predicate.Operator
    column: str
    record: bytes
    def __init__(self, operator: _Optional[_Union[Predicate.Operator, str]] = ..., column: _Optional[str] = ..., record: _Optional[bytes] = ...) -> None: ...

class PredicatesGroup(_message.Message):
    __slots__ = ("grouping_type", "predicates")
    class GroupingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AND: _ClassVar[PredicatesGroup.GroupingType]
        OR: _ClassVar[PredicatesGroup.GroupingType]
    AND: PredicatesGroup.GroupingType
    OR: PredicatesGroup.GroupingType
    GROUPING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREDICATES_FIELD_NUMBER: _ClassVar[int]
    grouping_type: PredicatesGroup.GroupingType
    predicates: _containers.RepeatedCompositeFieldContainer[Predicate]
    def __init__(self, grouping_type: _Optional[_Union[PredicatesGroup.GroupingType, str]] = ..., predicates: _Optional[_Iterable[_Union[Predicate, _Mapping]]] = ...) -> None: ...

class Write(_message.Message):
    __slots__ = ()
    class MessageMigrateTable(_message.Message):
        __slots__ = ("table", "migrate_force")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_FORCE_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        migrate_force: bool
        def __init__(self, table: _Optional[bytes] = ..., migrate_force: bool = ...) -> None: ...
    class MessageInsert(_message.Message):
        __slots__ = ("record",)
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    class MessageDeleteStale(_message.Message):
        __slots__ = ("table", "source_name", "sync_time", "table_name")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        table: bytes
        source_name: str
        sync_time: _timestamp_pb2.Timestamp
        table_name: str
        def __init__(self, table: _Optional[bytes] = ..., source_name: _Optional[str] = ..., sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., table_name: _Optional[str] = ...) -> None: ...
    class MessageDeleteRecord(_message.Message):
        __slots__ = ("table_name", "where_clause", "table_relations")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
        TABLE_RELATIONS_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        where_clause: _containers.RepeatedCompositeFieldContainer[PredicatesGroup]
        table_relations: _containers.RepeatedCompositeFieldContainer[TableRelation]
        def __init__(self, table_name: _Optional[str] = ..., where_clause: _Optional[_Iterable[_Union[PredicatesGroup, _Mapping]]] = ..., table_relations: _Optional[_Iterable[_Union[TableRelation, _Mapping]]] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ("migrate_table", "insert", "delete", "delete_record")
        MIGRATE_TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        DELETE_RECORD_FIELD_NUMBER: _ClassVar[int]
        migrate_table: Write.MessageMigrateTable
        insert: Write.MessageInsert
        delete: Write.MessageDeleteStale
        delete_record: Write.MessageDeleteRecord
        def __init__(self, migrate_table: _Optional[_Union[Write.MessageMigrateTable, _Mapping]] = ..., insert: _Optional[_Union[Write.MessageInsert, _Mapping]] = ..., delete: _Optional[_Union[Write.MessageDeleteStale, _Mapping]] = ..., delete_record: _Optional[_Union[Write.MessageDeleteRecord, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class Transform(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("record",)
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("record",)
        RECORD_FIELD_NUMBER: _ClassVar[int]
        record: bytes
        def __init__(self, record: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class TransformSchema(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("schema",)
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        schema: bytes
        def __init__(self, schema: _Optional[bytes] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("schema",)
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        schema: bytes
        def __init__(self, schema: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class Close(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class TestConnection(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("spec",)
        SPEC_FIELD_NUMBER: _ClassVar[int]
        spec: bytes
        def __init__(self, spec: _Optional[bytes] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("success", "failure_code", "failure_description")
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
        FAILURE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        success: bool
        failure_code: str
        failure_description: str
        def __init__(self, success: bool = ..., failure_code: _Optional[str] = ..., failure_description: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
