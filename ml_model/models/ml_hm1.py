from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

# Load data from CSV file
data = pd.read_csv("datasets/final.csv")


# Separate features and target variable
features = data.drop("Label", axis=1)
target = data["Label"]

# Create a MinMaxScaler object (adjust range if needed)
scaler = MinMaxScaler(feature_range=(0, 1))

# Scale the features
features = scaler.fit_transform(features)

# Create and train the Bayes Net classifier
model = MultinomialNB()
model.fit(features, target)

# Make predictions on unseen data
predictions = model.predict(features)

# Calculate accuracy
accuracy = accuracy_score(target, predictions)
print("Accuracy:", accuracy)

# Get confusion matrix
confusion_matrix = confusion_matrix(target, predictions)

# Extract true positives, true negatives, false positives, and false negatives
tp = confusion_matrix[1, 1]
tn = confusion_matrix[0, 0]
fp = confusion_matrix[0, 1]
fn = confusion_matrix[1, 0]

print("True Positives (TP):", tp)
print("True Negatives (TN):", tn)
print("False Positives (FP):", fp)
print("False Negatives (FN):", fn)
