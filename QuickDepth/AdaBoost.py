

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('synthetic_data.csv')


label_encoder = LabelEncoder()


categorical_columns = data.select_dtypes(include=['object']).columns

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])


X = data.drop('Logic Depth', axis=1)  
y = data['Logic Depth']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


ada_model = AdaBoostRegressor(n_estimators=50, random_state=42)


ada_model.fit(X_train, y_train)


y_pred = ada_model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
print(f"AdaBoost Model - MAE: {mae:.4f}")
