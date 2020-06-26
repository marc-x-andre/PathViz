import random
from typing import Tuple

from graph.entities import Graph, Node


def _get_random_number(average: int):
    return random.randrange(int(average / 3), int(average * 2))


def generate_graph(average_nodes: int = 30, seed=None, cartesian_size: Tuple[int, int] = None) -> Graph:
    if seed:
        random.seed(seed)
    nb_nodes = _get_random_number(average_nodes)

    nodes = [Node(name=i) for i in range(nb_nodes)]

    if cartesian_size:
        for n in nodes:
            n.point = (random.randrange(0, cartesian_size[0]), random.randrange(0, cartesian_size[1]))

    graph = Graph()
    for i in range(random.randrange(1, nb_nodes)):
        if seed:
            seed += 1
            random.seed(seed)
        node_link = random.sample(nodes, 2)
        graph.connect(node_link)

    return graph









