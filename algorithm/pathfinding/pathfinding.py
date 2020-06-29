import random
from abc import ABC, abstractmethod

from models.grid import Grid
from utils.seed import get_random_seed


class Pathfinding(ABC):
    """
    Abstract representation of a pathfinding resolver class algorithm
    """

    @property
    @abstractmethod
    def name(self) -> str:
        return "Abstract Pathfinding"

    def __init__(self, grid: Grid, seed: int = None):
        self.grid = grid
        self.seed = seed or get_random_seed()
        random.seed(self.seed)

    @abstractmethod
    def next_step(self):
        """Should update the models boxes to the next step of the algorithm iteration
        The iteration should be visually pretty.
        """
        pass

    @abstractmethod
    def resolve(self):
        """Resolve the grid path"""
        pass

    @abstractmethod
    def _confirm_compatibility(self):
        """Check if the algorithm support every type of BoxType"""
        pass
