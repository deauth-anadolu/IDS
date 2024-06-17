
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: # to avoid circular import
    from Client import Client
from pyshark.packet.packet import Packet
from utils import *


class AttributeManager:
    def __init__(self) -> None:
        self.client = None
        self.threshold = 2
    def set_client(self, client: Client) -> None:
        self.client = client

    def time_difference(self):
        def update_last_deauth_frame(frame: Packet):
            self.client.last_auth_frame
            if is_frame_deauth(frame):
                self.client.last_auth_frame = frame

        def get_time_difference(last_auth_frame: Packet, last_deauth_frame: Packet):
            return get_frame_time(last_auth_frame) - get_frame_time(last_deauth_frame)

        is_auth = is_frame_auth(self.client.last_frame)
        is_deauth = update_last_deauth_frame(self.client.last_frame)
        if is_auth and is_deauth:
            time_difference_attr = get_time_difference(frame, client.last_deauth_frame) # type: ignore
            print(f"\nTIME_DIFFERENCE_ATTR = {time_difference_attr}\n")

            return time_difference_attr
        
    def num_of_deauth_frames(self):
        print(is_frame_deauth(self.client.last_frame))
        if is_frame_deauth(self.client.last_frame):
            self.client.num_of_deauth_frames += 1
            self.client.num_of_normal_frames = 0
        else:
            self.client.num_of_normal_frames += 1

            if self.client.num_of_normal_frames > self.threshold:
                self.client.num_of_deauth_frames = 0

    def num_of_frame_exchange(self) -> int:
        def update_last_auth_frame(frame: Packet):
            if is_frame_auth(frame):
                self.client.last_auth_frame = frame

        is_auth = update_last_auth_frame(self.client.last_frame)
        is_deauth = is_frame_deauth(self.client.last_frame)

        if is_auth and not is_deauth: 
            self.client.num_of_frame_exchange += 1
            
        elif is_auth and is_deauth: 
            aux = self.client.num_of_frame_exchange
            self.client.num_of_frame_exchange = 0

            return aux
            
        return
    
    def num_of_auth_frames(self) -> int:
        # client'ın deauth paketi göndermesi disconnect olduğu anlamına kesin gelmez. ona göre ilk disconnect olduğu frame'i tespit et.
        # aslında fark etmez biliyor musun? disconnect olup olmadığı önemli değil ki. önemli olan ilk deauth paketini aldıktan sonra kaç tane auth paketi gönderdiği!

        # ya peki, client'ın auth paketi göndermesi auth olduğu anlamına kesin gelir mi? veya buna ihtiyacımız var mı? sanırım yok. aslında var. nereye kadar auth paketlerini sayacağız, auth olana kadar.

        # num_of_auth_frames = disconnect olduktan hemen sonra kaç tane auth paketi gönderiliyor? bu attr (num_of_auth_frames) bu bilgiyi tutar.
        is_deauth = is_frame_deauth(self.client.last_frame)
        is_auth = is_frame_auth(self.client.last_frame)

        # if first_deuath_frame is not set, then set it with the deauth frame
        if is_deauth and not self.client.first_deauth_frame:
            self.client.first_deauth_frame = self.client.last_frame
        
        # if there is no deauth frame in the trafic till now, then return
        if not self.client.last_deauth_frame:
            return

        
        if self.client.first_deauth_frame and is_auth:
            self.client.num_of_auth_frames += 1

        # stop if the is_auth and ... condition was met. "..." can be checking the next 100 (random num) frames if they include a deauth frame.. if they don't include some, then we can stop counting the auth_frames.
        elif is_auth and ...:
            self.client.first_deauth_frame = None

            aux = self.client.num_of_auth_frames
            self.client.num_of_auth_frames = 0

            return aux

        return None
    
    def num_of_tcp_frames(self) -> int: pass
    def num_of_udp_frames(self) -> int: pass
    def num_of_association_frames(self) -> int: pass
    
        
        
       
       

def set_attributes(self, **kwargs) -> None:
    for key, value in kwargs.items():
        if hasattr(self, key):
            getattr(self, key).value = value  # Call setter on the Attribute object
        else:
            print(f"Warning: Attribute '{key}' does not exist in the class.")

# def get_attributes(self) -> dict[str, int | Attribute | None]:
#     return {
#         "time_difference": self.time_difference.value,
#         "num_of_deauth_frames": self.num_of_deauth_frames.value,
#         "num_of_frame_exchange": self.num_of_frame_exchange.value,
#         "num_of_auth_frames": self.num_of_auth_frames.value,
#         "num_of_tcp_frames": self.num_of_tcp_frames.value,
#         "num_of_association_frames": self.num_of_association_frames.value,
#         "num_of_udp_frames": self.num_of_udp_frames.value
#     }
    
