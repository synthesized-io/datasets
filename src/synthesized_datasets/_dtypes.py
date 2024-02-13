from enum import Enum

import pyspark.sql.types as st


class DType(str, Enum):
    """Class to define the internal dtypes that can be handled."""

    BOOL = "bool"
    NULLABLE_BOOL = "bool?"
    DATETIME = "datetime"
    DATE = "date"
    FLOAT = "float"
    DOUBLE = "double"
    INTEGER = "int"
    LONG = "long"
    NULLABLE_LONG = "long?"
    STRING = "string"
    TIMEDELTA = "timedelta"
    TIME = "time"


def create_pandas_schema(schema: dict[str, DType]) -> dict[str, str]:
    """Creates a PySpark schema from a dictionary of column names and d"""
    return {name: _PD_DTYPE_MAP[dtype] for name, dtype in schema.items()}


def create_pyspark_schema(schema: dict[str, DType]) -> st.StructType:
    """Creates a PySpark schema from a dictionary of column names and d"""
    return st.StructType(
        [
            st.StructField(name, _PS_DTYPE_MAP[dtype], _PS_NULLABLE_MAP[dtype])
            for name, dtype in schema.items()
        ]
    )


_PD_DTYPE_MAP = {
    DType.BOOL: "bool",
    DType.NULLABLE_BOOL: "boolean",
    DType.DATETIME: "datetime64[ns]",
    DType.DATE: "datetime64[ns]",
    DType.FLOAT: "float32",
    DType.DOUBLE: "float64",
    DType.INTEGER: "int32",
    DType.LONG: "int64",
    DType.NULLABLE_LONG: "Int64",
    DType.STRING: "string",
    DType.TIMEDELTA: "timedelta64[ns]",
    DType.TIME: "timedelta64[ns]",
}


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
    DType.TIMEDELTA: st.StringType(),
    DType.TIME: st.DayTimeIntervalType(1, 3),
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
    DType.TIMEDELTA: True,
    DType.TIME: True,
}
