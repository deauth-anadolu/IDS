import shap
import pandas as pd
from sklearn.model_selection import train_test_split


# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/clean5.csv')



# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Train the Lasso model again if needed
lasso.fit(X_train, y_train)

# Initialize the SHAP explainer with the trained Lasso model
explainer = shap.Explainer(lasso, X_train)
shap_values = explainer(X_test)

# Plot the SHAP values for a single prediction
shap.plots.waterfall(shap_values[0])

# Summarize the SHAP values for all predictions
shap.summary_plot(shap_values, X_test)
