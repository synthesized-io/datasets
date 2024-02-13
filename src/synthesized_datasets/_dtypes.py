from enum import Enum

import pyspark.sql.types as st


class DType(str, Enum):
    """Class to define the internal dtypes that can be handled."""

    BOOL = "bool"
    NULLABLE_BOOL = "boolean"
    DATETIME = "datetime64[ns]"
    DATE = "date"
    FLOAT = "float32"
    DOUBLE = "float64"
    INTEGER = "int32"
    LONG = "int64"
    NULLABLE_LONG = "Int64"
    STRING = "string"
    TIMEDELTA = "timedelta64[ns]"


def create_pyspark_schema(schema: dict[str, DType]) -> st.StructType:
    """Creates a PySpark schema from a dictionary of column names and d"""
    return st.StructType(
        [
            st.StructField(name, _PS_DTYPE_MAP[dtype], _PS_NULLABLE_MAP[dtype])
            for name, dtype in schema.items()
        ]
    )


_PS_DTYPE_MAP = {
    DType.BOOL: st.BooleanType(),
    DType.NULLABLE_BOOL: st.BooleanType(),
    DType.DATETIME: st.TimestampType(),
    DType.DATE: st.DateType(),
    DType.FLOAT: st.FloatType(),
    DType.DOUBLE: st.DoubleType(),
    DType.INTEGER: st.IntegerType(),
    DType.LONG: st.LongType(),
    DType.NULLABLE_LONG: st.FloatType(),
    DType.STRING: st.StringType(),
    DType.TIMEDELTA: st.LongType(),
}

_PS_NULLABLE_MAP = {
    DType.BOOL: False,
    DType.NULLABLE_BOOL: True,
    DType.DATETIME: False,
    DType.DATE: False,
    DType.FLOAT: False,
    DType.DOUBLE: False,
    DType.INTEGER: False,
    DType.LONG: False,
    DType.NULLABLE_LONG: True,
    DType.STRING: True,
    DType.TIMEDELTA: False,
}
