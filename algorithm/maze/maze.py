from abc import ABC, abstractmethod

from models.grid import Grid


class Maze(ABC):
    """
    Abstract representation of a maze maker class algorithm
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
        """Resolve the models path"""
        pass

    @abstractmethod
    def _confirm_compatibility(self):
        """Check if the algorithm support every type of BoxType"""
        pass
