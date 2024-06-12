import pandas as pd
import os

# Path to directory containing CSV files
directory = '/media/hsrv/data/awid3_csv/1.Deauth/'
# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
def fo(s: str): return int(s.split("_")[-1][:-4])
csv_files.sort(key=fo)

# Specify columns to delete
df = pd.read_csv(os.path.join(directory, csv_files[25]))
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
columns = df.head(0)
print(columns)


c = ...
first = pd.read_csv(os.path.join(directory, csv_files[0]))
# print(first.head(0))
delete_columns = [col for col in first if col not in columns]
# print(delete_columns)
# for f in csv_files:
#     df = pd.read_csv(os.path.join(directory, f))
#     df.drop(columns=)
#     if c not in columns:
# #     ...
# # # Initialize a DataFrame with the first CSV file after deleting specified columns
# merged_df = pd.read_csv(os.path.join(directory, csv_files[0]))
# merged_df.drop(columns=columns_to_delete, inplace=True)

# # Loop through remaining CSV files, delete specified columns, and merge them
# for file in csv_files[1:]:
#     df = pd.read_csv(os.path.join(directory, file))
#     df.drop(columns=columns_to_delete, inplace=True)  # Delete specified columns
#     merged_df = pd.concat([merged_df, df], ignore_index=True)

# # Write the merged DataFrame to a new CSV file
# merged_df.to_csv(os.path.join(directory, 'merged.csv'), index=False)