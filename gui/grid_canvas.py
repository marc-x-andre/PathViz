from tkinter import Canvas, Tk, ALL
from typing import Dict

from commons.common import Common, Event
from models.box import Box, BoxStatus, BoxType
from models.grid import Grid
from utils.logger import get_logger

BOX_SIZE = 30
CANVAS_PADDING = 1

BOX_STATUS_COLOR = {
    BoxStatus.VISITED: "",
    BoxStatus.UNVISITED: "",
}

BOX_TYPE_COLOR = {
    BoxType.EMPTY: "#f2f4f3",
    BoxType.START: "#008DD5",
    BoxType.END: "#f56476",
    BoxType.WALL: "#495159",
}


class BoxCanvas:

    def __init__(self, box: Box, canvas: Canvas):
        self.box = box
        self.border_entity_id: int = canvas.create_rectangle(
            (box.position.x * BOX_SIZE) + CANVAS_PADDING,
            (box.position.y * BOX_SIZE) + CANVAS_PADDING,
            ((box.position.x * BOX_SIZE) + BOX_SIZE) + CANVAS_PADDING,
            ((box.position.y * BOX_SIZE) + BOX_SIZE) + CANVAS_PADDING,
            fill=BOX_TYPE_COLOR[box.type]
        )

    def update(self):
        pass


class GridCanvas:

    canvas_width = 800
    canvas_height = 800

    def __init__(self, window: Tk):
        self.logger = get_logger(__name__)
        self.canvas = Canvas(window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.grid: Grid = None
        self.canvas_boxes: Dict[int, Dict[int, BoxCanvas]] = {}
        # self.canvas_boxes: Dict = None
        # self.reset()
        self._register_events()

    def reset(self, **kwargs):
        self.canvas.delete(ALL)
        self._init_grid()

    def _register_events(self):
        Common.gui_event.on(Event.CLEAR, self.reset)

    def _init_grid(self):
        self.grid: Grid = Grid(width=int(self.canvas_width/BOX_SIZE), height=int(self.canvas_height/BOX_SIZE))
        self.grid.init_grid()
        for x in range(int(self.canvas_width/BOX_SIZE)):
            for y in range(int(self.canvas_height/BOX_SIZE)):
                if self.canvas_boxes.get(x) is None:
                    self.canvas_boxes[x] = {}
                # sleep(0.1)
                self.canvas_boxes[x][y] = BoxCanvas(self.grid.boxes[x][y], self.canvas)

    def update(self):
        pass

