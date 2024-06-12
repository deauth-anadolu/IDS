
from Device import Device
from Client import Client

class AccessPoint(Device):
    _clients: list[Client] = []

    def __init__(self, mac, dbms: list) -> None:
        super().__init__(mac, dbms)
     
    @property
    def clients(self):
        return self._clients
    @clients.setter
    def clients(self, value):
        self._clients = value

    