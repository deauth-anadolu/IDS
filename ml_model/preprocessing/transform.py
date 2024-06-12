import pandas as pd
import numpy as np

data = pd.read_csv("datasets/missing_filled.csv")

def radiotap_dbm_antisignal(value):
    vals = str(value).split("-")
    sum = 0
    for v in vals:
        if v.isnumeric():
            sum += -1 * int(v)

    return sum / len(vals)

def wlan_fc_ds(value):
    if value == "0x00000000": return 1
    return 0

def radiotap_present_tsft(value):
    if value == "1-0-0": return 1
    return 0

def is_missing(value):
    if value == -1: return 1
    return 0

def label(value):
    if value == "Deauth": return "1"
    return "0"


data["Label"] = data["Label"].apply(label)
data["radiotap.dbm_antsignal"] = data["radiotap.dbm_antsignal"].apply(radiotap_dbm_antisignal)
data["wlan.fc.ds"]= data["wlan.fc.ds"].apply(wlan_fc_ds)
data["radiotap.present.tsft"] = data["radiotap.present.tsft"].apply(radiotap_present_tsft)
data["data.len"] = data["data.len"].apply(is_missing)
data["udp.time_relative"] = data["udp.time_relative"].apply(is_missing)
data["udp.time_delta"] = data["udp.time_delta"].apply(is_missing)

data.to_csv("datasets/transformed.csv", index=False)