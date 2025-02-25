import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('synthetic_data.csv')  # Ensure this is the correct file path

# Data Preprocessing (if needed)
data = data.dropna()  # Remove any missing values if present

# Feature engineering (you may need to adjust these depending on your dataset)
X = data[['Fan-In', 'Fan-Out', 'Total Gate Count', 'Critical Path']]  # Features
y = data['Logic Depth']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Feature scaling (SVR often performs better with scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the SVR model
svr_model = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = svr_model.predict(X_test_scaled)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (SVR): {mae}')
