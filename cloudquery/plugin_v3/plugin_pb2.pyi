import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    class MessageError(_message.Message):
        __slots__ = ("table_name", "error")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        error: str
        def __init__(self, table_name: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
    class BackendOptions(_message.Message):
        __slots__ = ("table_name", "connection")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        connection: str
        def __init__(self, table_name: _Optional[str] = ..., connection: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ("tables", "skip_tables", "skip_dependent_tables", "deterministic_cq_id", "backend", "shard", "withErrorMessages")
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
        WITHERRORMESSAGES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        skip_tables: _containers.RepeatedScalarFieldContainer[str]
        skip_dependent_tables: bool
        deterministic_cq_id: bool
        backend: Sync.BackendOptions
        shard: Sync.Request.Shard
        withErrorMessages: bool
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., skip_tables: _Optional[_Iterable[str]] = ..., skip_dependent_tables: bool = ..., deterministic_cq_id: bool = ..., backend: _Optional[_Union[Sync.BackendOptions, _Mapping]] = ..., shard: _Optional[_Union[Sync.Request.Shard, _Mapping]] = ..., withErrorMessages: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("migrate_table", "insert", "delete_record", "error")
        MIGRATE_TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        DELETE_RECORD_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        migrate_table: Sync.MessageMigrateTable
        insert: Sync.MessageInsert
        delete_record: Sync.MessageDeleteRecord
        error: Sync.MessageError
        def __init__(self, migrate_table: _Optional[_Union[Sync.MessageMigrateTable, _Mapping]] = ..., insert: _Optional[_Union[Sync.MessageInsert, _Mapping]] = ..., delete_record: _Optional[_Union[Sync.MessageDeleteRecord, _Mapping]] = ..., error: _Optional[_Union[Sync.MessageError, _Mapping]] = ...) -> None: ...
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
        def __init__(self, table: _Optional[bytes] = ..., source_name: _Optional[str] = ..., sync_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., table_name: _Optional[str] = ...) -> None: ...
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

class AssessTables(_message.Message):
    __slots__ = ()
    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNKNOWN: _ClassVar[AssessTables.Category]
        CATEGORY_NO_CHANGE: _ClassVar[AssessTables.Category]
        CATEGORY_AUTOMATICALLY_MIGRATABLE: _ClassVar[AssessTables.Category]
        CATEGORY_MANUAL_MIGRATION_REQUIRED: _ClassVar[AssessTables.Category]
        CATEGORY_TABLE_REMOVED: _ClassVar[AssessTables.Category]
        CATEGORY_FILE_SCHEMA_CHANGED: _ClassVar[AssessTables.Category]
    CATEGORY_UNKNOWN: AssessTables.Category
    CATEGORY_NO_CHANGE: AssessTables.Category
    CATEGORY_AUTOMATICALLY_MIGRATABLE: AssessTables.Category
    CATEGORY_MANUAL_MIGRATION_REQUIRED: AssessTables.Category
    CATEGORY_TABLE_REMOVED: AssessTables.Category
    CATEGORY_FILE_SCHEMA_CHANGED: AssessTables.Category
    class TablePair(_message.Message):
        __slots__ = ("old_table", "new_table")
        OLD_TABLE_FIELD_NUMBER: _ClassVar[int]
        NEW_TABLE_FIELD_NUMBER: _ClassVar[int]
        old_table: bytes
        new_table: bytes
        def __init__(self, old_table: _Optional[bytes] = ..., new_table: _Optional[bytes] = ...) -> None: ...
    class Evidence(_message.Message):
        __slots__ = ("synthetic_value", "before", "after")
        SYNTHETIC_VALUE_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        synthetic_value: str
        before: str
        after: str
        def __init__(self, synthetic_value: _Optional[str] = ..., before: _Optional[str] = ..., after: _Optional[str] = ...) -> None: ...
    class ColumnFinding(_message.Message):
        __slots__ = ("column_name", "category", "old_type", "new_type", "safe_mode_behavior", "forced_mode_behavior", "evidence")
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        OLD_TYPE_FIELD_NUMBER: _ClassVar[int]
        NEW_TYPE_FIELD_NUMBER: _ClassVar[int]
        SAFE_MODE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        FORCED_MODE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        EVIDENCE_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        category: AssessTables.Category
        old_type: str
        new_type: str
        safe_mode_behavior: str
        forced_mode_behavior: str
        evidence: _containers.RepeatedCompositeFieldContainer[AssessTables.Evidence]
        def __init__(self, column_name: _Optional[str] = ..., category: _Optional[_Union[AssessTables.Category, str]] = ..., old_type: _Optional[str] = ..., new_type: _Optional[str] = ..., safe_mode_behavior: _Optional[str] = ..., forced_mode_behavior: _Optional[str] = ..., evidence: _Optional[_Iterable[_Union[AssessTables.Evidence, _Mapping]]] = ...) -> None: ...
    class TableFinding(_message.Message):
        __slots__ = ("table_name", "category", "safe_mode_behavior", "forced_mode_behavior", "columns", "evidence", "incomplete_coverage_reason")
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        SAFE_MODE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        FORCED_MODE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        EVIDENCE_FIELD_NUMBER: _ClassVar[int]
        INCOMPLETE_COVERAGE_REASON_FIELD_NUMBER: _ClassVar[int]
        table_name: str
        category: AssessTables.Category
        safe_mode_behavior: str
        forced_mode_behavior: str
        columns: _containers.RepeatedCompositeFieldContainer[AssessTables.ColumnFinding]
        evidence: _containers.RepeatedCompositeFieldContainer[AssessTables.Evidence]
        incomplete_coverage_reason: str
        def __init__(self, table_name: _Optional[str] = ..., category: _Optional[_Union[AssessTables.Category, str]] = ..., safe_mode_behavior: _Optional[str] = ..., forced_mode_behavior: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[AssessTables.ColumnFinding, _Mapping]]] = ..., evidence: _Optional[_Iterable[_Union[AssessTables.Evidence, _Mapping]]] = ..., incomplete_coverage_reason: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ("tables", "migrate_force")
        TABLES_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_FORCE_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedCompositeFieldContainer[AssessTables.TablePair]
        migrate_force: bool
        def __init__(self, tables: _Optional[_Iterable[_Union[AssessTables.TablePair, _Mapping]]] = ..., migrate_force: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("tables",)
        TABLES_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedCompositeFieldContainer[AssessTables.TableFinding]
        def __init__(self, tables: _Optional[_Iterable[_Union[AssessTables.TableFinding, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
