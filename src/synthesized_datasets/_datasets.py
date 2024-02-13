import os as _os
import sys as _sys
import typing as _ty
from enum import Enum as _Enum

import pandas as _pd
import pyspark.sql as _ps
import yaml as _yaml
from pyspark import SparkFiles as _SparkFiles

from ._dtypes import _PD_DTYPE_MAP
from ._dtypes import DType as _DType
from ._dtypes import create_pyspark_schema as _create_pyspark_schema

# _ROOT_GITHUB_URL = "https://raw.githubusercontent.com/synthesized-io/datasets/master/"
_ROOT_GITHUB_URL = ""


class _Tag(_Enum):
    ALL = "all"
    CREDIT = "credit"
    INSURANCE = "insurance"
    FRAUD = "fraud"
    HEALTHCARE = "healthcare"
    BINARY_CLASSIFICATION = "binary_classification"
    CHURN = "churn"
    REGRESSION = "regression"
    TIME_SERIES = "time_series"
    FINANCE = "finance"
    GEOSPATIAL = "geospatial"

    def __repr__(self):
        return f"<{self.value}>"


class _Dataset:
    def __init__(
        self,
        name: str,
        url: str,
        schema: _ty.Mapping[str, _DType],
        tags: _ty.Optional[_ty.List[_Tag]] = None,
        date_format: _ty.Optional[str] = None,
    ):
        self._name = name
        self._url = (
            url
            if url.startswith("https://storage.googleapis.com")
            else _ROOT_GITHUB_URL + url
        )
        self._tags: _ty.List[_Tag] = tags if tags is not None else []
        self._schema = schema
        self._date_format = date_format

        _REGISTRIES[_Tag.ALL]._register(self)
        for tag in self._tags:
            _REGISTRIES[tag]._register(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def tags(self) -> _ty.List[_Tag]:
        return self._tags

    def load(self) -> _pd.DataFrame:
        """Loads the dataset."""
        if self.url.endswith("parquet"):
            df = _pd.read_parquet(self.url)
        else:
            # CSV load is the default
            dtypes = {
                col: (
                    _PD_DTYPE_MAP[dtype]
                    if dtype
                    not in [
                        _DType.DATETIME,
                        _DType.TIMEDELTA,
                        _DType.DATE,
                        _DType.TIME,
                    ]
                    else "string"
                )
                for col, dtype in self._schema.items()
            }
            df = _pd.read_csv(self.url, dtype=dtypes)
            for col, dtype in self._schema.items():
                if dtype is [_DType.DATETIME, _DType.DATE]:
                    df[col] = _pd.to_datetime(df[col], dayfirst=True)
                if dtype in [_DType.TIMEDELTA, _DType.TIME]:
                    df[col] = _pd.to_timedelta(df[col])
        df.attrs["name"] = self.name
        return df

    def load_spark(self, spark: _ty.Optional[_ps.SparkSession] = None) -> _ps.DataFrame:
        """Loads the dataset as a Spark DataFrame."""

        if spark is None:
            spark = _ps.SparkSession.builder.getOrCreate()

        schema = _create_pyspark_schema(self._schema)
        spark.sparkContext.addFile(self.url)
        _, filename = _os.path.split(self.url)
        if self.url.endswith("parquet"):
            df = spark.read.parquet(_SparkFiles.get(filename))
        else:
            # CSV load is the default
            df = spark.read.csv(
                _SparkFiles.get(filename),
                header=True,
                schema=schema,
                enforceSchema=False,
                dateFormat=self._date_format,
            )
        df.name = self.name
        return df

    def __repr__(self):
        return f"<Dataset: {self.url}>"

    def _to_dict(self):
        params = {
            "name": self.name,
            "url": (
                self.url[len(_ROOT_GITHUB_URL) :]
                if self.url.startswith(_ROOT_GITHUB_URL)
                else self.url
            ),
            "schema": [{key: value.value} for key, value in self._schema.items()],
            "tags": [tag.value for tag in self.tags],
        }
        if self._date_format is not None:
            params["date_format"] = self._date_format

        return params

    @classmethod
    def _from_dict(cls, d):
        return _Dataset(
            name=d["name"],
            url=d["url"],
            date_format=d.get("date_format"),
            schema={
                next(elem.keys().__iter__()): _DType(next(elem.values().__iter__()))
                for elem in d["schema"]
            },
            tags=[_Tag(tag) for tag in d["tags"]],
        )

    def _to_yaml(self):
        return _yaml.dump(self._to_dict(), indent=2)


class _Registry:
    def __init__(self, tag: _Tag):
        self._tag = tag
        self._datasets: _ty.MutableMapping[str, _Dataset] = {}

    def _register(self, dataset: _Dataset):
        if self._tag not in dataset.tags and self._tag != _Tag.ALL:
            raise ValueError(f"_Dataset {dataset.name} is not tagged with {self._tag}")

        if dataset.name not in self._datasets:
            self._datasets[dataset.name] = dataset
            setattr(self, dataset.name, dataset)


_REGISTRIES: _ty.MutableMapping[_Tag, _Registry] = {}

for _tag in _Tag:
    _registry = _Registry(_tag)
    _REGISTRIES[_tag] = _registry
    setattr(_sys.modules[__name__], _tag.name, _registry)
