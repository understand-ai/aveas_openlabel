"""Information about the road the object is on"""

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
from enum import Enum
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    NumberData,
    TextData,
    no_default,
)


@dataclass
class Road__SpeedLimit(NumberData):
    """Applicable speed limit for the vehicle at its current position in (m/s).
    0 indicates no speed limit (i.e. unlimited)."""

    val: float = field(default_factory=lambda: no_default(field="Road__SpeedLimit.val"), metadata=required)
    """Speed limit value in (m/s)"""

    name: Literal["road/speed_limit"] = field(default="road/speed_limit")
    """Is always 'road/speed_limit'"""


class Road__ClassificationValue(str, Enum):
    """Possible values of 'track_section'"""

    STRAIGHT = "straight"
    """A straight road section"""

    CURVE = "curve"
    """A curving road section"""

    T_INTERSECTION = "t_intersection"
    """A T intersection"""

    X_INTERSECTION = "x_intersection"
    """A crossing"""

    ROUNDABOUT = "roundabout"
    """A roundabout"""

    PARKING_AREA = "parking_area"
    """A parking lot or area"""

    PROPERTY_ENTRANCE = "property_entrance"
    """A property entrance"""


@dataclass
class Road__Classification(TextData):
    """The classification of the current road section"""

    val: Road__ClassificationValue = field(
        default_factory=lambda: no_default(field="Road__Classification.val"), metadata=required
    )
    """See `Road__ClassificationValue` for possible values."""

    name: Literal["road/classification"] = field(default="road/classification")
    """Is always 'road/classification'"""


@dataclass
class Road__NumberLanes__Left__Legal(NumberData):
    """Number of lanes left of vehicle's position that the vehicle is legally permitted to use.

    A value of -1 means that this attribute is not applicable.
    A lane change occurs when the center of the bounding box crosses the lane boundary.
    """

    val: int = field(default_factory=lambda: no_default(field="Road__NumberLanes__Left__Legal.val"), metadata=required)
    """Number of lanes left of vehicle's position that the vehicle is legally permitted to use."""

    name: Literal["road/number_lanes/left/legal"] = field(default="road/number_lanes/left/legal")
    """Is always 'road/number_lanes/left/legal'"""


@dataclass
class Road__NumberLanes__Left__Physical(NumberData):
    """
    Number of lanes left of vehicle's position that the vehicle can physically reach, excluding its current lane.
    This includes lanes the vehicle is not allowed to drive on.

    A value of -1 means that this attribute is not applicable.
    A lane change occurs when the center of the bounding box crosses the lane boundary.
    """

    val: int = field(default_factory=lambda: no_default(field="Road__NumberLanes__Left__Physical.val"), metadata=required)
    """Number of lanes left of vehicle's position that the vehicle can physically reach, excluding its current lane."""

    name: Literal["road/number_lanes/left/physical"] = field(default="road/number_lanes/left/physical")
    """Is always 'road/number_lanes/left/physical'"""


@dataclass
class Road__NumberLanes__Right__Legal(NumberData):
    """Number of lanes right of vehicle's position that the vehicle is legally permitted to use.

    A value of -1 means that this attribute is not applicable.
    A lane change occurs when the center of the bounding box crosses the lane boundary.
    """

    val: int = field(default_factory=lambda: no_default(field="Road__NumberLanes__Right__Legal.val"), metadata=required)
    """Number of lanes right of vehicle's position that the vehicle is legally permitted to use."""

    name: Literal["road/number_lanes/right/legal"] = field(default="road/number_lanes/right/legal")
    """Is always 'road/number_lanes/right/legal'"""


@dataclass
class Road__NumberLanes__Right__Physical(NumberData):
    """
    Number of lanes right of vehicle's position that the vehicle can physically reach, excluding its current lane.
    This includes lanes the vehicle is not allowed to drive on.

    A value of -1 means that this attribute is not applicable.
    A lane change occurs when the center of the bounding box crosses the lane boundary.
    """

    val: int = field(default_factory=lambda: no_default(field="Road__NumberLanes__Right__Physical.val"), metadata=required)
    """Integer number of lanes"""

    name: Literal["road/number_lanes/right/physical"] = field(default="road/number_lanes/right/physical")
    """Is always 'road/number_lanes/right/physical'"""
