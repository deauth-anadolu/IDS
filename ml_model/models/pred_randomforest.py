import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from sklearn.model_selection import train_test_split 


def load_dataset(filename):

    # Load CSV data into a pandas DataFrame
    data = pd.read_csv(f"datasets/{filename}")

    # Assuming the last column is the target variable and the rest are features
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1]   # Target variable

    # Encode categorical target variable if needed
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    return X_train, X_test, y_train, y_test



def predict(row):

    filename = "randomforest.sav"
    model = joblib.load(f"models/{filename}")

    return model.predict(row)




# filename = "randomforest.sav"
# model = joblib.load(f"models/{filename}")


# X_train, X_test, y_train, y_test  = load_dataset("final.csv")
# # evaluate model 
# y_predict = model.predict(X_test)
# print("X TEST-----------------------")
# print(X_test.iloc[0])
# print("-----------------X TEST")

# print(y_predict)

# # check results
# print(classification_report(y_test, y_predict)) 

# TP = sum((y_test == 1) & (y_predict == 1))
# TN = sum((y_test == 0) & (y_predict == 0))
# FP = sum((y_test == 0) & (y_predict == 1))
# FN = sum((y_test == 1) & (y_predict == 0))

# print("True Positives (TP):", TP)
# print("True Negatives (TN):", TN)
# print("False Positives (FP):", FP)
# print("False Negatives (FN):", FN)







