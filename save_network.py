import pyshark

from utils import *
import csv
from datetime import datetime
import pathlib

#NETWORKNAME = "BAHADDIN_GAZI_KYK"
NETWORKNAME = "KBU_MUHENDISLIK"
DIR = pathlib.Path(__file__).parent.resolve()

print("IDS AWAKE! - Network Saver Mode")

def main():
    capture = pyshark.LiveCapture(interface='wlp3s0mon', display_filter=None)
    
    # Create the CSV file with the starting timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    filename = f"{DIR}/networks/{NETWORKNAME}_{timestamp}.csv"
    
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["frame.wlan.ta", "frame.len", "wlan.fc.subtype", "wlan.fc.type", "wlan.fc.ds"])
        
        for frame in capture:
            data = []
            try:
                data = [
                    frame.wlan.ta,
                    frame.frame_info.len,
                    # int(frame.wlan.fc_type_subtype, 16),
                    frame.wlan.fc_type_subtype,
                    frame.wlan.fc_type,
                    frame.wlan.fc_ds,
                ]
                
                print(data)
                csv_writer.writerow(data)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
