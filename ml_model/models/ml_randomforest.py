# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import GridSearchCV
from imblearn.under_sampling import RandomUnderSampler

from joblib import dump

def plot_learning_curves(model, X, y, cv=5, n_jobs=None, train_sizes=np.linspace(0.1, 1.0, 10)):
    """
    Plots the learning curves for a given model and dataset.

    Parameters:
    - model: The machine learning model to use.
    - X: Feature dataset.
    - y: Target variable.
    - cv: Number of cross-validation folds.
    - n_jobs: Number of jobs to run in parallel. None means 1 unless in a joblib.parallel_backend context.
    - train_sizes: Relative or absolute numbers of training examples that will be used to generate the learning curve.
    """
    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes, scoring='accuracy')

    # Calculate mean and standard deviation for training set scores
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)

    # Calculate mean and standard deviation for test set scores
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(8, 5))
    plt.plot(train_sizes, train_mean, 'o-', color="r", label="Training score")
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color="r")
    plt.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-validation score")
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color="g")

    plt.title("Learning Curve")
    plt.xlabel("Training examples")
    plt.ylabel("Accuracy")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

def tune_model(X_train, y_train, X_test, y_test, param_grid, cv=5, scoring='accuracy', filename='best_random_forest_model.joblib'):
    """
    Tune a RandomForest model using GridSearchCV and save the best model.

    Parameters:
    - X_train: Training features.
    - y_train: Training target variable.
    - X_test: Test features.
    - y_test: Test target variable.
    - param_grid: Dictionary with parameters names (str) as keys and lists of parameter settings to try as values.
    - cv: Number of cross-validation folds.
    - scoring: Strategy to evaluate the performance of the cross-validated model on the test set.
    - filename: The filename for saving the model.
    """
    model = RandomForestClassifier(random_state=42, bootstrap=True)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv, scoring=scoring)
    grid_search.fit(X_train, y_train)

    # Best model
    best_model = grid_search.best_estimator_

    # Evaluate the best model on the test set
    y_test_pred = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print("Adjusted Model Accuracy:", test_accuracy)



    return best_model, test_accuracy

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/final2.csv')
# print(data.columns)
# columns = ['dns.time', 'frame.len', 'frame.time_delta',
#        'frame.time_epoch', 'radiotap.datarate', 'radiotap.dbm_antsignal',
#        'radiotap.length', 'radiotap.mactime', 'radiotap.present.tsft',
#        'udp.time_delta', 'udp.time_relative', 'wlan.duration', 'wlan.fc.ds', 'wlan.fc.frag', 'wlan.fc.moredata', 'wlan.fc.order',
#        'wlan.fc.protected', 'wlan.fc.pwrmgt', 'wlan.fc.retry',
#        'wlan.fc.subtype', 'wlan.fc.type', 'wlan_radio.data_rate', 'wlan_radio.duration', 'wlan_radio.phy']
# data = data.drop(columns=columns)
# print(data.columns)


# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# Encode categorical target variable if needed
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# # Parameters grid
# param_grid = {
#     'n_estimators': [100, 200, 300],  # More trees (try different values)
#     'max_depth': [10, 20, None],      # None means no limit
#     'min_samples_leaf': [1, 2, 4],    # Higher values
#     'min_samples_split': [2, 5, 10],  # Higher values
#     'max_features': ['auto', 'sqrt', 'log2']  # Different number of max features
# }

# Tune and save the model
# best_model, test_accuracy = tune_modell(X_train, y_train, X_test, y_test, param_grid)

# Plot learning curves
# plot_learning_curves(best_model, X_train, y_train)




# # Apply oversampling using RandomOverSampler
# oversampler = RandomOverSampler(sampling_strategy='auto', random_state=42)
# X_train_oversampled, y_train_oversampled = oversampler.fit_resample(X_train, y_train)

# # Apply undersampling using RandomUnderSampler
# undersampler = RandomUnderSampler(sampling_strategy='auto', random_state=42)
# X_train_undersampled, y_train_undersampled = undersampler.fit_resample(X_train, y_train)

# # Fit RandomForest classifier on the oversampled train set
# model_oversampled = RandomForestClassifier(random_state=42)
# model_oversampled.fit(X_train_oversampled, y_train_oversampled)

# # Fit RandomForest classifier on the undersampled train set
# model_undersampled = RandomForestClassifier(random_state=42)
# model_undersampled.fit(X_train_undersampled, y_train_undersampled)

# # Make predictions on test set
# y_test_pred_oversampled = model_oversampled.predict(X_test)
# y_test_pred_undersampled = model_undersampled.predict(X_test)

# # Calculate accuracy for oversampled and undersampled models
# accuracy_oversampled = accuracy_score(y_test, y_test_pred_oversampled)
# accuracy_undersampled = accuracy_score(y_test, y_test_pred_undersampled)

# # Calculate TP, TN, FP, FN for oversampled model
# TP_oversampled = sum((y_test == 1) & (y_test_pred_oversampled == 1))
# TN_oversampled = sum((y_test == 0) & (y_test_pred_oversampled == 0))
# FP_oversampled = sum((y_test == 0) & (y_test_pred_oversampled == 1))
# FN_oversampled = sum((y_test == 1) & (y_test_pred_oversampled == 0))

# # Calculate TP, TN, FP, FN for undersampled model
# TP_undersampled = sum((y_test == 1) & (y_test_pred_undersampled == 1))
# TN_undersampled = sum((y_test == 0) & (y_test_pred_undersampled == 0))
# FP_undersampled = sum((y_test == 0) & (y_test_pred_undersampled == 1))
# FN_undersampled = sum((y_test == 1) & (y_test_pred_undersampled == 0))

# # Print results
# print("Oversampled Model Accuracy:", accuracy_oversampled)
# print("Undersampled Model Accuracy:", accuracy_undersampled)
# print("Oversampled TP:", TP_oversampled, "TN:", TN_oversampled, "FP:", FP_oversampled, "FN:", FN_oversampled)
# print("Undersampled TP:", TP_undersampled, "TN:", TN_undersampled, "FP:", FP_undersampled, "FN:", FN_undersampled)

# # Plot learning curves for both models
# plot_learning_curves(model_oversampled, X_train_oversampled, y_train_oversampled)
# plot_learning_curves(model_undersampled, X_train_undersampled, y_train_undersampled)

print("---Random Forest---")

# Example 1: Random Forest Classifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print("Accuracy: ", rf_accuracy)
print(rf_classifier.score(X_train, y_train))


# cv_scores = cross_val_score(rf_classifier, X_train, y_train, cv=5)

# # Print the cross-validation scores
# print("Cross-Validation Scores:", cv_scores)

# # Print the average cross-validation score
# print("Average Cross-Validation Score:", cv_scores.mean())

TP = sum((y_test == 1) & (rf_predictions == 1))
TN = sum((y_test == 0) & (rf_predictions == 0))
FP = sum((y_test == 0) & (rf_predictions == 1))
FN = sum((y_test == 1) & (rf_predictions == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)


# Plot learning curves
# plot_learning_curves(rf_classifier, X_train, y_train)



# Save the model
filename = "randomforest.sav"
dump(rf_classifier, f"models/{filename}")
print(f"Model saved to {filename}")

