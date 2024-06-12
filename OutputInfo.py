

class OutputInfo:
    def __init__(self, mac: str, dbms: list[int], location: list[float], under_attack: int, timestamp: str) -> None:
        self.mac = mac
        self.dbms = dbms
        self.location = location
        self.under_attack = under_attack
        self.timestamp = timestamp
        