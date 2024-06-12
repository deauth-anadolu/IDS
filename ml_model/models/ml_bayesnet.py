# Import necessary libraries
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/final.csv')
print(data.columns)
# Assuming the last column is the target variable and the rest are features

X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print([(str(c), "Label") for c in X.columns])
# Create a Bayesian Network model
model = BayesianNetwork([(X.columns[i], 'Label') for i in range(len(X.columns))])  # Define the edges between features and target

# Explicitly specify state names for the label variable
label_states = y.unique().tolist()

# Estimate the parameters of the model using Bayesian Estimator
model.fit(X_train, estimator=BayesianEstimator)

# Make predictions
inference = VariableElimination(model)
y_pred = []
for index, row in X_test.iterrows():
    query = inference.map_query(variables=['Label'], evidence=row.to_dict())
    y_pred.append(query['Label'])


print("---BayesNet---")

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

TP = sum((y_test == 1) & (y_pred == 1))
TN = sum((y_test == 0) & (y_pred == 0))
FP = sum((y_test == 0) & (y_pred == 1))
FN = sum((y_test == 1) & (y_pred == 0))

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)
