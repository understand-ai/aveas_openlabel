"""Contains the dynamic attributes of passive objects on the sidewalk."""

# Copyright © 2024 understandAI GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from dataclasses import dataclass, field
from typing import Union

from apischema.metadata import required
from uai_openlabel import ObjectData as BaseObjectData
from uai_openlabel import no_default

from aveas_openlabel.attribute_enforcer import EachAttributeOnlyOnceEnforcer
from aveas_openlabel.attributes.general import (
    Acceleration,
    Acceleration__UStdDev,
    BoundingBox,
    BoundingBox__UStdDev,
    Velocity,
    Velocity__UStdDev,
)
from aveas_openlabel.attributes.open_drive import (
    OpenDrive__LocalRoadCoordinates,
    OpenDrive__LocalRoadCoordinates__UStdDev,
    OpenDrive__RoadId,
)


@dataclass
class ObjectInFrameData__NonVehicle_NonOperator(BaseObjectData, EachAttributeOnlyOnceEnforcer):
    """
    This class contains dynamic attributes of passive objects on the sidewalk.

    They can be retrieved from the `cuboid`, `text`, and `vec` fields according to their type.
    """

    cuboid: list[BoundingBox] = field(
        default_factory=lambda: no_default(field="ObjectInFrameData__NonVehicle_NonOperator.cuboid"), metadata=required
    )
    """Contains a single cuboid geometry"""

    text: list[OpenDrive__RoadId] = field(
        default_factory=lambda: no_default(field="ObjectInFrameData__NonVehicle_NonOperator.text"), metadata=required
    )
    """Contains all textual attributes"""

    vec: list[
        Union[
            BoundingBox__UStdDev,
            Velocity,
            Velocity__UStdDev,
            Acceleration,
            Acceleration__UStdDev,
            OpenDrive__LocalRoadCoordinates,
            OpenDrive__LocalRoadCoordinates__UStdDev,
        ]
    ] = field(default_factory=lambda: no_default(field="ObjectInFrameData__NonVehicle_NonOperator.vec"), metadata=required)
    """Contains all vectorial attributes"""
