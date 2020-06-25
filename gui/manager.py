import tkinter as tk

from gui.graph_canvas import GraphCanvas
from utils.logger import get_logger


class Manager:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.main_window = tk.Tk()
        self._pack_components()
        self.main_window.mainloop()

    def reset_window(self):
        pass

    def _pack_components(self):
        self.logger.info("Packing Main Window")
        greeting = tk.Label(text="Hello, Tkinter")
        button = tk.Button(
            text="Click me!",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        )
        greeting.pack()
        button.pack()
        GraphCanvas(self.main_window)
