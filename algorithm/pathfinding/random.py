import random

from algorithm.pathfinding.pathfinding import Pathfinding
from models.box import BoxStatus
from models.grid import Grid


class Random(Pathfinding):
    """For test purpose only"""

    name = "Random"

    def __init__(self, grid: Grid, seed: int = None):
        super().__init__(grid, seed)

    def next_step(self):
        raise NotImplementedError("Oh no!")

    def resolve(self):
        for x in range(random.randrange(self.grid.width)):
            for y in range(random.randrange(self.grid.height)):
                self.grid.boxes[x][y].status = BoxStatus.VISITED

    def _confirm_compatibility(self):
        pass
