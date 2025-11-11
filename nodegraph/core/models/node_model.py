"""
Node Model
==========

Represents a node in the network graph.
Nodes are the fundamental building blocks that process data.
"""

from typing import Dict, Optional
from uuid import uuid4

from .connector_model import ConnectorModel
from .parameter_model import ParameterModel


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
        _inputs: Dictionary of input connectors
        _outputs: Dictionary of output connectors
    """

    def __init__(self, name: str = "Node", node_type: str = "BaseNode", category: str = "General"):
        self.id = str(uuid4())
        self.name = name
        self.node_type = node_type
        self.category = category

        # Visual attributes
        self.position = (0.0, 0.0)
        self.parameters: Dict[str, ParameterModel] = {}
        self._inputs: Dict[str, ConnectorModel] = {}
        self._outputs: Dict[str, ConnectorModel] = {}

    def __repr__(self) -> str:
        return f"NodeModel(name='{self.name}', type='{self.node_type}, id='{self.id}')"

    def input(self, name: str) -> Optional[ConnectorModel]:
        """Get input connector by name."""
        return self._inputs.get(name)

    def output(self, name: str) -> Optional[ConnectorModel]:
        """Get output connector by name."""
        return self._outputs.get(name)

    def inputs(self) -> Dict[str, ConnectorModel]:
        """Get all input connectors."""
        return self._inputs.copy()

    def outputs(self) -> Dict[str, ConnectorModel]:
        """Get all output connectors."""
        return self._outputs.copy()

    def set_position(self, x: float, y: float) -> None:
        """Set node position."""
        self.position = (x, y)
