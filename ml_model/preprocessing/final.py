import pandas as pd


data = pd.read_csv("datasets/transformed.csv")

# columns = ['data.len', 'frame.len', 'wlan.fc.subtype', 'wlan.fc.type', 'Label']
columns = ['frame.len', 'wlan.fc.subtype', 'wlan.fc.type', 'Label']

data = data[columns]

data.to_csv("datasets/final2.csv", index=False)

