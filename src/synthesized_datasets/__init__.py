import os as _os

import yaml as _yaml

from ._datasets import _Dataset

_DATASETS_YAML = _os.path.join(_os.path.dirname(__file__), "datasets.yaml")


with open(_DATASETS_YAML, "r", encoding="utf-8") as _f:
    for _d in _yaml.full_load_all(_f):
        _Dataset._from_dict(_d)


from ._datasets import *
