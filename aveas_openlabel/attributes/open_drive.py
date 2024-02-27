"""Attributes referencing the object to the OpenDRIVE map"""

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
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    TextData,
    VectorData,
    no_default,
)


@dataclass
class OpenDrive__RoadId(TextData):
    """Road ID in the OpenDRIVE file that the local road coordinates are referencing"""

    val: str = field(default_factory=lambda: no_default(field="OpenDrive__RoadId.val"), metadata=required)
    """The OpenDRIVE road ID"""

    name: Literal["used_road_link"] = field(default="used_road_link")
    """Is always 'open_drive/road_id'"""


@dataclass
class OpenDrive__LocalRoadCoordinates(VectorData):
    """The bounding box position in the local road coordinates as defined in OpenDRIVE"""

    val: tuple[float, float] = field(
        default_factory=lambda: no_default(field="OpenDrive__LocalRoadCoordinates.val"), metadata=required
    )
    """The (s, t) tuple of the local road coordinates ."""

    name: Literal["local_road_coordinates"] = field(default="local_road_coordinates")
    """Is always 'open_drive/local_road_coordinates'"""


@dataclass
class OpenDrive__LocalRoadCoordinates__UStdDev(VectorData):
    """Uncertainty for `OpenDrive__LocalRoadCoordinates` as standard deviation around the parent indicated value."""

    val: tuple[float, float] = field(
        default_factory=lambda: no_default(field="OpenDrive__LocalRoadCoordinates__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["open_drive/local_road_coordinates/ustddev"] = field(default="open_drive/local_road_coordinates/ustddev")
    """Is always 'open_drive/local_road_coordinates/ustddev'."""
