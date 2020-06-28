import uuid
from typing import Dict
from uuid import UUID

from pydantic import validator
from pydantic.main import BaseModel

from models.box import Box, Point, BoxType


class Grid(BaseModel):
    unique_id: UUID = None  # To save or multi view
    width: int
    height: int
    boxes: Dict[int, Dict[int, Box]] = None
    start_box: Box = None
    end_box: Box = None

    @validator('unique_id', pre=True, always=True)
    def set_id(cls, v):
        return v or uuid.uuid4()

    def init_grid(self):
        if self.boxes is not None:
            return
        boxes: Dict[int, Dict[int, Box]] = {}
        # Create boxes
        for x in range(self.width):
            boxes[x] = {}
            for y in range(self.height):
                boxes[x][y] = Box(position=Point(x=x, y=y))
        self.boxes = boxes

        self.start_box = self.boxes[int(self.width / 4)][int(self.height / 2)]
        self.end_box = self.boxes[int(self.width / 3 * 2.5)][int(self.height / 2)]
        self.start_box.type = BoxType.START
        self.end_box.type = BoxType.END

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Grid(width={self.width}, height={self.height})"









