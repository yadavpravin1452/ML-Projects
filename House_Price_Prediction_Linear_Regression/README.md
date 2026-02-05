# House Price Prediction using Linear Regression

This project focuses on predicting house prices using a Linear Regression model.
The goal is to understand the complete machine learning workflow starting from
data understanding to model evaluation, using only numeric features.


## Project Overview

- Problem Type: Regression
- Algorithm Used: Linear Regression
- Target Variable: SalePrice
- Dataset Size: 2919 records, 13 features

This project is built as a learning-focused ML project with clear steps
and clean structure.


## Project Structure

House_Price_Prediction_Linear_Regression/
├── data/
│   └── HousePricePrediction.xlsx
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_linear_regression_sklearn.ipynb
│   └── 05_gradient_descent_from_scratch.ipynb
├── results/
│   └── metrics.txt
├── README.md
└── requirements.txt


## Dataset Description

The dataset contains information about residential houses.
Only numeric features were used for the initial model.

Target Variable:
- SalePrice

Selected Features:
- TotalBsmtSF
- YearBuilt
- YearRemodAdd
- LotArea
- OverallCond


## Exploratory Data Analysis

- SalePrice distribution is right-skewed with several high-value outliers
- Basement size and construction year show moderate correlation with SalePrice
- LotArea shows weak correlation with SalePrice
- Feature selection was done based on correlation analysis and domain sense


## Data Cleaning & Feature Selection

- Dropped non-informative column: Id
- Handled missing values using mean or row removal
- Selected numeric features only for baseline model
- Categorical features were excluded in this phase



## Model Used

- Linear Regression (scikit-learn)

Train-Test Split:
- Training: 80%
- Testing: 20%

Evaluation Metrics:
- RMSE (Root Mean Squared Error)
- R² Score



## Model Performance

- RMSE: 57388.71
- R² Score: 0.5706

This model serves as a baseline regression model.
Performance is limited due to linear assumptions and exclusion of categorical features.


## Tools & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook