"""Attributes not belonging to any particular group"""

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

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    BooleanData,
    ObjectUid,
    TextData,
    VectorData,
    no_default,
)
from uai_openlabel import (
    ThreeDBoundingBoxEuler as BaseThreeDBoundingBoxEuler,
)


@dataclass
class BoundingBox(BaseThreeDBoundingBoxEuler):
    """A cuboid in 3D Euclidean space with a pose defined via Euler angles, according to ISO 8855."""

    val: tuple[float, float, float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="BoundingBox.val"), metadata=required
    )
    """
    A tuple of nine floats. 
     - x in (m): The x coordinate of the 3D position of the center of the cuboid.
     - y in (m): The y coordinate of the 3D position of the center of the cuboid.
     - z in (m): The z coordinate of the 3D position of the center of the cuboid.
     - rx in (rad): Euler roll angle (positive: right roll).
     - ry in (rad): Euler pitch angles (positive: pitch down).
     - rz in (rad): Euler yaw angles (positive: yaw left).
     - sx in (m): The x (length) dimension of the cuboid.
     - sy in (m): The y (width) dimension of the cuboid.
     - sz in (m): The z (height) dimension of the cuboid.
    """

    name: Literal["bounding_box"] = field(default="bounding_box")
    """Is always 'bounding_box'."""


@dataclass
class BoundingBox__UStdDev(VectorData):
    """Uncertainty for `BoundingBox` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="BoundingBox__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["bounding_box/ustddev"] = field(default="bounding_box/ustddev")
    """Is always 'bounding_box/ustddev'."""


@dataclass
class Velocity(VectorData):
    """Velocity data of the object."""

    val: tuple[float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Velocity.val"), metadata=required
    )
    """
    A tuple of six floats. 
     - x in (m/s): Velocity of the x (forward) coordinate of the center of the cuboid.
     - y in (m/s): Velocity of the y (left) coordinate of the center of the cuboid.
     - z in (m/s): Velocity of the z (up) coordinate of the center of the cuboid.
     - rx in (rad/s): Velocity of the roll angle.
     - ry in (rad/s): Velocity of the pitch angle.
     - rz in (rad/s): Velocity of the yaw angle.
    """

    name: Literal["velocity"] = field(default="velocity")
    """Is always 'velocity'"""


@dataclass
class Velocity__UStdDev(VectorData):
    """Uncertainty for `Velocity` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Velocity__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["velocity/ustddev"] = field(default="velocity/ustddev")
    """Is always 'velocity/ustddev'."""


@dataclass
class Acceleration(VectorData):
    """Acceleration data of the object."""

    val: tuple[float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Acceleration.val"), metadata=required
    )
    """
    A tuple of six floats. 
     - x in (m/s^2): Acceleration of the x coordinate of the center of the cuboid
     - y in (m/s^2): Acceleration of the y coordinate of the center of the cuboid
     - z in (m/s^2): Acceleration of the z coordinate of the center of the cuboid
     - rx in (rad/s^2): Acceleration of the roll angle.
     - ry in (rad/s^2): Acceleration of the pitch angle.
     - rz in (rad/s^2): Acceleration of the yaw angle.
    """

    name: Literal["acceleration"] = field(default="acceleration")
    """Is always 'acceleration'"""


@dataclass
class Acceleration__UStdDev(VectorData):
    """Uncertainty for `Acceleration` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Acceleration__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["acceleration/ustddev"] = field(default="acceleration/ustddev")
    """Is always 'acceleration/ustddev'."""


@dataclass
class Classification__Uncertainties(VectorData):
    """
    Uncertainty values for the classification of the object.
    """

    val: tuple[float, float, float, float, float, float, float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Classification__Uncertainties.val"), metadata=required
    )
    """Tuple with classification probabilities (must accumulate to 1), in the following order: 
     - animal
     - vehicle/bicycle
     - vehicle/bus
     - vehicle/car
     - human/pedestrian
     - vehicle/mobility_device
     - vehicle/motorcycle
     - other
     - pushable_pullable
     - vehicle/railvehicle
     - vehicle/trailer
     - vehicle/truck
     - vehicle/van
    """

    name: Literal["classification/uncertainties"] = field(default="classification/uncertainties")
    """Is always 'classification/uncertainties'"""

    def __post_init__(self) -> None:
        if not math.isclose(sum(self.val), 1.0):
            raise ValueError(f"Uncertainty values for {self.__class__.__name__} must sum to 1.")


@dataclass
class IsRecorder(BooleanData):
    """Indicates whether the object is the recording entity in this scenario."""

    val: bool = field(default_factory=lambda: no_default(field="IsRecorder.val"), metadata=required)
    """If True, this object is the recording entity of the scenario."""

    name: Literal["is_recorder"] = field(default="is_recorder")
    """Is always 'is_recorder'."""


@dataclass
class AttachedTo(TextData):
    """An attribute for objects that are attached to other objects."""

    val: ObjectUid = field(default_factory=lambda: no_default(field="AttachedTo.val"), metadata=required)
    """The UID of the object this object is attached to."""

    name: Literal["attached_to"] = field(default="attached_to")
    """Is always 'attached_to'."""


@dataclass
class ExactestReferencePointTypeValue(str, Enum):
    """Possible values of 'ExactestReferencePointType'"""

    LEFT = "left"
    """best detection is left road users' side"""

    RIGHT = "right"
    """best detection is right road users' side"""

    FRONT = "front"
    """best detection is road users' front"""

    BACK = "back"
    """best detection is road users' back"""

    CENTRE = "centre"
    """best detection is road users' centre of bbox"""


@dataclass
class ExactestReferencePointType(TextData):
    """The classification of the best detectable bbox-side of road users"""

    val: ExactestReferencePointTypeValue = field(
        default_factory=lambda: no_default(field="ExactestReferencePointType.val"), metadata=required
    )
    """See `ExactestReferencePointTypeValue` for possible values."""

    name: Literal["general/exactest_reference_point_type"] = field(default="general/exactest_reference_point_type")
    """Is always 'general/exactest_reference_point_type'"""


@dataclass
class ExactestReferencePoint(VectorData):
    """Points coordinates of best detectable point of bbox of road users."""

    val: tuple[float, float] = field(default_factory=lambda: no_default(field="ExactestReferencePoint"), metadata=required)
    """x, y coordinates of best detectable point of bbox of road users."""

    name: Literal["general/exactest_reference_point"] = field(default="general/exactest_reference_point")
    """Is always 'general/exactest_reference_point'."""
