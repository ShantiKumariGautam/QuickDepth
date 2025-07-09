import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error


data = pd.read_csv('synthetic_data.csv')


X = data.drop(['Logic Depth', 'Gate Type'], axis=1) 
y = data['Logic Depth']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


ridge_model = Ridge()


ridge_model.fit(X_train, y_train)


y_pred = ridge_model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
print(f'Ridge Regression Model - MAE: {mae}')
