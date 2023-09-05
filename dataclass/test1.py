from dataclasses import dataclass
import os

@dataclass
class Car:
    brand : str
    price : int



if __name__ == '__main__':
    c1 = Car("tsla", 100)
    print(f"{c1.brand}, {c1.price}")