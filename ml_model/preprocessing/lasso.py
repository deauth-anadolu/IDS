import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Sample data
data = pd.read_csv('datasets/corr_10.csv')

# Assume the last column is the target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the Lasso model
lasso = Lasso(alpha=1.0)  # alpha is the regularization strength
lasso.fit(X_train, y_train)

# Predict and evaluate
y_pred = lasso.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Print the coefficients
print("Lasso Coefficients:", lasso.coef_)