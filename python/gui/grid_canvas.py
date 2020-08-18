from tkinter import Canvas, Tk, ALL
from typing import Dict, Optional, List, Type

from algorithm.maze.maze import Maze
from algorithm.pathfinding.pathfinding import Pathfinding
from commons.common import Common, Event
from models.box import Box, BoxStatus, BoxType, Point
from models.grid import Grid
from utils.logger import get_logger

BOX_SIZE = 20
CANVAS_PADDING = 1

BOX_STATUS_COLOR = {
    BoxStatus.VISITED: "#d4e09b",
    BoxStatus.UNVISITED: "#f2f4f3",
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
        self.border_entity_id = None
        self.canvas = canvas
        self.draw()

    def draw(self):
        fill = BOX_STATUS_COLOR[self.box.status] if self.box.type == BoxType.EMPTY else BOX_TYPE_COLOR[self.box.type]
        self.border_entity_id: int = self.canvas.create_rectangle(
            (self.box.position.x * BOX_SIZE) + CANVAS_PADDING,
            (self.box.position.y * BOX_SIZE) + CANVAS_PADDING,
            ((self.box.position.x * BOX_SIZE) + BOX_SIZE) + CANVAS_PADDING,
            ((self.box.position.y * BOX_SIZE) + BOX_SIZE) + CANVAS_PADDING,
            fill=fill
        )

    def __str__(self):
        return f"BoxCanvas(box={self.box}, border_entity_id={self.border_entity_id})"


class GridCanvas:

    logger = get_logger(__name__)
    canvas_width = 1000
    canvas_height = 1000

    is_resolve = False

    last_motion_box_updated: List[BoxCanvas] = []
    moving_special_box: Optional[BoxCanvas] = None

    def __init__(self, window: Tk):
        self.canvas = Canvas(window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.grid: Grid = None
        self.canvas_boxes: Dict[int, Dict[int, BoxCanvas]] = {}
        self._register_events()
        self.pathfinding: Pathfinding = None
        self.maze: Maze = None
        self.reset()

    ##
    # Maze
    ##

    def set_maze(self, maze: Type[Maze]):
        self.maze = maze(self.grid)
        self.reset()

    def make(self):
        if self.pathfinding:
            self.maze.make()
            self.draw()

    def next_step_maze(self):
        if self.pathfinding:
            self.maze.next_step()
            self.draw()
    ##
    # Pathfinding
    ##

    def set_pathfinding(self, pathfinding: Type[Pathfinding]):
        self.pathfinding = pathfinding(self.grid)
        self.reset()
        self.resolve_path()

    def resolve_path(self):
        if self.pathfinding:
            self.pathfinding.resolve()
            self.draw()

    def next_step_path(self):
        if self.pathfinding:
            self.pathfinding.next_step()
            self.draw()

    ##
    # Display
    ##

    def reset(self, **kwargs):
        self.canvas.delete(ALL)
        self.grid: Grid = Grid(width=int(self.canvas_width/BOX_SIZE), height=int(self.canvas_height/BOX_SIZE))
        self.grid.init_grid()
        self.draw()

    def draw(self):
        """Draw all box in the grid"""
        self.canvas.delete(ALL)
        self.canvas_boxes = {}
        for x in range(int(self.canvas_width/BOX_SIZE)):
            for y in range(int(self.canvas_height/BOX_SIZE)):
                if self.canvas_boxes.get(x) is None:
                    self.canvas_boxes[x] = {}
                self.canvas_boxes[x][y] = BoxCanvas(self.grid.boxes[x][y], self.canvas)

    def get_box_canvas_at(self, position: Point) -> Optional[BoxCanvas]:
        if self.canvas_boxes.get(int(position.x/BOX_SIZE)):
            return self.canvas_boxes.get(int(position.x / BOX_SIZE)).get(int(position.y/BOX_SIZE))
        return None

    ##
    # User Input
    ##

    def _motion_handler(self, event: Point):
        """Handle constant click"""
        if self.moving_special_box:
            # Currently moving a box
            self._move_box_canvas(event, self.moving_special_box)
        else:
            box_canvas = self.get_box_canvas_at(event)
            if box_canvas:
                if box_canvas.box.type != BoxType.EMPTY and box_canvas.box.type != BoxType.WALL:
                    self.moving_special_box = box_canvas
                else:
                    self._toggle_box_canvas(box_canvas)

    def _move_box_canvas(self, event: Point, box_canvas: BoxCanvas):
        future_position = self.get_box_canvas_at(event)
        if future_position is not box_canvas:
            tmp = box_canvas.box.type
            box_canvas.box.type = future_position.box.type
            future_position.box.type = tmp
            box_canvas.draw()
            future_position.draw()
            self.moving_special_box = future_position

    def _toggle_box_canvas(self, box_canvas: BoxCanvas):
        """Change box status from wall to empty, vice versa"""
        if box_canvas not in self.last_motion_box_updated:
            if box_canvas.box.type == BoxType.EMPTY:
                box_canvas.box.type = BoxType.WALL
            elif box_canvas.box.type == BoxType.WALL:
                box_canvas.box.type = BoxType.EMPTY
            box_canvas.draw()
            self.last_motion_box_updated.append(box_canvas)

    def _motion_stop_handler(self, event):
        self.last_motion_box_updated = []
        self.moving_special_box = None

    ##
    # Event
    ##

    def _register_events(self):
        Common.gui_event.on(Event.CLEAR, self.reset)
        Common.algorithm_event.on(Event.RESOLVE_PATH, self.set_pathfinding)
        self.canvas.bind("<Button-1>", self._motion_handler)
        self.canvas.bind("<B1-Motion>", self._motion_handler)
        self.canvas.bind("<ButtonRelease-1>", self._motion_stop_handler)

