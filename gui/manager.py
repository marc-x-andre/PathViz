import tkinter as tk


from gui.canvas import CanvasGraph
from gui.toolbar import Toolbar
from utils.logger import get_logger


BTN_DEFAULT_STYLE = {"width": 20, "height": 2, "bg": "blue", "fg":"white"}


class Manager:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.main_window = tk.Tk()
        self.main_window.title("Graph Player")
        self.toolbar = Toolbar()
        self.canvas = CanvasGraph(self.main_window)
        self.main_window.mainloop()

    def reset_canvas(self):
        self.canvas.reset()

