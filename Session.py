from pyshark.packet.packet import Packet


class Session:
    def __init__(self) -> None:
        self.begin = False
        self.finish = False
        self._frames: list[Packet] = []
    
    @property
    def frames(self):
        return self._frames
    @frames.setter
    def frames(self, _frames):
        self._frames = _frames[self.begin:self.finish]
    

        


