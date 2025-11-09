"""
Network Model
=============

Represents a node network (graph).
A network contains nodes and connections between them.
"""

from typing import Dict
from .node_model import NodeModel


class NetworkModel:
    """
    Data model for a node network.

    A network is a collection of nodes and connections between them.
    Similar to Houdini's network view.

    Attributes:
        name: Network name
        nodes: Dictionary of nodes (id -> NodeModel)
        connections: List of connections (tuples of connector pairs)
    """

    def __init__(self, name: str = "Network"):
        self.name = name
        self.nodes: Dict[str, NodeModel] = {}
