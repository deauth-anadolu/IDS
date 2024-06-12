import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.utils.class_weight import compute_class_weight

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/transformed.csv')

# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# Encode categorical target variable if needed
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Compute class weights
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)

svc_classifier_weighted = SVC(class_weight={0: class_weights[0], 1: class_weights[1]})
svc_classifier_weighted.fit(X_train, y_train)
svc_predictions_weighted = svc_classifier_weighted.predict(X_test)
svc_accuracy_weighted = accuracy_score(y_test, svc_predictions_weighted)

print("---SVC---")

print(svc_accuracy_weighted)

# Confusion matrix for weighted SVC
TP_weighted = sum((y_test == 1) & (svc_predictions_weighted == 1))
TN_weighted = sum((y_test == 0) & (svc_predictions_weighted == 0))
FP_weighted = sum((y_test == 0) & (svc_predictions_weighted == 1))
FN_weighted = sum((y_test == 1) & (svc_predictions_weighted == 0))

print("True Positives (TP) - Weighted:", TP_weighted)
print("True Negatives (TN) - Weighted:", TN_weighted)
print("False Positives (FP) - Weighted:", FP_weighted)
print("False Negatives (FN) - Weighted:", FN_weighted)
