
from AttributeManager import AttributeManager

from Device import Device
from pyshark.packet.packet import Packet
from typing import Optional
from Attribute import Attribute

ATTRMANAGER = AttributeManager()

class Client(Device):
    
    def __init__(self, mac, dbms: list, frame: Packet) -> None:

        super().__init__(mac, dbms)
        self.frames: list[Packet] = []
        self.last_frame: Optional[Packet] = frame

        self.last_deauth_frame: Optional[Packet] = None

        self.last_auth_frame: Optional[Packet] = None
        self.first_deauth_frame: Optional[Packet] = None

        self._num_of_auth_frames: int = 0
        self._num_of_deauth_frames: int = 0
        self._num_of_frame_exchange: int = 0
        self._num_of_tcp_frames = Attribute(0)
        self._num_of_udp_frames = Attribute(0)
        self._time_difference = Attribute(None)
        self._num_of_association_frames = Attribute(0)

        self.num_of_normal_frames: int = 0





    @property
    def num_of_deauth_frames(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_deauth_frames()
        return self._num_of_deauth_frames
    @num_of_deauth_frames.setter
    def num_of_deauth_frames(self, value: int) -> None:
        self._num_of_deauth_frames = value

    @property
    def num_of_auth_frames(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_auth_frames()
        return self._num_of_auth_frames
    @num_of_auth_frames.setter
    def num_of_auth_frames(self, value: int) -> None:
        self._num_of_auth_frames = value


    @property
    def num_of_frame_exchange(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_frame_exchange()
        return self._num_of_frame_exchange
    @num_of_frame_exchange.setter
    def num_of_frame_exchange(self, value: int) -> None:
        self._num_of_frame_exchange = value

    @property
    def num_of_tcp_frames(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_tcp_frames()
        return self._num_of_tcp_frames
    @num_of_tcp_frames.setter
    def num_of_tcp_frames(self, value: int) -> None:
        self._num_of_tcp_frames = value

    @property
    def num_of_udp_frames(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_udp_frames()
        return self._num_of_udp_frames
    @num_of_udp_frames.setter
    def num_of_udp_frames(self, value: int) -> None:
        self._num_of_udp_frames = value

    @property
    def time_difference(self) -> Optional[int]:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.time_difference()
        return self._time_difference
    @time_difference.setter
    def time_difference(self, value: Optional[int]) -> None:
        self._time_difference = value

    @property
    def num_of_association_frames(self) -> int:
        ATTRMANAGER.set_client(self)
        ATTRMANAGER.num_of_association_frames()
        return self._num_of_association_frames
    @num_of_association_frames.setter
    def num_of_association_frames(self, value: int) -> None:
        self._num_of_association_frames = value

        
        