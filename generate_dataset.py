import pyshark
from Client import Client
from Device import Device
from utils import *
import pandas as pd
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
FILTER = ""
# FILTER = "wlan.da == 88:66:a5:55:a2:d4"
# FILTER = "wlan.fc.type_subtype == 0x000c"
# FILTER = "wlan.fc.type_subtype == 0x000b || wlan.fc.type_subtype == 0x000c"
FILTER = "frame.number > 800000" # skip first 800000 frames
CAP = pyshark.FileCapture('/media/hsrv/data/1. Deauth.pcap', display_filter=FILTER, keep_packets=False)


print("IDS AWAKE!")
devices: list[Client] = []
new_data_list = []
def main():
    device = None
    
    for frame in CAP:
        print(f"I-> {frame.number}")
        print(is_deauth_attack(frame))

        try:
            da = get_da(frame)
            if da:
    
                if is_unknown_device(frame, devices):
                    device = Client(da, None, frame)
                    devices.append(device)
                else:
                    device = Device.find_device_by_mac(devices, da)

                if device:
                    device.last_frame = frame

                    new_row = {
                        'wlan.fc.type_subtype': int(frame.wlan.fc_type_subtype, 16),
                        'wlan.fc.type': int(frame.wlan.fc_type, 16),
                        'wlan.fc.protected': int(frame.wlan.fc_protected),

                        'time_difference': device.time_difference,
                        'num_of_deauth_frames': device.num_of_deauth_frames,

                        'Label': is_deauth_attack(frame)
                    }
                    
                    # Append the new row to a list
                    new_data_list.append(new_row)

        except Exception as e:
            print(e)

    # Convert the list to a DataFrame and write to CSV
    all_new_data = pd.DataFrame(new_data_list, columns=['wlan.fc.type_subtype', 'wlan.fc.type', 'wlan.fc.protected', 'time_difference', 'num_of_deauth_frames', 'Label'])
    all_new_data.to_csv('generated.csv', mode='w', index=False)


main()