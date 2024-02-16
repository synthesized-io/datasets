import pytest

import synthesized_datasets as data

dataset_names = list(data.ALL._datasets.keys())
dataset_names.sort()


@pytest.fixture(params=dataset_names)
def dataset(request):
    dataset_name = request.param
    if dataset_name in ["noaa_isd_weather_additional_dtypes_100gb", "simple_fraud_5gb"]:
        pytest.skip("This dataset is too large to be tested")
    return getattr(data.ALL, dataset_name)


def test_pandas_dataset(dataset):
    df = dataset.load()
    assert not df.isna().all().any()
    assert not (df.dtypes == "object").any()
    assert "Unnamed: 0" not in df.columns


def test_spark_dataset(dataset):
    df = dataset.load_spark()

    assert not df.toPandas().isna().all().any()
