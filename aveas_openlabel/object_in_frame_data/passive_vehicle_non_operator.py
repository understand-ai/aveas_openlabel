"""Contains dynamic attributes of passive objects on the road"""

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
from aveas_openlabel.attributes.lights import (
    Lights__Brake,
    Lights__Daytime,
    Lights__Front,
    Lights__HighBeam,
    Lights__Indicator__Left,
    Lights__Indicator__Right,
)
from aveas_openlabel.attributes.open_drive import (
    OpenDrive__LocalRoadCoordinates,
    OpenDrive__LocalRoadCoordinates__UStdDev,
    OpenDrive__RoadId,
)
from aveas_openlabel.attributes.road import (
    Road__Classification,
    Road__NumberLanes__Left__Legal,
    Road__NumberLanes__Left__Physical,
    Road__NumberLanes__Right__Legal,
    Road__NumberLanes__Right__Physical,
)


@dataclass
class ObjectInFrameData__PassiveVehicle_NonOperator(BaseObjectData, EachAttributeOnlyOnceEnforcer):
    """
    This class contains dynamic attributes of passive objects on the road.

    They can be retrieved from the `cuboid`, `boolean`, `num`, `text`, and `vec` fields according to their type.
    """

    boolean: list[
        Union[
            Lights__Brake,
            Lights__Indicator__Left,
            Lights__Indicator__Right,
            Lights__Front,
            Lights__Daytime,
            Lights__HighBeam,
        ]
    ] = field(
        default_factory=lambda: no_default(field="ObjectInFrameData__PassiveVehicle_NonOperator.boolean"), metadata=required
    )
    """Contains all boolean attributes"""

    cuboid: list[BoundingBox] = field(
        default_factory=lambda: no_default(field="ObjectInFrameData__PassiveVehicle_NonOperator.cuboid"), metadata=required
    )
    """Contains a single cuboid geometry"""

    num: list[
        Union[
            Road__NumberLanes__Left__Legal,
            Road__NumberLanes__Left__Physical,
            Road__NumberLanes__Right__Legal,
            Road__NumberLanes__Right__Physical,
        ]
    ] = field(default_factory=lambda: no_default(field="ObjectInFrameData__PassiveVehicle_NonOperator.num"), metadata=required)
    """Contains all numeric attributes"""

    text: list[Union[OpenDrive__RoadId, Road__Classification]] = field(
        default_factory=lambda: no_default(field="ObjectInFrameData__PassiveVehicle_NonOperator.text"), metadata=required
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
    ] = field(default_factory=lambda: no_default(field="ObjectInFrameData__PassiveVehicle_NonOperator.vec"), metadata=required)
    """Contains all vectorial attributes"""
