
from AttributeManager import AttributeManager

from Device import Device
from pyshark.packet.packet import Packet
from typing import Optional


class Client(Device):
    def __init__(self, mac, dbms: list) -> None:
        super().__init__(mac, dbms)
        
        self.frames: list[Packet] = []
        self.attributes = AttributeManager(self)

        self.last_deauth_frame: Optional[Packet] = None
        self.num_of_deauth_frames: int = 0
        self.num_of_frame_exchange: int = 0
        self.last_auth_frame: Optional[Packet] = None
        self.num_of_auth_frames: int = 0
        self.first_deauth_frame: Optional[Packet] = None

        