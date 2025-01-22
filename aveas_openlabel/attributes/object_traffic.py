from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    NumberData,
    no_default,
)


@dataclass
class Density(NumberData):
    """
        Density of the traffic on the road the vehicle is currently on.
    The density of the traffic is the number of vehicles with the center of their bounding box within a 50 m range before and after the vehicle containing this attribute.
    The vehicle containing this attribute is counted as well.
    Measurement unit: m⁻¹
    Value range: [0, ∞]
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="Density.val"), metadata=required)
    """Density"""

    name: Literal["object/traffic/density"] = field(default="object/traffic/density")
    """Is always object/traffic/density"""


@dataclass
class Volume(NumberData):
    """
        Intensity of the traffic on the road section the vehicle is currently on, measured as the number of vehicles entering the road section (across all parallel lanes in the same direction) per unit of time.
    The intensity of the traffic shall be measured over a time frame of 1 minute. The unit of the traffic intensity is vehicles per hour.
    The vehicle containing this attribute shall be counted as well.
    Measurement unit: 1/h
    Value range: [0, ∞]
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="Volume.val"), metadata=required)
    """Volume"""

    name: Literal["object/traffic/volume"] = field(default="object/traffic/volume")
    """Is always object/traffic/volume"""
