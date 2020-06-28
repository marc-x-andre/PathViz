import tkinter as tk

from gui.grid_canvas import GridCanvas
from gui.toolbar import Toolbar
from utils.logger import get_logger


BTN_DEFAULT_STYLE = {"width": 20, "height": 2, "bg": "blue", "fg": "white"}


class Manager:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.main_window = tk.Tk()
        self.main_window.title("PathViz")
        self.toolbar = Toolbar()
        self.canvas = GridCanvas(self.main_window)
        self.main_window.mainloop()

    def reset_canvas(self):
        self.canvas.reset()

