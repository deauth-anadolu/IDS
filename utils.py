from datetime import datetime
import json
from pyshark.packet.packet import Packet
import pyshark
from Device import Device

import requests


def calc_percentage(cap_len, frame_num):
    return float((int(frame_num) * 100) / int(cap_len))

def live_capture():
    capture = pyshark.LiveCapture(interface='wlp3s0', display_filter=None)
    for frame in capture.sniff_continuously():
        yield frame

def calc_cap_len(cap):
    cap_len = 0
    for _ in cap: cap_len += 1
    return cap_len

def get_frame_time(frame: Packet):
    time_stamp = frame.frame_info.time # type: ignore
    return datetime.strptime((time_stamp.rsplit(' ', 1)[0])[:-3], '%b %d, %Y %H:%M:%S.%f')

def is_frame_auth(frame: Packet) -> bool:
    try:
        is_auth = frame.wlan.fc_subtpye == "0x000b"
        is_success = frame.layers[-1].wlan_fixed_status_code == "0x0000"
        
        return is_auth and is_success
    except:
        return False

def is_frame_deauth(frame: Packet) -> bool:
    try:
        is_deauth = frame.wlan.fc_subtype == "0x000c"
        return is_deauth
    except:
        return False

def is_unknown_device(frame: Packet, devices: list[Device]):
    da = get_da(frame)
    if any(d.mac == da for d in devices):
        return False
    return da

def get_da(frame: Packet):
    return frame.layers[2].da
def get_sa(frame: Packet):
    return frame.layers[2].sa

def is_ap(mac: None):
    return False


def get_singal_dbms(frame: Packet):
    dbms = frame.wlan_radio.signal_dbm
    dbms = str(dbms).split("-")[1:]

    # Test amaçlı! 3 anten olduğunda aşağıyı sil!
    d = -1 * int(dbms[0])
    dbms = [d, d, d] 
    return dbms



def post_output_to_adminpanel(output_info):
    
    output_info_json = json.dumps(vars(output_info))
    # output_info_json = json.dumps({"a": "abc", "b": "def"})
    # Send the data to your Django project
    url = 'http://127.0.0.1:8000/update_output_info/'
    response = requests.post(url, json=output_info_json)

    # Check response status or handle errors as needed
    if response.status_code == 200:
        print("Output info sent successfully!")
    else:
        print("Failed to send output info.")