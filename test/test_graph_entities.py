import unittest

from grid.entities import Node, Graph
from utils.logger import get_logger


class TestGraphEntities(unittest.TestCase):

    logger = get_logger(__name__)

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_node_unique_id(self):
        unique_ids = []
        for x in range(100000):
            unique_ids.append(Node(name="test").unique_id)
        self.assertEqual(len(unique_ids), len(set(unique_ids)), "Node unique_id isn't unique")

    def test_node_add(self):
        a = Node(name="a")
        b = Node(name="b")

        a.add([a])
        self.assertEqual(len(a.nodes), 0, "Should do nothing")

        a.add([b])
        self.assertIn(a, b.nodes, "A should have a new node B")
        self.assertIn(b, a.nodes, "B should have a new node A")

        a.add([b])
        self.assertEqual(len(a.nodes), 1, "B shouldn't be added multiple time")
        self.assertEqual(len(b.nodes), 1, "A shouldn't be added multiple time")

        b.add([a])
        self.assertEqual(len(a.nodes), 1, "B shouldn't be added multiple time")
        self.assertEqual(len(b.nodes), 1, "A shouldn't be added multiple time")

    def test_graph_add(self):
        node_a = Node(name="a")
        node_b = Node(name="b")
        graph = Graph(nodes=[])

        graph.add([node_a])

        self.assertIn(node_a, graph.nodes, "A should be added in nodes")
        self.assertNotIn(node_b, graph.nodes, "B shouldn't be added in nodes")

    def test_graph_connect(self):
        node_a = Node(name="a")
        node_b = Node(name="b")
        graph = Graph(nodes=[])

        graph.connect((node_a, node_b))

        self.assertIn(node_a, graph.nodes, "A should be added in nodes")
        self.assertIn(node_b, graph.nodes, "B shouldn't be added in nodes")
