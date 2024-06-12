from typing import Optional

class A(Optional[int | str]):
    def __init__(self, b) -> None:
        self.b = b
        self.c = "ccc"


    def __get__(self):
        return self.c
    

a = A("bbb")

print(a)    