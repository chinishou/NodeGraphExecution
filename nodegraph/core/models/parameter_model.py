"""
Parameter Model
===============

Represents a parameter on a node.
Parameters are editable properties that control node behavior and data.
"""

from typing import Any, Optional


class ParameterModel:
    """
    Data model for a node parameter.

    Parameters are the editable properties of a node.

    Attributes:
        name: Parameter identifier
        display_name: Human-readable name
        value: Current parameter value
        default_value: Default value
        data_type: Type of the parameter (int, float, string, List of options for choice/enum types etc.)
        min_value: Minimum value (for numeric types)
        max_value: Maximum value (for numeric types)
        description: Parameter description/tooltip
    """

    def __init__(
        self,
        name: str,
        data_type: type = None,
        default_value: Any = None,
        display_name: Optional[str] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        description: str = "",
    ):
        self.name = name
        self.data_type = data_type
        self.value = default_value
        self.default_value = default_value
        self.display_name = display_name or name
        self.min_value = min_value
        self.max_value = max_value
        self.description = description

    def __repr__(self) -> str:
        return f"ParameterModel(name='{self.name}', type='{self.data_type}', value={self.value})"
