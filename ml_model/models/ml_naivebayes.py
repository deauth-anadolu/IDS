# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler



# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/final.csv')


data = data.drop(columns=["data.len"])
data = data.drop(columns=["frame.len"])
data = data.drop(columns=["wlan.fc.type"])


print(data.columns)
# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# print(X[:100])
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
# print(X[:100])


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Create and train the Naive Bayes model
naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(X_train, y_train)

# Make predictions
naive_bayes_predictions = naive_bayes_classifier.predict(X_test)



print("---Naive Bayes---")

# Evaluate the model
accuracy = accuracy_score(y_test, naive_bayes_predictions)
print("Accuracy:", accuracy)


TP = sum((y_test == 1) & (naive_bayes_predictions == 1))
TN = sum((y_test == 0) & (naive_bayes_predictions == 0))
FP = sum((y_test == 0) & (naive_bayes_predictions == 1))
FN = sum((y_test == 1) & (naive_bayes_predictions == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)