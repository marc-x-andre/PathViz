from tkinter import Canvas, Tk

from utils.logger import get_logger


class GraphCanvas:

    def __init__(self, window: Tk):
        self.logger = get_logger(__name__)
        self.canvas = Canvas(window, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_line(0, 0, 200, 100)
        self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")
        oval = self.canvas.create_oval(50, 25, 150, 75, fill="red")
        self.canvas.move(oval, 200, 200)
        # self.canvas.delete(ALL)

    def move_node(self, node_id: int, x, y):
        pass

    def compute_node_distances(self, node_id: int):
        pass

    def update_node_status(self, node_id: int, status):
        pass

    def update_node_information(self, node_id: int, x, y):
        pass

    def update_node_information(self, node_id: int, x, y):
        pass

