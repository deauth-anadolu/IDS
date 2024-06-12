
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/final.csv')

# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
# X = data[['frame.time_delta', 'radiotap.datarate', 'radiotap.mactime', 'radiotap.present.tsft', 'tcp.ack', 'udp.time_relative']]
y = data.iloc[:, -1]   # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the SVM model
svm_classifier = SVC(kernel='rbf', C=1.0, gamma='scale')  
# You can adjust the kernel, C (regularization parameter), and gamma
svm_classifier.fit(X_train, y_train)

# Make predictions
svm_predictions = svm_classifier.predict(X_test)


print("---SVM---")

# Evaluate the model
accuracy = accuracy_score(y_test, svm_predictions)
print(accuracy)


TP = sum((y_test == 1) & (svm_predictions == 1))
TN = sum((y_test == 0) & (svm_predictions == 0))
FP = sum((y_test == 0) & (svm_predictions == 1))
FN = sum((y_test == 1) & (svm_predictions == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)