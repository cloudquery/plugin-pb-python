from pyarrow import ipc
import pyarrow as pa
from typing import List

def schema_to_bytes(sc) -> bytes:
    """
    Convert a schema to bytes
    """
    sink = pa.BufferOutputStream()
    try:
      with pa.ipc.new_stream(sink, sc) as writer:
          pass
      return sink.getvalue().to_pybytes()
    finally:
      sink.close()

def new_schema_from_bytes(buf: bytes) -> pa.Schema:
    """
    Convert bytes to schema
    """
    schema = None
    with pa.ipc.open_stream(buf) as reader:
      schema = reader.schema
    return schema

def schemas_to_bytes(schemas: List[pa.Schema]):
  res : List[bytes] = []
  for schema in schemas:
    res.append(schema_to_bytes(schema))
  return res

def new_schemas_from_bytes(bufs: List[bytes]) -> List[pa.Schema]:
  res : List[pa.Schema] = []
  for buf in bufs:
    res.append(new_schema_from_bytes(buf))
  return res

def record_to_bytes(rec: pa.RecordBatch) -> bytes:
  sink = pa.BufferOutputStream()
  try:
    with pa.ipc.new_stream(sink, rec.schema) as writer:
        writer.write_batch(rec)
    return sink.getvalue().to_pybytes()
  finally:
    sink.close()

def new_record_from_bytes(buf :bytes) -> pa.RecordBatch:
  rec = None
  with pa.ipc.open_stream(buf) as reader:
    rec = reader.read_next_batch()
  return rec
