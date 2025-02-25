

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('synthetic_data.csv')

# Encode categorical columns with LabelEncoder
label_encoder = LabelEncoder()

# Assuming the categorical column is one of the features in the dataset
categorical_columns = data.select_dtypes(include=['object']).columns

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Split features (X) and target (y)
X = data.drop('Logic Depth', axis=1)  # Features
y = data['Logic Depth']  # Target variable

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize AdaBoost Regressor with default decision tree as base estimator
ada_model = AdaBoostRegressor(n_estimators=50, random_state=42)

# Train the model
ada_model.fit(X_train, y_train)

# Make predictions
y_pred = ada_model.predict(X_test)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"AdaBoost Model - MAE: {mae:.4f}")
