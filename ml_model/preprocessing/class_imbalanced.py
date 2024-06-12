import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/clean5.csv')

# Assuming the last column is the target variable
target_column = data.columns[-1]

# Count the number of instances in each class
class_distribution = data[target_column].value_counts()

# Plot the class distribution
plt.figure(figsize=(8, 6))
class_distribution.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Class Distribution')
plt.xlabel('Class')
plt.ylabel('Number of Instances')
plt.xticks(rotation=0)
plt.show()