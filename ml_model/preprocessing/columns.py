import numpy as np
import pandas as pd


data = pd.read_csv('datasets/clean5.csv')

columns = [
    'wlan.ssid',
    'tcp.ack',
    'tcp.ack_raw',
    'tcp.checksum',
    'tcp.checksum.status',
    'tcp.seq',
    'tcp.seq_raw',
    'tcp.srcport',
    'tcp.time_delta',
    'tcp.time_relative'
]

data.drop(columns=columns, inplace=True)

data.to_csv('datasets/clean6.csv', index=False)

