# model_trainer.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# 1. Load data
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
           'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv('pima-indians-diabetes.data.csv', header=None, names=columns)

# 2. Replace 0s with NaN where appropriate
cols_with_zero_as_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero_as_missing] = df[cols_with_zero_as_missing].replace(0, np.nan)

# 3. Drop rows with missing values
df.dropna(inplace=True)

# 4. Split data
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Save the model
joblib.dump(model, "diabetes_model.pkl")
print("✅ Model trained and saved as 'diabetes_model.pkl'")
