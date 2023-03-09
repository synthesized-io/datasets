from ._datasets import _Dataset, _Tag

# Tabular
_Dataset("biased_data", "tabular/biased/biased_data.csv", [_Tag.FINANCE, _Tag.REGRESSION])
_Dataset("biased_data_mixed_types", "tabular/biased/biased_data_mixed_types.csv", [_Tag.FINANCE, _Tag.REGRESSION])
_Dataset("compas", "tabular/biased/compas.csv", [_Tag.REGRESSION])

_Dataset("uk_libraries", "tabular/geolocation_data/UK_libraries.csv", [_Tag.GEOSPATIAL])
_Dataset("uk_open_pubs", "tabular/geolocation_data/UK_open_pubs.csv", [_Tag.GEOSPATIAL])
_Dataset("uk_schools_list", "tabular/geolocation_data/UK_schools_list.csv", [_Tag.GEOSPATIAL])

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

_Dataset("adult", "tabular/templates/adult.csv", [_Tag.REGRESSION])
_Dataset("atlas_higgs_detection", "tabular/templates/atlas_higgs_detection.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("boston_housing_prices", "tabular/templates/boston_housing_prices.csv", [_Tag.REGRESSION])
_Dataset("churn_prediction", "tabular/templates/churn_prediction.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("claim_prediction", "tabular/templates/claim_prediction.csv", [_Tag.INSURANCE, _Tag.BINARY_CLASSIFICATION])
_Dataset("credit", "tabular/templates/credit.csv", [_Tag.CREDIT, _Tag.BINARY_CLASSIFICATION])
_Dataset("credit_with_categories", "tabular/templates/credit_with_categoricals.csv", [_Tag.CREDIT, _Tag.BINARY_CLASSIFICATION])
_Dataset("fire_peril", "tabular/templates/fire-peril.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.INSURANCE])
_Dataset("german_credit_data", "tabular/templates/german_credit_data.csv", [_Tag.CREDIT, _Tag.REGRESSION])
_Dataset("homesite_quote_conversion", "tabular/templates/homesite-quote-conversion.csv", [_Tag.GEOSPATIAL])
_Dataset("life_insurance", "tabular/templates/life-insurance.csv", [_Tag.INSURANCE])
_Dataset("noshowappointments", "tabular/templates/noshowappointments.csv", [_Tag.HEALTHCARE, _Tag.BINARY_CLASSIFICATION])
_Dataset("price_paid_household", "tabular/templates/price_paid_household.csv", [_Tag.REGRESSION])
_Dataset("sales_pipeline", "tabular/templates/sales_pipeline.csv", [_Tag.REGRESSION])
_Dataset("segmentation_analysis", "tabular/templates/segmentation_analysis.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("telecom_churn", "tabular/templates/telecom-churn.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("telecom_churn_large", "tabular/templates/telecom-churn-large.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("titanic", "tabular/templates/titanic.csv", [_Tag.REGRESSION])
_Dataset("vehicle_insurance", "tabular/templates/vehicle-insurance.csv", [_Tag.INSURANCE])

_Dataset("bank_marketing1", "tabular/uci/bank_marketing1.csv", [_Tag.REGRESSION, _Tag.FINANCE])
_Dataset("bank_marketing2", "tabular/uci/bank_marketing2.csv", [_Tag.REGRESSION, _Tag.FINANCE])
_Dataset("creditcard_default", "tabular/uci/creditcard_default.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.FINANCE, _Tag.INSURANCE])
_Dataset("onlinenews_popularity", "tabular/uci/onlinenews_popularity.csv", [_Tag.REGRESSION, _Tag.TIME_SERIES])
_Dataset("wine_quality-red", "tabular/uci/wine_quality-red.csv", [_Tag.REGRESSION])
_Dataset("wine_quality-white", "tabular/uci/wine_quality-white.csv", [_Tag.REGRESSION])


# Timeseries
_Dataset("air_quality", "time-series/air-quality.csv", [_Tag.TIME_SERIES])
_Dataset("bitcoin_price", "time-series/bitcoin_price.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("brent_oil_prices", "time-series/brent-oil-prices.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("simple_fraud", "time-series/fraud-time-series.csv", [_Tag.FRAUD, _Tag.BINARY_CLASSIFICATION])
_Dataset("household_power_consumption_small", "time-series/household_power_consumption_small.csv", [_Tag.TIME_SERIES])
_Dataset("mock_medical_data", "time-series/mock_medical_data.csv", [_Tag.HEALTHCARE, _Tag.TIME_SERIES])
_Dataset("noaa_isd_weather_additional_dtypes_small", "time-series/NoaaIsdWeather_added_dtypes_small.csv", [_Tag.TIME_SERIES])
_Dataset("noaa_isd_weather_additional_dtypes_medium", "time-series/NoaaIsdWeather_added_dtypes_medium.csv", [_Tag.TIME_SERIES])
_Dataset("occupancy_data", "time-series/occupancy-data.csv", [_Tag.TIME_SERIES])
_Dataset("s_and_p_500_5yr", "time-series/sandp500_5yr.csv", [_Tag.FINANCE, _Tag.TIME_SERIES])
_Dataset("time_series_basic", "time-series/time_series_basic.csv", [_Tag.TIME_SERIES])
_Dataset("transactions", "time-series/transactions.csv", [_Tag.TIME_SERIES])
_Dataset("transactions_sample_10k", "time-series/transactions_sample_10k.csv", [_Tag.TIME_SERIES])

from ._datasets import *
