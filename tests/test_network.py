"""
Tests for NetworkModel
======================

Test the network management system including:
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from nodegraph.core.models import NetworkModel, NodeModel


def test_network_creation():
    """Test creating a network."""
    network = NetworkModel(name="TestNetwork")

    assert network.name == "TestNetwork"
    assert len(network.nodes()) == 0
    assert len(network.connector_pairs()) == 0

    print("✓ Network creation works")


def run_all_tests():
    """Run all network tests."""
    print("=" * 60)
    print("NetworkModel Tests")
    print("=" * 60)

    test_network_creation()

    print("=" * 60)
    print("All NetworkModel tests passed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
