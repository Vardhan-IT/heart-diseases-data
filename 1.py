import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('heart.csv')
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.columns)
print(data['target'].value_counts())
print("Duplicate Rows:", data.duplicated().sum())
data = data.drop_duplicates()
print("Shape after removing duplicates:", data.shape)
print(data.dtypes)
plt.figure(figsize=(5,4))
sb.countplot(x='target', data=data)
plt.title('Target Distribution')
plt.show()
plt.figure(figsize=(6,4))
sb.histplot(data['age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()
plt.figure(figsize=(6,4))
sb.histplot(data['chol'], bins=20, kde=True)
plt.title('Cholesterol Distribution')
plt.show()
plt.figure(figsize=(6,4))
sb.histplot(data['trestbps'], bins=20, kde=True)
plt.title('Resting Blood Pressure Distribution')
plt.show()
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sb.boxplot(y=data['chol'])
plt.title('Cholesterol')
plt.subplot(1,2,2)
sb.boxplot(y=data['trestbps'])
plt.title('Blood Pressure')
plt.show()
plt.figure(figsize=(12,8))
sb.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
corr = data.corr()['target'].sort_values(ascending=False)
print(corr)
plt.figure(figsize=(6,4))
sb.boxplot(x='target', y='age', data=data)
plt.title('Age vs Heart Disease')
plt.show()
plt.figure(figsize=(6,4))
sb.boxplot(x='target', y='thalach', data=data)
plt.title('Maximum Heart Rate vs Heart Disease')
plt.show()
plt.figure(figsize=(6,4))
sb.countplot(x='cp', hue='target', data=data)
plt.title('Chest Pain Type vs Target')
plt.show()
cols = ['age','trestbps','chol','thalach','target'] 
sb.pairplot(data[cols], hue='target')
plt.show()
num_cols = ['age','trestbps','chol','thalach','oldpeak']
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])
print(data.head())
from scipy.stats import pearsonr
selected_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']       
correlations = {feature: pearsonr(data[feature], data['target'])[0] for feature in selected_features   }
correlations_d = pd.DataFrame.from_dict(list(correlations.items()), columns=['feature', 'correlation_with_target'])
print(correlations_d)
from scipy.stats import chi2_contingency
categorical_features = [
    'sex', 'cp', 'fbs', 'restecg',
    'exang', 'slope', 'ca', 'thal'
]
chi2_results = []
for feature in categorical_features:
    contingency_table = pd.crosstab(data[feature], data['target'])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    chi2_results.append({
        'Feature': feature,
        'Chi2 Statistic': round(chi2, 4),
        'P-value': round(p, 6)
    })
chi2_df = pd.DataFrame(chi2_results)
print("\nChi-Square Test Results")
print(chi2_df)
print("\nSignificant Features (p < 0.05)")
print(chi2_df[chi2_df['P-value'] < 0.05])