"""
Node Model
==========

Represents a node in the network graph.
Nodes are the fundamental building blocks that process data.
"""

from uuid import uuid4


class NodeModel:
    """
    Data model for a node.

    Attributes:
        id: Unique node identifier (UUID)
        name: Node display name
        node_type: Type of node (e.g., "AddNode", "SubnetNode")
        category: Category for organization (e.g., "Math", "Logic")
        position: (x, y) position in the network view
        parameters: Dictionary of parameters
        inputs: Dictionary of input connectors
        outputs: Dictionary of output connectors
    """

    def __init__(self, name: str = "Node", node_type: str = "BaseNode", category: str = "General"):
        self.id = str(uuid4())
        self.name = name
        self.node_type = node_type
        self.category = category

        # Visual attributes
        self.position = (0.0, 0.0)
        self.parameters = {}
        self.inputs = {}
        self.outputs = {}

    def __repr__(self) -> str:
        return f"NodeModel(name='{self.name}', type='{self.node_type}, id='{self.id}')"
