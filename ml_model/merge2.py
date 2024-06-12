import pandas as pd
import os


# CSV dosyasını yükle
# df = pd.read_csv("/media/hsrv/data/awid3_csv/1.Deauth/Deauth_0.csv")

# # "Label" sütununda "Deauth" veya "Normal" dışındaki satırları filtrele
# df = df[(df['Label'] == 'Deauth') | (df['Label'] == 'Normal')]


# df = df.dropna(axis=1, how='all')

# print(df)


# Path to directory containing CSV files
directory = '/media/hsrv/data/awid3_csv/1.Deauth/'
# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
def fo(s: str): return int(s.split("_")[-1][:-4])
csv_files.sort(key=fo)


# İlk dosyayı yükle
merged_df = pd.read_csv(os.path.join(directory, csv_files[0]))

# İlk dosyanın sonrasındaki dosyaları birleştir
for file_name in csv_files[1:]:
    # Dosyayı yükle, ilk satırı atla
    df = pd.read_csv(os.path.join(directory, file_name), skiprows=1)
    # DataFrameleri birleştir
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Birleştirilmiş DataFrame'i göster
print(merged_df)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv(os.path.join(directory, 'merged.csv'), index=False)