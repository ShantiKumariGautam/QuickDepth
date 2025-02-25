# XGBoost Model
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error

# Load the dataset
data = pd.read_csv('synthetic_data.csv')

# Preprocessing
X = data[['Fan-In', 'Fan-Out', 'Total Gate Count', 'Critical Path']]  # Features
y = data['Logic Depth']  # Target

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize and train the XGBoost model
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=10, learning_rate=0.1)
xgb_model.fit(X_train, y_train)

# Make predictions
xgb_predictions = xgb_model.predict(X_test)

# Calculate Mean Absolute Error
xgb_mae = mean_absolute_error(y_test, xgb_predictions)
print(f"XGBoost Model - MAE: {xgb_mae}")
