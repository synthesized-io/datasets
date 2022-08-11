from ._datasets import _Dataset, _Tag

_Dataset("atlas_higgs_detection", "tabular/templates/atlas_higgs_detection.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("breast_cancer", "tabular/health/breast_cancer.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("boston_housing_prices", "tabular/templates/boston_housing_prices.csv", [_Tag.REGRESSION])
_Dataset("churn_prediction", "tabular/templates/churn_prediction.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("claim_prediction", "tabular/templates/claim_prediction.csv", [_Tag.INSURANCE, _Tag.BINARY_CLASSIFICATION])
_Dataset("credit", "tabular/templates/credit.csv", [_Tag.CREDIT, _Tag.BINARY_CLASSIFICATION])
_Dataset("german_credit_data", "tabular/templates/german_credit_data.csv", [_Tag.CREDIT, _Tag.REGRESSION])
_Dataset("indian_liver_patient", "tabular/health/indian-liver-patient-dataset.csv", [_Tag.BINARY_CLASSIFICATION, _Tag.HEALTHCARE])
_Dataset("segmentation_analysis", "tabular/templates/segmentation_analysis.csv", [_Tag.BINARY_CLASSIFICATION])
_Dataset("simple_fraud", "time-series/fraud-time-series.csv", [_Tag.FRAUD, _Tag.BINARY_CLASSIFICATION])
_Dataset("telecom_churn", "tabular/templates/telecom-churn.csv", [_Tag.CHURN, _Tag.BINARY_CLASSIFICATION])
_Dataset("vehicle_insurance", "tabular/templates/vehicle-insurance.csv", [_Tag.INSURANCE])

from ._datasets import *
