import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('synthetic_data.csv')
data = data.dropna()

X = data[['Fan-In', 'Fan-Out', 'Total Gate Count', 'Critical Path']]
y = data['Logic Depth']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svr_model = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_model.fit(X_train_scaled, y_train)

y_pred = svr_model.predict(X_test_scaled)

mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (SVR): {mae}')
