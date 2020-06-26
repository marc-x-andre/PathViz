import uuid
from typing import List, Optional, Tuple, Union
from uuid import UUID

from pydantic import validator
from pydantic.main import BaseModel


class Node(BaseModel):
    unique_id: UUID = None
    name: Union[str, int] = ""
    point: Tuple[int, int] = (0, 0)
    nodes: List["Node"] = []
    tags: List[str] = []

    @validator('unique_id', pre=True, always=True)
    def set_id(cls, v):
        return v or uuid.uuid4()

    def add(self, nodes: List["Node"]):
        for node in nodes:
            if node.unique_id == self.unique_id:
                continue
            if node.unique_id not in [n.unique_id for n in self.nodes]:
                self.nodes.append(node)
            if self.unique_id not in [n.unique_id for n in node.nodes]:
                node.nodes.append(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Node(name={self.name}, nodes={[node.name for node in self.nodes]}))"


Node.update_forward_refs()


class Graph(BaseModel):
    nodes: List[Node] = []
    entry_node: Optional[Node]
    exit_node: Optional[Node]

    def add(self, nodes: List[Node]):
        for node in nodes:
            if node.unique_id not in [n.unique_id for n in self.nodes]:
                self.nodes.append(node)

    def connect(self, nodes: (Node, Node)):
        self.add([nodes[0], nodes[1]])
        nodes[0].add([nodes[1]])

    def debug_str(self) -> str:
        newline = '\n'
        tab = '\t'
        nodes = newline.join([f"{tab}{str(node)}" for node in self.nodes])
        return f"{newline}Graph(nodes={newline}{nodes}, " \
               f"{newline}entry_node={self.entry_node}, {newline}exit_node={self.exit_node}{newline})"
