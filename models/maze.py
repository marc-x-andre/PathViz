import sys
import random
from typing import Dict

from pydantic import validator

from models.box import Box
from models.grid import Grid


class Maze(Grid):
    """
    Basicly a
    """
    width: int
    height: int
    boxes: Dict[int, Dict[int, Box]] = None
    start_box: Box = None
    end_box: Box = None
    seed: int = None

    @validator('seed', pre=True, always=True)
    def set_id(cls, v):
        return v or random.randrange(sys.maxsize)

    def init_maze(self):
        if self.boxes is None:
            self.init_grid()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Maze(width={self.width}, height={self.height})"







