import tkinter as tk

from gui.canvas import CanvasGraph
from utils.logger import get_logger


BTN_DEFAULT_STYLE = {"width": 20, "height": 2, "bg": "blue", "fg":"white"}


class Toolbar:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.main_window = tk.Tk()
        self.main_window.title("Graph Player")
        self.canvas = None
        self._pack_components()
        self.canvas = CanvasGraph(self.main_window)
        self.main_window.mainloop()

    def reset_canvas(self):
        self.canvas.reset()

    def _pack_components(self):
        self.logger.info("Packing Main Window")
        greeting_label = tk.Label(text="Graph Visualization")
        generate_graph_btn = tk.Button(text="Generate Graph", command=self.reset_canvas, **BTN_DEFAULT_STYLE)
        graph_seed_label = tk.Label(text=f"")
        greeting_label.pack()
        generate_graph_btn.pack()
        graph_seed_label.pack()
