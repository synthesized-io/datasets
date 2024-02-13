from enum import Enum as _Enum


class DType(str, _Enum):
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
