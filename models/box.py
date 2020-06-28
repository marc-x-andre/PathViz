from enum import Enum

from pydantic.main import BaseModel


class Point(BaseModel):
    x: int
    y: int


class BoxAround(Enum):
    """
    Use for Box.around_ref dictionary
    0 1 2
    3 4 5
    6 7 8
    Box.around_ref[CENTER] should return self
    TODO Implement if needed
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
    FINAL_PATH = "final_path"


class BoxType(Enum):
    EMPTY = "empty"
    START = "start"
    END = "end"
    WALL = "wall"


class Box(BaseModel):
    """Representation of a models box"""
    position: Point
    status: BoxStatus = BoxStatus.UNVISITED
    type: BoxType = BoxType.EMPTY
    # around_ref: Dict[int, Union["Box", None]] = {}  # Ref to adjacent box in the models TODO

    def __str__(self):
        return f"Box(position={self.position}, status={self.status}, type={self.type})"


Box.update_forward_refs()
