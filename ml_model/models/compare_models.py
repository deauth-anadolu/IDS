import os
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

from sklearn.svm import SVC


# Load CSV data into a pandas DataFrame
filename = "final"
data = pd.read_csv(f"datasets/{filename}.csv")

print(data.columns)
# columns = ['dns.time',  'frame.time_delta',
#        'frame.time_epoch', 'radiotap.datarate', 'radiotap.dbm_antsignal',
#        'radiotap.length', 'radiotap.mactime', 'radiotap.present.tsft',
#        'udp.time_delta', 'udp.time_relative', 'wlan.duration', 'wlan.fc.frag', 'wlan.fc.moredata', 'wlan.fc.order',
#        'wlan.fc.protected', 'wlan.fc.pwrmgt', 'wlan.fc.retry',
#        'wlan_radio.data_rate', 'wlan_radio.duration', 'wlan_radio.phy', 'wlan.fc.ds',
#        ]
# data = data.drop(columns=columns)
data = data.drop(columns=["data.len"])

print(data.columns)

# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# scaler = StandardScaler()

# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)


# Apply oversampling using RandomOverSampler
oversampler = RandomOverSampler(sampling_strategy='auto', random_state=42)
X_train_oversampled, y_train_oversampled = oversampler.fit_resample(X_train, y_train)

# Apply undersampling using RandomUnderSampler
undersampler = RandomUnderSampler(sampling_strategy='auto', random_state=42)
X_train_undersampled, y_train_undersampled = undersampler.fit_resample(X_train, y_train)

model_original = Ridge(alpha=1.0)
model_original.fit(X_train, y_train)


# Fit KNN classifier on the oversampled train set
model_oversampled =  Ridge(alpha=1.0)
model_oversampled.fit(X_train_oversampled, y_train_oversampled)

# Fit KNN classifier on the undersampled train set
model_undersampled =  Ridge(alpha=1.0)
model_undersampled.fit(X_train_undersampled, y_train_undersampled)

# Make predictions on train sets
y_train_pred_original = model_original.predict(X_train)
y_train_pred_oversampled = model_oversampled.predict(X_train_oversampled)
y_train_pred_undersampled = model_undersampled.predict(X_train_undersampled)

# Make predictions on test sets
y_test_pred_original = model_original.predict(X_test)
y_test_pred_oversampled = model_oversampled.predict(X_test)
y_test_pred_undersampled = model_undersampled.predict(X_test)



print(f"DATASET: {filename}")

# Calculate and print TP, TN, FP, FN for each train set
TP_train_original = sum((y_train == 1) & (y_train_pred_original == 1))
TN_train_original = sum((y_train == 0) & (y_train_pred_original == 0))
FP_train_original = sum((y_train == 0) & (y_train_pred_original == 1))
FN_train_original = sum((y_train == 1) & (y_train_pred_original == 0))
print("Accuracy on Original Train Set:", accuracy_score(y_train, y_train_pred_original))
print("Original Train Set - TP:", TP_train_original, "TN:", TN_train_original, "FP:", FP_train_original, "FN:", FN_train_original)

TP_train_oversampled = sum((y_train_oversampled == 1) & (y_train_pred_oversampled == 1))
TN_train_oversampled = sum((y_train_oversampled == 0) & (y_train_pred_oversampled == 0))
FP_train_oversampled = sum((y_train_oversampled == 0) & (y_train_pred_oversampled == 1))
FN_train_oversampled = sum((y_train_oversampled == 1) & (y_train_pred_oversampled == 0))
print("Accuracy on Oversampled Train Set:", accuracy_score(y_train_oversampled, y_train_pred_oversampled))
print("Oversampled Train Set - TP:", TP_train_oversampled, "TN:", TN_train_oversampled, "FP:", FP_train_oversampled, "FN:", FN_train_oversampled)

TP_train_undersampled = sum((y_train_undersampled == 1) & (y_train_pred_undersampled == 1))
TN_train_undersampled = sum((y_train_undersampled == 0) & (y_train_pred_undersampled == 0))
FP_train_undersampled = sum((y_train_undersampled == 0) & (y_train_pred_undersampled == 1))
FN_train_undersampled = sum((y_train_undersampled == 1) & (y_train_pred_undersampled == 0))
print("Accuracy on Undersampled Train Set:", accuracy_score(y_train_undersampled, y_train_pred_undersampled))
print("Undersampled Train Set - TP:", TP_train_undersampled, "TN:", TN_train_undersampled, "FP:", FP_train_undersampled, "FN:", FN_train_undersampled)

# Calculate and print TP, TN, FP, FN for each test set
TP_test_original = sum((y_test == 1) & (y_test_pred_original == 1))
TN_test_original = sum((y_test == 0) & (y_test_pred_original == 0))
FP_test_original = sum((y_test == 0) & (y_test_pred_original == 1))
FN_test_original = sum((y_test == 1) & (y_test_pred_original == 0))
print("\nAccuracy on Original Test Set:", accuracy_score(y_test, y_test_pred_original))
print("Original Test Set - TP:", TP_test_original, "TN:", TN_test_original, "FP:", FP_test_original, "FN:", FN_test_original)

TP_test_oversampled = sum((y_test == 1) & (y_test_pred_oversampled == 1))
TN_test_oversampled = sum((y_test == 0) & (y_test_pred_oversampled == 0))
FP_test_oversampled = sum((y_test == 0) & (y_test_pred_oversampled == 1))
FN_test_oversampled = sum((y_test == 1) & (y_test_pred_oversampled == 0))
print("Accuracy on Oversampled Test Set:", accuracy_score(y_test, y_test_pred_oversampled))
print("Oversampled Test Set - TP:", TP_test_oversampled, "TN:", TN_test_oversampled, "FP:", FP_test_oversampled, "FN:", FN_test_oversampled)

TP_test_undersampled = sum((y_test == 1) & (y_test_pred_undersampled == 1))
TN_test_undersampled = sum((y_test == 0) & (y_test_pred_undersampled == 0))
FP_test_undersampled = sum((y_test == 0) & (y_test_pred_undersampled == 1))
FN_test_undersampled = sum((y_test == 1) & (y_test_pred_undersampled == 0))
print("Accuracy on Undersampled Test Set:", accuracy_score(y_test, y_test_pred_undersampled))
print("Undersampled Test Set - TP:", TP_test_undersampled, "TN:", TN_test_undersampled, "FP:", FP_test_undersampled, "FN:", FN_test_undersampled)







# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
# Dynamically retrieve the model name
model_name = type(model_original).__name__ 

# Create a DataFrame to store the results
results = pd.DataFrame({
    "Date": [current_date] * 6,  # Repeat the date for each row
    "Model": [model_name] * 6,   # Repeat the dynamically retrieved model name for each row
    "Dataset": [filename] * 6,   # Repeat the filename for each row
    "Set": ["Original Train", "Oversampled Train", "Undersampled Train", "Original Test", "Oversampled Test", "Undersampled Test"],
    "TP": [TP_train_original, TP_train_oversampled, TP_train_undersampled, TP_test_original, TP_test_oversampled, TP_test_undersampled],
    "TN": [TN_train_original, TN_train_oversampled, TN_train_undersampled, TN_test_original, TN_test_oversampled, TN_test_undersampled],
    "FP": [FP_train_original, FP_train_oversampled, FP_train_undersampled, FP_test_original, FP_test_oversampled, FP_test_undersampled],
    "FN": [FN_train_original, FN_train_oversampled, FN_train_undersampled, FN_test_original, FN_test_oversampled, FN_test_undersampled],
    "Accuracy": [
        accuracy_score(y_train, y_train_pred_original),
        accuracy_score(y_train_oversampled, y_train_pred_oversampled),
        accuracy_score(y_train_undersampled, y_train_pred_undersampled),
        accuracy_score(y_test, y_test_pred_original),
        accuracy_score(y_test, y_test_pred_oversampled),
        accuracy_score(y_test, y_test_pred_undersampled)
    ]
})


# Save the DataFrame to a CSV file
results.to_csv(f"models/model_compare.csv", mode='a', header=not os.path.exists(f"models/model_compare.csv"), index=False)

