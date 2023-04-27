from dataclasses import dataclass
import time
from config import *

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

@dataclass
class Node:
    x: float
    dx: float
    dy: int

    def __init__(self, x=0, dx=0, dy=0):
        self.x = x
        self.dx = dx
        self.dy = dy