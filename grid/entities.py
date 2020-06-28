from enum import Enum
from typing import Tuple, Dict, Union

from pydantic import validator
from pydantic.main import BaseModel


class BoxAround(Enum):
    """
    Use for Box.around_ref dictionary
    0 1 2
    3 4 5
    6 7 8
    Box.around_ref[CENTER] should return self
    """
    TOP_LEFT = 0
    TOP_CENTER = 1
    TOP_RIGHT = 2
    LEFT = 3
    CENTER = 4
    RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM_CENTER = 7
    BOTTOM_RIGHT = 8


class BoxStatus(Enum):
    """Tell if a box as been visited, could be a bool"""
    UNVISITED = "unvisited"
    VISITED = "visited"


class BoxType(Enum):
    EMPTY = "empty"
    START = "start"
    END = "end"
    WALL = "wall"


class Box(BaseModel):
    """Representation of a grid box"""
    position: Tuple[int, int] = (0, 0)
    status: BoxStatus = BoxStatus.UNVISITED
    type: BoxType = BoxType.EMPTY
    around_ref: Dict[int, Union["Box", None]] = {}  # Ref to adjacent box in the grid

    def get_around(self, location: BoxAround) -> Union["Box", None]:
        return self.around_ref[location.value]

    def __str__(self):
        return f"Box(position={self.position}, status={self.status}, type={self.type})"


Box.update_forward_refs()


class Grid(BaseModel):
    width: int
    height: int
    boxes: Dict[int, Dict[int, Box]] = None

    @validator('boxes', always=True)
    def set_boxes(cls, v):
        if v is not None:
            return v
        boxes: Dict[int, Dict[int, Box]] = {}
        # Create boxes
        for x in range(cls.width):
            boxes[x] = {}
            for y in range(cls.height):
                boxes[x][y] = Box(position=(x, y))
        # Assign boxes around_ref
        for x in range(cls.width):
            for y in range(cls.height):
                boxes[x][y].around_ref = {
                    BoxAround.TOP_LEFT.value: boxes.get(x - 1).get(y - 1) if boxes.get(x) is not None else None,
                    BoxAround.TOP_CENTER.value: boxes.get(x).get(y - 1) if boxes.get(x) is not None else None,
                    BoxAround.TOP_RIGHT.value: boxes.get(x + 1).get(y - 1) if boxes.get(x) is not None else None,
                    BoxAround.LEFT.value: boxes.get(x - 1).get(y) if boxes.get(x) is not None else None,
                    BoxAround.CENTER.value: boxes.get(x).get(y),
                    BoxAround.RIGHT.value: boxes.get(x + 1).get(y) if boxes.get(x) is not None else None,
                    BoxAround.BOTTOM_LEFT.value: boxes.get(x - 1).get(y + 1) if boxes.get(x) is not None else None,
                    BoxAround.BOTTOM_CENTER.value: boxes.get(x).get(y + 1) if boxes.get(x) is not None else None,
                    BoxAround.BOTTOM_RIGHT.value: boxes.get(x + 1).get(y + 1) if boxes.get(x) is not None else None,
                }
        return boxes










