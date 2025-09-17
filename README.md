Fraud Detection Project

Credit Card Fraud Detection using Machine Learning (EDA, SMOTE, Random Forest, XGBoost)

Project Overview

This project focuses on detecting fraudulent credit card transactions using machine learning.
It includes:

Exploratory Data Analysis (EDA)

Handling imbalanced datasets with SMOTE

Building and comparing ML models: Logistic Regression, Random Forest, XGBoost

Generating visualizations and ROC curves

Saving reports and cleaned notebooks for reproducibility

Dataset

Source: Kaggle – Credit Card Fraud Detection

Shape: 284,807 rows × 31 columns

Features: V1–V28 (PCA transformed), Time, Amount, Class (0 = Normal, 1 = Fraud)

Class distribution:

Class	Count
0	284,315
1	492
Project Structure
fraud_detection_project/
│
├── data/                 # Raw and processed datasets
│   └── Data.py           # Script to download and clean dataset
│
├── notebooks/            # Jupyter notebooks
│   ├── 01_eda_github.ipynb
│   └── 02_modeling_github.ipynb
│
├── reports/              # Generated plots, ROC curves, and PDFs
│   └── roc_curves.png
│
├── src/                  # Optional Python scripts for modeling
│
├── requirements.txt      # Project dependencies
└── README.md             # Project overview

Key Steps
1. Data Loading

Load dataset from Kaggle using kagglehub

Clean and preprocess data (handle missing values, scale features)

2. Exploratory Data Analysis (EDA)

Visualize distributions and correlations

Check for class imbalance and fraud patterns

3. Data Preprocessing

Split dataset into train and test sets

Scale features using StandardScaler

Apply SMOTE to balance classes

4. Modeling

Models used:

Logistic Regression

Random Forest Classifier

XGBoost Classifier

Evaluate using:

Confusion Matrix

Classification Report

ROC-AUC and ROC Curve Comparison

5. Feature Importance

Identify top predictors from Random Forest and XGBoost models

6. Visualization

Correlation Heatmaps

ROC Curves

Fraud distribution plots

Usage

Clone this repository:

git clone https://github.com/pawan935/fraud_detection_project.git


Navigate to project folder:

cd fraud_detection_project


Create virtual environment and install dependencies:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


Run scripts or notebooks:

# Run Data download script
python data/Data.py

# Open notebooks
jupyter notebook notebooks/01_eda_github.ipynb
jupyter notebook notebooks/02_modeling_github.ipynb

Technologies & Tools

Python (3.13)

Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Imbalanced-learn, Seaborn, Matplotlib

Jupyter Notebook

GitHub for version control

Results

Balanced dataset after SMOTE

Random Forest and XGBoost achieved high ROC-AUC scores

Visualizations saved in reports/ folder for reporting

Author

Pawan – GitHub
