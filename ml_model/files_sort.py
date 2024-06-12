import pandas as pd
import os

# Path to directory containing CSV files
directory = '/media/hsrv/data/awid3_csv/1.Deauth/'
# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
def fo(s: str): return int(s.split("_")[-1][:-4])
csv_files.sort(key=fo)

