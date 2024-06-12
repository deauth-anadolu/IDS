import pandas as pd
import numpy as np

data = pd.read_csv("datasets/corr_10.csv")


# data['dns.time'] = data['dns.time'].fillna(-1)
# data['radiotap.datarate'] = data['radiotap.datarate'].fillna(-1)
# data['radiotap.mactime'] = data['radiotap.mactime'].fillna(-1)
# data['data.len'] = data['data.len'].fillna(-1)
# data['wlan.tag.length'] = data['wlan.tag.length'].fillna(-1)

data = data.replace('?', -1)
data.to_csv("datasets/missing_filled.csv", index=False)






# data["radiotap.dbm_antsignal"].apply(radiotap_dbm_antisignal, meta=("radiotap.dbm_antsignal", int))


