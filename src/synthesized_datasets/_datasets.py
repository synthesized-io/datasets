from enum import Enum as _Enum
import typing as _typing 
import pandas as _pd
import sys as _sys

_ROOT_URL = "https://raw.githubusercontent.com/synthesized-io/datasets/master/"


class _Tag(_Enum):
    CREDIT = "credit"
    INSURANCE = "insurance"
    FRAUD = "fraud"
    BINARY_CLASSIFICATION = "binary_classification"
    CHURN = "churn"
    REGRESSION = "regression"

    def __repr__(self):
        return f"<{self.value}>"


class _Dataset:

    def __init__(self, name: str , url: str, tags: _typing.List[_Tag] = None):
        self._name = name
        self._url = _ROOT_URL + url
        self._tags: _typing.List[str] = tags if tags is not None else []
        for tag in self._tags:
            _REGISTRIES[tag]._register(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def tags(self) -> _typing.List[str]:
        return self._tags

    def load(self) -> _pd.DataFrame:
        """Loads the dataset."""
        return _pd.read_csv(self.url)

    def __repr__(self):
        return f"<Dataset: {self.url}>"


class _Registry:
    def __init__(self, tag: _Tag):
            self._tag = tag
            self._datasets: _typing.Mapping[str, _Dataset] = {}
    
    def _register(self, dataset: _Dataset):
        if self._tag not in dataset.tags:
            raise ValueError(f"_Dataset {dataset.name} is not tagged with {self._tag}")
        
        if dataset.name not in self._datasets:
            self._datasets[dataset.name] = dataset
            setattr(self, dataset.name, dataset)

_REGISTRIES: _typing.Mapping[_Tag, _Registry] = {}

for _tag in _Tag:
    _registry = _Registry(_tag)
    _REGISTRIES[_tag] = _registry
    setattr(_sys.modules[__name__], _tag.name, _registry)
