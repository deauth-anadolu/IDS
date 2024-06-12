import pyshark
from Client import Client
from Device import Device
from AccessPoint import AccessPoint
from Detector import Detector
from utils import *
from parallel import attribute_functions
import threading
import pandas as pd
import csv
from datetime import datetime
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
FILTER = ""
# FILTER = "wlan.da == 88:66:a5:55:a2:d4"
# CAP = pyshark.FileCapture('/media/hsrv/data/1. Deauth.pcap', display_filter=FILTER)

print("IDS AWAKE!")

devices: list[Device] = []
detector = Detector(f"randomforest.sav")
base_aps = list[AccessPoint]

def main():
    device = None
    capture = pyshark.LiveCapture(interface='wlp3s0mon', display_filter=None)
    
    # Create the CSV file with the starting timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{DIR}/outputs/{timestamp}.csv"
    
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["MAC", "Signal Power", "GeoLocation", "Attack", "Date"])
        
        for frame in capture:
            try:
                # data = {
                #     'frame.len': [frame.frame_info.len],
                #     'wlan.fc.subtype': [int(frame.wlan.fc_type_subtype, 16)],
                #     'wlan.fc.type': [frame.wlan.fc_type]
                # }
                data = {
                    'frame.len': [86],
                    'wlan.fc.subtype': [12],
                    'wlan.fc.type': [0]
                }
                data = pd.DataFrame(data)
                pred = detector.predict_attack(data)

                da = get_da(frame)
                if da:
                    dbms = get_singal_dbms(frame)
                    if is_unknown_device(frame, devices):
                        device = Device(da, dbms)
                        devices.append(device)
                    else:
                        device = Device.find_device_by_mac(devices, da)

                    if device:
                        device.dbms = dbms
                        if pred == 1:
                            device.under_attack = 1
                            print("Deauth Attack!")
                        else:
                            device.under_attack = 0
                            print("Normal.")
                        
                        device.timestamp = frame.frame_info.time
                        device.set_geo_location()
                        post_output_to_adminpanel(device.output_info)
                        device.append_to_csv(csv_writer)
                        
                        print(device)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
