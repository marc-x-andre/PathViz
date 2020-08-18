import random
from abc import ABC, abstractmethod

from models.grid import Grid
from utils.seed import get_random_seed


class Maze(ABC):
    """
    Abstract representation of a maze maker class algorithm
    """

    @property
    @abstractmethod
    def name(self) -> str:
        return "Abstract Maze"

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
    def make(self):
        """Create the maze in the grid"""
        pass
