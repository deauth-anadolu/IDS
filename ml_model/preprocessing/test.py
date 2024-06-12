import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Load CSV data into a pandas DataFrame
data = pd.read_csv("datasets/final.csv")


data = data[["frame.len", "wlan.fc.type", "wlan.fc.subtype", "Label"]]
# data = data.replace('?', np.nan)
# def label(value):
#     if value == "Deauth": return "1"
#     return "0"
# data["Label"] = data["Label"].apply(label)


# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# Create and train the Ridge regression model
ridge = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization strength
ridge.fit(X_train, y_train)

# Make predictions
ridge_predictions = ridge.predict(X_test)
print("---Ridor---")

# Evaluate the model
mse = mean_squared_error(y_test, ridge_predictions)
print("Mean Squared Error:", mse)

# Calculate accuracy (R^2 score) of the Ridge regression model
accuracy = ridge.score(X_test, y_test)
print("Accuracy (R^2 score):", accuracy)

from sklearn.metrics import confusion_matrix

# conf_matrix = confusion_matrix(y_test, ridge_predictions)
# TP = conf_matrix[1, 1]
# TN = conf_matrix[0, 0]
# FP = conf_matrix[0, 1]
# FN = conf_matrix[1, 0]

# print("True Positives (TP):", TP)
# print("True Negatives (TN):", TN)
# print("False Positives (FP):", FP)
# print("False Negatives (FN):", FN)

