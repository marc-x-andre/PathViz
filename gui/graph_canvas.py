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
        # self.canvas.delete(ALL)








