from __future__ import annotations
from typing import Optional
from GeoLocater import GeoLocater
from OutputInfo import OutputInfo



geolocater = GeoLocater()

class Device:
    def __init__(self, mac, dbms: list) -> None:
        self.mac = mac
        self.dbms = dbms
        self.x: float = 0
        self.y: float = 0
        self.rs = []
        self.under_attack = 0
        self.timestamp = ""
        self.output_info = OutputInfo(self.mac, self.dbms, [self.x, self.y], self.under_attack, self.timestamp)
        
    
    @staticmethod
    def find_device_by_mac(devices: list[Device], mac_to_find: str) -> Optional[Device]:
        for device in devices:
            if device.mac == mac_to_find:
                return device
        return None
    
    def set_geo_location(self):
         self.rs = geolocater.calculate_distances(self.dbms)
         location = geolocater.calculate_geo_location(self.rs)
         self.x, self.y = location[0], location[1]
         self.__update_output_info()
    
    def __update_output_info(self):
        self.output_info = OutputInfo(self.mac, self.dbms, [self.x, self.y], self.under_attack, self.timestamp)  # Adjust parameters as needed

    def __str__(self) -> str:
        return f"---\nMAC: {self.mac}\ndbms: {self.dbms}\nGeoLocation: (x: {self.x}, y: {self.y})\n---"
    

    def append_to_csv(self, csv_writer):
        csv_writer.writerow([
            self.output_info.mac,
            self.output_info.dbms,
            self.output_info.location,
            self.output_info.under_attack,
            self.output_info.timestamp
        ])