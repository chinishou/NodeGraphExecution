"""
Connector Model
===============

Represents an input or output connector on a node.
Connectors allow data to flow between nodes.
"""

from typing import Optional, Any
from enum import Enum

from .node_model import NodeModel


class ConnectorType(Enum):
    INPUT = "input"
    OUTPUT = "output"


class ConnectorModel:
    """
    Data model for a node connector.

    Connectors are the input/output ports on nodes that allow connections.

    Attributes:
        name: Connector identifier
        connector_type: INPUT or OUTPUT
        data_type: Type of data this connector accepts/produces
        display_name: Human-readable name
        node: The node this connector belongs to
        multi_connection: Whether multiple connections are allowed
        default_value: Default value if no connection
        _connector_pairs: tuples of connector pairs
    """

    def __init__(
        self,
        name: str,
        connector_type: ConnectorType,
        data_type: str = "any",
        display_name: Optional[str] = None,
        node: Optional[NodeModel] = None,
        multi_connection: bool = False,
        default_value: Any = None,
    ):
        self.name = name
        self.connector_type = connector_type
        self.data_type = data_type
        self.display_name = display_name or name
        self.node = node
        self.multi_connection = multi_connection
        self.default_value = default_value

        # Store connections (for outputs: list of connectors, for inputs: single/multiple connectors)
        self._connector_pairs: list[ConnectorModel] = []

        # Cached value (for data flow)
        self._cached_value: Any = None

    def is_input(self) -> bool:
        """Check if this is an input connector."""
        return self.connector_type == ConnectorType.INPUT

    def is_output(self) -> bool:
        """Check if this is an output connector."""
        return self.connector_type == ConnectorType.OUTPUT

    def is_connected(self) -> bool:
        """Check if this connector has any connections."""
        return len(self._connector_pairs) > 0

    def connector_pairs(self) -> list["ConnectorModel"]:
        """Get list of connected connectors."""
        return self._connector_pairs.copy()

    def _can_connect_to(self, other: "ConnectorModel") -> bool:
        """Check if connection to another connector is valid."""
        # Can't connect to self
        if other is self:
            return False

        # Can't connect to same node
        if other.node is self.node:
            return False

        # Input can only connect to output and vice versa
        if self.connector_type == other.connector_type:
            return False

        if self.data_type != other.data_type:
            return False

        return True

    def connect_to(self, other: "ConnectorModel") -> bool:
        """
        Connect this connector to another connector.

        Args:
            other: The connector to connect to

        Returns:
            True if connection was successful, False otherwise
        """
        # Validate connection
        if not self._can_connect_to(other):
            return False

        # Add connection
        if other not in self._connector_pairs:
            self._connector_pairs.append(other)
            # Also add reverse connection
            if self not in other._connector_pairs:
                other._connector_pairs.append(self)

            return True

        return False

    def disconnect_from(self, other: "ConnectorModel") -> bool:
        """
        Disconnect from another connector.

        Args:
            other: The connector to disconnect from

        Returns:
            True if disconnection was successful
        """
        if other in self._connector_pairs:
            self._connector_pairs.remove(other)

            # Also remove reverse connection
            if self in other._connector_pairs:
                other._connector_pairs.remove(self)

            return True

        return False
