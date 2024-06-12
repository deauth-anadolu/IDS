# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/final.csv')

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


TP = sum((y_test == 1) & (ridge_predictions == 1))
TN = sum((y_test == 0) & (ridge_predictions == 0))
FP = sum((y_test == 0) & (ridge_predictions == 1))
FN = sum((y_test == 1) & (ridge_predictions == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)

# Convert y_train_pred_original to match the type of y_train
y_train_pred_original = y_train_pred_original.astype(int)

# Now you can use accuracy_score without the mix of binary and continuous targets error
print("Accuracy on Original Train Set:", accuracy_score(y_train, y_train_pred_original))
print("False Negatives (FN):", FN)