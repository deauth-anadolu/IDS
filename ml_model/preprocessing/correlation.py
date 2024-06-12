import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


# korelasyonu bu değerden büyük eşit olanlar elenecek..
# THRESHOLD = 0.8
# THRESHOLD = 0.999999999999999
# THRESHOLD = 0.9999999999
# THRESHOLD = 0.99999
THRESHOLD = 1.0
# THRESHOLD = 1.0



# Load CSV data into a pandas DataFrame
data = pd.read_csv('datasets/clean6.csv')





# # Convert all columns to numeric, coercing errors to NaN
# for col in data.columns:
#     data[col] = pd.to_numeric(data[col], errors='coerce')


# # Drop columns that couldn't be converted to numeric (still have NaN after conversion)
# # data.dropna(axis=1, how='all', inplace=True)
# # Drop rows where any value is NaN, except in the 'Label' column
# data.dropna(axis=0, how='any', subset=[col for col in data.columns if col != 'Label'], inplace=True)

# # Print the number of NaNs in each column except 'Label'
# print(data.drop(columns=['Label']).isnull().sum())

# print(data)
# Compute the correlation matrix
# correlation_matrix = data.corr()





# # Korelasyonu 1 olan özellikleri bul
# correlation_pairs = []
# m = []
# # Korelasyon matrisinin üst üçgensinde dolaş
# for i in range(len(correlation_matrix.columns)):
#     for j in range(i+1, len(correlation_matrix.columns)):
#         aux = correlation_matrix.iloc[i, j]
#         if aux.item() >= THRESHOLD:
#             if correlation_matrix.columns[i] not in m:
#                 m.append(correlation_matrix.columns[i])
#             if correlation_matrix.columns[j] not in m:
#                 m.append(correlation_matrix.columns[j])
#             correlation_pairs.append((correlation_matrix.columns[i], correlation_matrix.columns[j]))

# # # Korelasyonu 1 olan özellikleri yazdır
# # for pair in correlation_pairs:
# #     print("{}, {}".format(pair[0], pair[1]))

# # print(len(correlation_pairs))

# # Plot the correlation matrix heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
# plt.title('Correlation Matrix Heatmap')
# plt.show()

correlation_pairs = [
("wlan_radio.end_tsf", "wlan_radio.timestamp"),
("radiotap.mactime", "wlan_radio.timestamp"),
("radiotap.mactime", "wlan_radio.end_tsf"),
("frame.time_delta", "frame.time_delta_displayed"),
("wlan_radio.start_tsf", "wlan_radio.timestamp"),
("wlan_radio.end_tsf", "wlan_radio.start_tsf"),
("radiotap.mactime", "wlan_radio.start_tsf"),
("frame.time_relative", "radiotap.timestamp.ts"),
("frame.time_epoch", "radiotap.timestamp.ts"),
("frame.time_epoch", "frame.time_relative"),
]

m = []
for pair in correlation_pairs:
    if pair[0] not in m:
        m.append(pair[0])
    if pair[1] not in m:
        m.append(pair[1])


def make_unique(pairs):
    aux = dict()
    for pair in pairs:
        aux.setdefault(pair[0], []).append(pair[1])


    return aux

pairs_dict = make_unique(correlation_pairs)
# print(pairs_dict)
def delete(pairs_dict: dict):
    for key, val in pairs_dict.copy().items():
        for v in val:
            try:
                del pairs_dict[v]
            except: ...
delete(pairs_dict)


# print(f"Korelasyonu 1 olanların teke indirgenmiş hali (artık korelasyonları 1 değil): {list(pairs_dict.keys())}")

keys = list(pairs_dict.keys())
# keys.append("Label")



z = data.columns
x = keys

news = []
def substract_list():
    # z - m + x
    aux = sorted(list(set(z) - set(m) | set(x)))
    if "Label" in aux:
        aux.remove("Label")
    aux.append("Label")

    return aux


news = substract_list()
news.remove("arp")
news.remove("udp.length")
news.remove("wlan.tag.length")
news.remove("wlan_radio.signal_dbm")

file_name = f"corr_{str(THRESHOLD).replace('.', '')}"
print(f"THRESHOLD: {THRESHOLD}")
print(f"Num of attributes: {len(news)}")
print(news)
print(file_name)

data = data[news]
file_name = "corr_10"
data.to_csv(f"datasets/{file_name}.csv", index=False)

