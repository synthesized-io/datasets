from ._datasets import _Dataset, _Tag

# Tabular
_Dataset("atlas_higgs_detection", "tabular/templates/atlas_higgs_detection.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("biased_data", "tabular/biased/biased_data.csv", [_Tag.FINANCE, _Tag.REGRESSION])
_Dataset("biased_data_mixed_types", "tabular/biased/biased_data_mixed_types.csv", [_Tag.FINANCE, _Tag.REGRESSION])
_Dataset("compas", "tabular/biased/compas.csv", [_Tag.REGRESSION])
_Dataset("autism", "tabular/health/autism.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("breast_cancer", "tabular/health/breast_cancer.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("healthcare", "tabular/health/healthcare.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("indian_liver_patient", "tabular/health/indian-liver-patient-dataset.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("parkinsons", "tabular/health/parkinsons.csv", [_Tag.HEALTHCARE])
_Dataset("retail_data_transactions", "tabular/insurance/retailer_data_transactions.csv", [_Tag.INSURANCE])
_Dataset("sweden_motor_insurance", "tabular/insurance/sweden_motor_insurance.csv", [_Tag.REGRESSION, _Tag.INSURANCE])
_Dataset("uk_insurance_claims_1", "tabular/insurance/uk_insurance_claims_1.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.INSURANCE])
_Dataset("uk_insurance_claims_2", "tabular/insurance/uk_insurance_claims_2.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.INSURANCE])
_Dataset("uk_land_register_transactions", "tabular/insurance/uk_land_register_transactions.csv", [_Tag.REGRESSION, _Tag.INSURANCE])
_Dataset("us_insurance_premiums", "tabular/insurance/us_insurance_premiums.csv", [_Tag.REGRESSION, _Tag.INSURANCE])
_Dataset("boston_housing_prices", "tabular/templates/boston_housing_prices.csv", [_Tag.REGRESSION])
_Dataset("churn_prediction", "tabular/templates/churn_prediction.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("claim_prediction", "tabular/templates/claim_prediction.csv", [_Tag.INSURANCE, _Tag.BINARY_CLASSIFICATION])
_Dataset("credit", "tabular/templates/credit.csv", [_Tag.CREDIT, _Tag.BINARY_CLASSIFICATION])
_Dataset("credit_with_categories", "tabular/templates/credit_with_categoricals.csv", [_Tag.CREDIT, _Tag.BINARY_CLASSIFICATION])
_Dataset("german_credit_data", "tabular/templates/german_credit_data.csv", [_Tag.CREDIT, _Tag.REGRESSION])
_Dataset("segmentation_analysis", "tabular/templates/segmentation_analysis.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("telecom_churn", "tabular/templates/telecom-churn.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("vehicle_insurance", "tabular/templates/vehicle-insurance.csv", [_Tag.INSURANCE])

# Timeseries
_Dataset("air_quality", "time-series/air-quality.csv", [_Tag.TIME_SERIES])
_Dataset("bitcoin_price", "time-series/bitcoin_price.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("brent_oil_prices", "time-series/brent-oil-prices.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("occupancy_data", "time-series/occupancy-data.csv", [_Tag.TIME_SERIES])
_Dataset("s&p500_5yr", "time-series/sandp500_5yr.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("simple_fraud", "time-series/fraud-time-series.csv", [_Tag.FRAUD, _Tag.BINARY_CLASSIFICATION])
_Dataset("noaa_isd_weather_additional_dtypes_small", "time-series/NoaaIsdWeather_added_dtypes_small.csv", [_Tag.TIME_SERIES])
_Dataset("noaa_isd_weather_additional_dtypes_medium", "time-series/NoaaIsdWeather_added_dtypes_medium.csv", [_Tag.TIME_SERIES])

from ._datasets import *
