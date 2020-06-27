import math
import random
import sys
from tkinter import Canvas, Tk, ALL
from typing import List

from graph.entities import Node, Graph
from graph.generator import generate_graph
from commons.common import Common, Event
from utils.logger import get_logger


class CanvasNode:
    oval_size = 40

    def __init__(self, node: Node, canvas: Canvas):
        self.node = node
        self.entity_id: int = canvas.create_oval(
            (node.point[0] - self.oval_size/2),
            (node.point[1] - self.oval_size/2),
            (node.point[0] + self.oval_size/2),
            (node.point[1] + self.oval_size/2),
            fill="red"
        )


class CanvasGraph:
    canvas_width = 800
    canvas_height = 800

    def __init__(self, window: Tk):
        self.logger = get_logger(__name__)
        self.canvas = Canvas(window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.graph: Graph = None
        self.canvas_nodes: List[CanvasNode] = None
        self.seed_value: int = None
        self.reset()
        self._register_events()

    def reset(self):
        self.seed_value = random.randrange(sys.maxsize)
        self.canvas.delete(ALL)
        self.graph: Graph = generate_graph(cartesian_size=(self.canvas_width, self.canvas_height), seed=self.seed_value)
        self.draw_links()
        self.canvas_nodes = [CanvasNode(n, self.canvas) for n in self.graph.nodes]
        Common.gui_event.emit(Event.NEW_GRAPH, graph=self.graph, seed=self.seed_value)

    def draw_links(self):
        for node in self.graph.nodes:
            for n in node.nodes:
                if n.point[0] >= n.point[0]:  # Draw only in one direction
                    self.canvas.create_line(n.point[0], n.point[1], node.point[0], node.point[1], fill="#476042")
                    line_length = int(math.sqrt(((n.point[0] - node.point[0]) ** 2 + (n.point[1] - node.point[1]) ** 2)))
                    self.canvas.create_text(
                        (n.point[0] + node.point[0])/2,
                        ((n.point[1] + node.point[1])/2),
                        text=line_length
                    )

    def _register_events(self):
        Common.gui_event.on(Event.REGENERATE_GRAPH, self.reset)



