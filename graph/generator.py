import random

from graph.entities import Graph, Node
from utils.logger import debug


def _get_random_number(average: int):
    return random.randrange(int(average / 3), int(average * 2))


def generate_graph(average_nodes: int = 10, seed=None) -> Graph:
    if seed:
        random.seed(seed)
    nb_nodes = _get_random_number(average_nodes)
    nodes = [Node(name=i) for i in range(nb_nodes)]

    graph = Graph()
    for i in range(random.randrange(1, nb_nodes)):
        seed += 1
        random.seed(seed)
        node_link = random.sample(nodes, 2)
        graph.connect(node_link)

    return graph









