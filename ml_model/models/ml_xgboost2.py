# First XGBoost model for Pima Indians dataset
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# load data
data = pd.read_csv('datasets/transformed.csv')
# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)



print("---xgboost---")

print("Accuracy: %.2f%%" % (accuracy * 100.0))

TP = sum((y_test == 1) & (predictions == 1))
TN = sum((y_test == 0) & (predictions == 0))
FP = sum((y_test == 0) & (predictions == 1))
FN = sum((y_test == 1) & (predictions == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)


