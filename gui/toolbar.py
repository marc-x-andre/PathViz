import tkinter as tk

from commons.common import Common, Event
from utils.logger import get_logger


BTN_DEFAULT_STYLE = {"width": 20, "height": 2, "bg": "blue", "fg":"white"}


class Toolbar:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.generate_graph_btn = tk.Button(text="Generate Graph", command=self.on_click_generate_graph, **BTN_DEFAULT_STYLE)
        self.graph_seed_label = tk.Label(text=f"Seed: ")

        self._pack_component()
        self._register_events()

    def on_click_generate_graph(self):
        Common.gui_event.emit(Event.REGENERATE_GRAPH)

    def update_seed(self, seed: int, **kwargs):
        self.graph_seed_label.configure(text=f"Seed: {seed}")

    def _register_events(self):
        Common.gui_event.on(Event.NEW_GRAPH, self.update_seed)

    def _pack_component(self):
        self.logger.info("Packing Toolbar")
        self.generate_graph_btn.pack()
        self.graph_seed_label.pack()
