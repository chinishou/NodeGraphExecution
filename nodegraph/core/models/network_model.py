"""
Network Model
=============

Represents a node network (graph).
A network contains nodes and connections between them.
"""

from typing import Dict, List, Optional, Tuple
from .node_model import NodeModel
from .connector_model import ConnectorModel


class NetworkModel:
    """
    Data model for a node network.

    A network is a collection of nodes and connections between them.
    Similar to Houdini's network view.

    Attributes:
        name: Network name
        nodes: Dictionary of nodes (id -> NodeModel)
        _connections: List of connections (tuples of connector pairs)
    """

    def __init__(self, name: str = "Network"):
        self.name = name
        self.nodes: Dict[str, NodeModel] = {}
        self._connections: List[ConnectorModel] = []

    def add_node(self, node: NodeModel) -> bool:
        """
        Add a node to the network.

        Args:
            node: The node to add

        Returns:
            True if node was added successfully
        """
        if node.id in self.nodes:
            return False

        node.network = self
        self.nodes[node.id] = node

        return True

    def remove_node(self, node_id: str) -> bool:
        """
        Remove a node from the network.

        Args:
            node_id: ID of the node to remove

        Returns:
            True if node was removed successfully
        """
        node = self.nodes.get(node_id)
        if not node:
            return False

        # Remove node
        del self.nodes[node_id]
        node.network = None

        return True

    def get_node(self, node_id: str) -> Optional[NodeModel]:
        """Get node by ID."""
        return self.nodes.get(node_id)

    def connect(self, source_node_id: str, source_output: str, target_node_id: str, target_input: str) -> bool:
        """
        Create a connection between two nodes.

        Args:
            source_node_id: ID of the source node
            source_output: Name of the output connector
            target_node_id: ID of the target node
            target_input: Name of the input connector

        Returns:
            True if connection was successful
        """
        source_node = self.get_node(source_node_id)
        target_node = self.get_node(target_node_id)

        if not source_node or not target_node:
            return False

        source_connector = source_node.output(source_output)
        target_connector = target_node.input(target_input)

        if not source_connector or not target_connector:
            return False

        success = source_connector.connect_to(target_connector)

        return success

    def disconnect(self, source_node_id: str, source_output: str, target_node_id: str, target_input: str) -> bool:
        """
        Remove a connection between two nodes.

        Args:
            source_node_id: ID of the source node
            source_output: Name of the output connector
            target_node_id: ID of the target node
            target_input: Name of the input connector

        Returns:
            True if disconnection was successful
        """
        source_node = self.get_node(source_node_id)
        target_node = self.get_node(target_node_id)

        if not source_node or not target_node:
            return False

        source_connector = source_node.output(source_output)
        target_connector = target_node.input(target_input)

        if not source_connector or not target_connector:
            return False

        success = source_connector.disconnect_from(target_connector)

        return success

    def connections(self) -> List[Tuple[ConnectorModel, ConnectorModel]]:
        """
        Get all connections in the network.

        Returns:
            List of (output_connector, input_connector) tuples
        """
        conns = []

        for node in self.nodes.values():
            for output in node.outputs().values():
                for connected_input in output.connector_pairs():
                    if connected_input.is_input():
                        conns.append((output, connected_input))

        return conns
