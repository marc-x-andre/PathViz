import unittest
import random

from graph.entities import Node, Graph
from graph.generator import generate_graph
from utils.logger import get_logger


class TestGraphGenerator(unittest.TestCase):

    logger = get_logger(__name__)

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_generate_graph(self):
        graph_1 = generate_graph(100, 20)
        graph_2 = generate_graph(100, 20)

        self.assertEqual(str(graph_1), str(graph_2), "Same parameter should generate same graph")

        self.logger.info(generate_graph(40, 1).debug_str())
