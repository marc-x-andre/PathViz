from abc import ABC, abstractmethod

from models.grid import Grid


class Pathfinding(ABC):
    """
    Abstract representation of a pathfinding resolver class algorithm
    """

    def __init__(self, grid: Grid):
        self.grid = grid

    @abstractmethod
    def next_step(self):
        """Should update the models boxes to the next step of the algorithm iteration
        The iteration should be visually pretty.
        """
        pass

    @abstractmethod
    def resolve(self):
        """Resolve the models maze"""
        pass
