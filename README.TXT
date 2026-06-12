# Heart Disease Exploratory Data Analysis (EDA)

## Project Overview

This project performs Data Cleaning, Data Processing, Statistical Analysis, and Exploratory Data Analysis (EDA) on a Heart Disease dataset using Python.

The goal of the project is to understand the dataset, identify important features associated with heart disease, detect patterns, and generate insights using visualization and statistical methods.

---

## Dataset Information

- Dataset: Heart Disease Dataset
- Total Records: 1025
- Features: 14
- Target Variable:
  - 0 = No Heart Disease
  - 1 = Heart Disease

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- SciPy

---

## Project Workflow

### 1. Data Loading

- Imported dataset using Pandas.
- Examined dataset structure using:
  - shape()
  - head()
  - info()
  - describe()

### 2. Data Cleaning

- Checked for missing values.
- Identified duplicate records.
- Removed duplicate rows from the dataset.

### 3. Exploratory Data Analysis (EDA)

Performed various visualizations including:

#### Target Distribution
- Count plot of heart disease cases.

#### Age Distribution
- Histogram with KDE curve.

#### Cholesterol Distribution
- Histogram with KDE curve.

#### Resting Blood Pressure Distribution
- Histogram with KDE curve.

#### Outlier Detection
- Boxplots for:
  - Cholesterol
  - Resting Blood Pressure

#### Correlation Analysis
- Correlation Heatmap for all features.

#### Feature Relationships
- Age vs Heart Disease
- Maximum Heart Rate vs Heart Disease
- Chest Pain Type vs Heart Disease

#### Pair Plot
- Visualized relationships between important numerical variables.

---

## Feature Scaling

Applied StandardScaler on numerical features:

- age
- trestbps
- chol
- thalach
- oldpeak

---

## Statistical Analysis

### Pearson Correlation

Calculated correlation between numerical features and target variable:

- age
- trestbps
- chol
- thalach
- oldpeak

### Chi-Square Test

Performed Chi-Square Test of Independence on categorical features:

- sex
- cp
- fbs
- restecg
- exang
- slope
- ca
- thal

Features with p-value < 0.05 were considered statistically significant.

---

## Key Findings

- No missing values were present in the dataset.
- Duplicate records were identified and removed.
- Chest Pain Type (cp) showed a strong relationship with heart disease.
- Exercise-Induced Angina (exang) was significantly associated with heart disease.
- Maximum Heart Rate (thalach) showed positive correlation with the target variable.
- Several categorical features were found statistically significant using the Chi-Square Test.

---

## Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Statistical Analysis
- Feature Engineering
- Correlation Analysis
- Hypothesis Testing
- Python Programming

---

## Project Structure

```
Heart-Disease-EDA/
│
├── heart.csv
├── heart_disease_eda.py
├── README.md
└── requirements.txt
```

---

## How to Run

### Install Dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy
```

### Run Project

```bash
python heart_disease_eda.py
```

---

## Author

Vardhan Karri

GitHub: https://github.com/your-github-username

---

## Future Improvements

- Build Machine Learning Models
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Feature Selection
- Model Evaluation
- Prediction Dashboard using Streamlit