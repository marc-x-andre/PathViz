import random
from typing import Tuple, List

from grandalf.layouts import DigcoLayout

from graph.entities import Graph, Node


def _assign_nodes_point(nodes: List[Node], edges: List[Tuple[Node, Node]], cartesian_size: Tuple[int, int]):
    """
    Using https://github.com/bdcht/grandalf to get graph nodes position
    If you find something better, create an issue
    """
    from grandalf.graphs import Graph as GrandalfGraph, Edge, Vertex
    from grandalf.layouts import SugiyamaLayout

    class defaultview(object):
        w, h = cartesian_size[0], cartesian_size[1]

    grandalf_vertexs = []
    grandalf_edges = []

    print(edges)
    for e in edges:
        v1 = Vertex(data=e[0].unique_id)
        v2 = Vertex(data=e[1].unique_id)
        v1.view = defaultview()
        v2.view = defaultview()
        grandalf_vertexs.extend([v1, v2])
        grandalf_edges.append(Edge(v1, v2))
    print(grandalf_vertexs)
    print(grandalf_edges)

    graph = GrandalfGraph(grandalf_vertexs, grandalf_edges)

    # Assign view dimensions
    class defaultview(object):
        # w, h = cartesian_size[0], cartesian_size[1]
        w, h = 10, 10
    for v in grandalf_vertexs:
        v.view = defaultview()
    # dco = DigcoLayout(graph.C[0])
    # dco.init_all()
    # dco.draw()
    # for v in graph.C[0].sV:
    #     print("%s: (%d,%d)" % (v.data, v.view.xy[0], v.view.xy[1]))
    pass

















def _get_random_number(average: int):
    return random.randrange(int(average / 3), int(average * 2))


def generate_graph(average_nodes: int = 30, seed=None, cartesian_size: Tuple[int, int] = None) -> Graph:
    if seed:
        random.seed(seed)
    nb_nodes = _get_random_number(average_nodes)

    nodes = [Node(name=i) for i in range(nb_nodes)]

    graph = Graph()
    edges: List[Tuple[Node, Node]] = []
    for i in range(random.randrange(1, nb_nodes)):
        if seed:
            seed += 1
            random.seed(seed)
        node_1, node_2 = random.sample(nodes, 2)
        edges.append((node_1, node_2))
        graph.connect(node_1, node_2)


    _assign_nodes_point(nodes, edges, cartesian_size)

    if cartesian_size:
        for n in nodes:
            n.point = (random.randrange(0, cartesian_size[0]), random.randrange(0, cartesian_size[1]))

    return graph



