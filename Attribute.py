from Session import Session

class Attribute:
    def __init__(self, default_value) -> None:
        self.value = default_value
        self.session = Session()
            