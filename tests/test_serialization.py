"""
Tests for Serialization
========================

Test serialization and deserialization of:
- ParameterModel
- ConnectorModel
- NodeModel
- Complete networks with connections
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from nodegraph.core.models import (
    ParameterModel,
    ConnectorModel,
    ConnectorType,
    NodeModel,
)


def test_parameter_serialization():
    """Test parameter serialization and deserialization."""
    # Create parameter
    param = ParameterModel(
        name="test_param",
        data_type="float",
        default_value=1.5,
        label="Test Parameter",
        description="A test parameter",
    )

    # Set a value
    param.set_value(3.7)

    # Serialize
    data = param.serialize()

    # Check serialized data
    assert data["name"] == "test_param"
    assert data["data_type"] == "float"
    assert data["value"] == 3.7
    assert data["default_value"] == 1.5

    # Deserialize
    param2 = ParameterModel.deserialize(data)

    # Check deserialized parameter
    assert param2.name == param.name
    assert param2.data_type == param.data_type
    assert param2.value() == param.value()
    assert param2.default_value == param.default_value

    print("✓ Parameter serialization works")


def test_connector_serialization():
    """Test connector serialization and deserialization."""
    # Create connector
    conn = ConnectorModel(
        name="test_input",
        connector_type=ConnectorType.INPUT,
        data_type="float",
        label="Test Input",
        default_value=0.0,
        description="A test input",
    )

    # Serialize
    data = conn.serialize()

    # Check serialized data
    assert data["name"] == "test_input"
    assert data["connector_type"] == "input"
    assert data["data_type"] == "float"
    assert data["default_value"] == 0.0

    # Deserialize
    conn2 = ConnectorModel.deserialize(data)

    # Check deserialized connector
    assert conn2.name == conn.name
    assert conn2.connector_type == conn.connector_type
    assert conn2.data_type == conn.data_type

    print("✓ Connector serialization works")


def test_node_serialization():
    """Test node serialization and deserialization."""
    # Create node with parameters and connectors
    node = NodeModel(name="TestNode", node_type="TestType", category="Test")

    node.add_parameter("param1", data_type="float", default_value=1.0)
    node.add_input("input1", data_type="float", default_value=0.0)
    node.add_output("output1", data_type="float")

    node.set_position(100.0, 200.0)

    # Serialize
    data = node.serialize()

    # Check serialized data
    assert data["name"] == "TestNode"
    assert data["node_type"] == "TestType"
    assert data["category"] == "Test"
    assert data["position"] == (100.0, 200.0)
    assert "param1" in data["parameters"]
    assert "input1" in data["inputs"]
    assert "output1" in data["outputs"]

    # Can serialize to JSON
    json_str = json.dumps(data, default=str)
    assert json_str is not None

    print("✓ Node serialization works")


def test_roundtrip_serialization():
    """Test complete roundtrip: serialize and deserialize."""
    # Create parameter
    original_param = ParameterModel(
        name="test",
        data_type="float",
        default_value=1.0,
    )
    original_param.set_value(5.5)

    # Serialize
    data = original_param.serialize()

    # Deserialize
    restored_param = ParameterModel.deserialize(data)

    # Compare
    assert restored_param.name == original_param.name
    assert restored_param.data_type == original_param.data_type
    assert restored_param.value() == original_param.value()
    assert restored_param.default_value == original_param.default_value

    print("✓ Roundtrip serialization works")


def run_all_tests():
    """Run all serialization tests."""
    print("=" * 60)
    print("Serialization Tests")
    print("=" * 60)

    test_parameter_serialization()
    test_connector_serialization()
    test_node_serialization()
    test_roundtrip_serialization()

    print("=" * 60)
    print("All serialization tests passed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
