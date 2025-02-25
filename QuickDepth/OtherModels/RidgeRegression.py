import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

# Load your dataset
data = pd.read_csv('synthetic_data.csv')

# Define the feature columns and target column
X = data.drop(['Logic Depth', 'Gate Type'], axis=1)  # Dropping target column and non-numeric feature column
y = data['Logic Depth']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Ridge regression model
ridge_model = Ridge()

# Train the model
ridge_model.fit(X_train, y_train)

# Predict on the test set
y_pred = ridge_model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Ridge Regression Model - MAE: {mae}')
