import pyarrow as pa
from cloudquery.plugin_v3.arrow import schemas_to_bytes, new_schemas_from_bytes, record_to_bytes, new_record_from_bytes

def test_schema_round_trip():
    sc = pa.schema(fields=[pa.field("a", pa.int64())], metadata={"foo":"bar", "baz":"quux"})
    b = schemas_to_bytes([sc])
    schemas = new_schemas_from_bytes(b)
    assert len(schemas) == 1
    assert schemas[0].equals(sc)

def test_record_round_trip():
  sc = pa.schema(fields=[pa.field("a", pa.int64())], metadata={"foo":"bar", "baz":"quux"})
  rec = pa.RecordBatch.from_arrays([pa.array([1,2,3])], schema=sc)
  b = record_to_bytes(rec)
  rec2 = new_record_from_bytes(b)
  assert rec.equals(rec2)
