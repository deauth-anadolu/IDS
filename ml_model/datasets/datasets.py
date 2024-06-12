import os
import pandas as pd

# Path to the datasets folder
datasets_path = 'datasets/'

# List all files in the datasets directory
dataset_files = os.listdir(datasets_path)

def count_classes(dataset_files):
    # Loop through each file and count the class labels
    for file in dataset_files:
        if file.endswith('.csv'):
            data_path = os.path.join(datasets_path, file)
            data = pd.read_csv(data_path, )
            # Assuming the last column is the target variable
            target = data.iloc[:, -1]
            count_1 = sum(target == 1)
            count_0 = sum(target == 0)
            print(f"File: {file}")
            print(f"Count of class '1': {count_1}")
            print(f"Count of class '0': {count_0}")
            print("----------")


def count_attributes(dataset_files):
    datas = {}
    for file in dataset_files:
        
        if file.endswith('.csv'):
            data_path = os.path.join(datasets_path, file)
            datas[file] = pd.read_csv(data_path)

    for file, data in sorted(datas.items()):
        print(f"{file} - {len(data.columns)}")


# count_classes(dataset_files)
count_attributes(dataset_files)

