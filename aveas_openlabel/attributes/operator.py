"""Information on the human operator"""

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
    ObjectUid,
    TextData,
    VectorData,
    no_default,
)


@dataclass
class Operator__HeadRotation(NumberData):
    """Angle between head direction and forward direction of the vehicle in (rad), left=positive."""

    val: float = field(default_factory=lambda: no_default(field="Operator__HeadRotation.val"), metadata=required)
    """Angle between head direction and forward direction of the vehicle in (rad), left=positive."""

    name: Literal["operator/head_rotation"] = field(default="operator/head_rotation")
    """Is always 'operator/head_rotation'"""


@dataclass
class Operator__HeadRotation__UStdDev(NumberData):
    """Uncertainty for `Operator__HeadRotation` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Operator__HeadRotation__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["operator/head_rotation/ustddev"] = field(default="operator/head_rotation/ustddev")
    """Is always 'operator/head_rotation/ustddev'."""


@dataclass
class Operator__FocussedPoint(VectorData):
    """
    Tuple of the viewed (x,y,z) coordinates in vehicle coordinates of the object that the operator is focussing on.
    Is defined by extending the viewing beam from the operators' eyes into the surrounding 3D world to derive the target point.
    """

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__FocussedPoint.val"), metadata=required
    )
    """The (x,y,z) coordinates of the focussed point."""

    name: Literal["operator/focussed_point"] = field(default="operator/focussed_point")
    """Is always 'operator/focussed_point'"""


@dataclass
class Operator__FocussedPoint__UStdDev(VectorData):
    """Uncertainty for `Operator__FocussedPoint` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__FocussedPoint__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["operator/focussed_point/ustddev"] = field(default="operator/focussed_point/ustddev")
    """Is always 'operator/focussed_point/ustddev'."""


@dataclass
class Operator__ViewingAngle(NumberData):
    """Drivers eye viewing angle as the angle between the top edge of the hood and the horizon, in (rad)."""

    val: float = field(default_factory=lambda: no_default(field="Operator__ViewingAngle.val"), metadata=required)
    """Drivers eye viewing angle as the angle between the top edge of the hood and the horizon, in (rad)."""

    name: Literal["operator/viewing_angle"] = field(default="operator/viewing_angle")
    """Is always 'operator/viewing_angle'"""


class Operator__FocussedObjectValue(str, Enum):
    """Possible values of `Operator__FocussedObject`"""

    LEADING_VEHICLE = "leading_vehicle"
    """Focussed object is the vehicle in front of the operator"""

    COLLIDING_VEHICLE = "colliding_vehicle"
    """Focussed object is a vehicle in the scene having a collision"""

    GENERIC_VEHICLE = "generic_vehicle"
    """Focussed object is a generic vehicle in the scene"""

    SIGNAL = "signal"
    """Focussed object is a traffic signal"""

    CENTER_DISPLAY = "center_display"
    """Focussed object is the vehicle-inter center display"""

    INSTRUMENT_CLUSTER = "instrument_cluster"
    """Focussed object is the vehicle-inter instrument cluster"""

    HUD = "hud"
    """Focussed object is the vehicle-inter head-up display"""

    OTHER_DISPLAY = "other_display"
    """Focussed object is another vehicle-inter head-up display"""

    LEFT_MIRROR = "left_mirror"
    """Focussed object is the left rear-view mirror"""

    RIGHT_MIRROR = "right_mirror"
    """Focussed object is the right rear-view mirror"""

    OTHER_INTERIOR = "other_interior"
    """Focussed object is another object in the vehicle's interior (or on the vehicle's body)"""

    OTHER_EXTERIOR = "other_exterior"
    """Focussed object is another exterior object"""


@dataclass
class Operator__FocussedObject(TextData):
    """Object the operator is focussing on."""

    val: Operator__FocussedObjectValue = field(
        default_factory=lambda: no_default(field="Operator__FocussedObject.val"), metadata=required
    )
    """See `Operator__FocussedObjectValue` for possible values. """

    name: Literal["operator/focussed_object"] = field(default="operator/focussed_object")
    """Is always 'operator/focussed_object'"""


@dataclass
class Operator__FocussedObject__Uncertainties(VectorData):
    """
    Uncertainty values for `Operator__FocussedObject` (must accumulate to 1)
    """

    val: tuple[float, float, float, float, float, float, float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__FocussedObject__Uncertainties.val"), metadata=required
    )
    """Tuple with class probabilities (must accumulate to 1), in the following order: 
     - leading_vehicle
     - colliding_vehicle
     - generic_vehicle
     - signal
     - center_display
     - instrument_cluster
     - other_display
     - hud
     - other_display
     - left_mirror
     - right_mirror
     - other_interior
     - other_exterior
    """

    name: Literal["operator/focussed_object/uncertainties"] = field(default="operator/focussed_object/uncertainties")
    """Is always 'operator/focussed_object/uncertainties'"""


@dataclass
class Operator__FocussedObject__Id(TextData):
    """
    ID of the object the operator is focussing on. Can be used to index the `AveasOpenLabel.objects` field.
    Is only provided if the object the operator is focussing on is indexed in this file.
    """

    val: ObjectUid = field(default_factory=lambda: no_default(field="Operator__FocussedObject__Id.val"), metadata=required)
    """ID of the focussed object."""

    name: Literal["operator/focussed_object/id"] = field(default="operator/focussed_object/id")
    """Is always 'operator/focussed_object/id'"""


@dataclass
class Operator__Pupil(VectorData):
    """Tuple of pupil-specific information for the operator"""

    val: tuple[float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__Pupil.val"), metadata=required
    )
    """Tuple with information on:
    1. left pupil diameter in (mm)
    2. right pupil diameter in (mm)
    3. left iris diameter in (mm)
    4. right iris diameter in (mm)
    5. left openness range
    6. right openness range
    7. focus stability range"""
    # TODO/JZ: Was bedeutet "openness range"

    name: Literal["operator/pupil"] = field(default="operator/pupil")
    """Is always 'operator/pupil'"""


@dataclass
class Operator__Pupil__UStdDev(VectorData):
    """Uncertainty for `Operator__Pupil` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__Pupil__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["operator/pupil/ustddev"] = field(default="operator/pupil/ustddev")
    """Is always 'operator/pupil/ustddev'."""


class Operator__HandInteractionAreaValue(str, Enum):
    """Possible values of `Operator__HandInteractionArea`."""

    STEERING_WHEEL = "steering_wheel"
    """Hand is on steering wheel"""

    CENTER_DISPLAY = "center_display"
    """Hand is on center display"""

    ARMREST = "armrest"
    """Hand is on armrest"""

    OTHER = "other"
    """Hand is on other element"""


@dataclass
class Operator__HandInteractionArea(VectorData):
    """Tuple of the left and right hand interaction area. See `Operator__HandInteractionAreaValue` for possible values."""

    val: tuple[Operator__HandInteractionAreaValue, Operator__HandInteractionAreaValue] = field(
        default_factory=lambda: no_default(field="Operator__HandInteractionArea.val"), metadata=required
    )
    """ Tuple of the left and right hand interaction area"""

    name: Literal["operator/hand_interaction_area"] = field(default="operator/hand_interaction_area")
    """Is always 'operator/hand_interaction_area'"""


@dataclass
class Operator__SixDoFRotationAndAcceleration(VectorData):
    """For simulation studies: Current parameters to a six-degrees-of-freedom physical driving simulator, if used.

    This can be used to evaluate the settings of a suitable physical driving simulator (e.g. a hexapod),
    which is the seat of the driving simulator and can exert forces onto the participant. For physical limitations,
    these values may differ from the actual physical properties of the simulated vehicle.
    """

    val: tuple[float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__SixDoFRotationAndAcceleration.val"), metadata=required
    )
    """Tuple with information: 
     - x in (m/s^2): Acceleration in x direction.
     - y in (m/s^2): Acceleration in y direction.
     - z in (m/s^2): Acceleration in z direction.
     - rz in (rad): Euler yaw angles (positive: yaw left).
     - ry in (rad): Euler pitch angles (positive: pitch down).
     - rx in (rad): Euler roll angle (positive: right roll).
    """

    name: Literal["operator/six_dof_rotation_and_acceleration"] = field(default="operator/six_dof_rotation_and_acceleration")
    """Is always 'operator/six_dof_rotation_and_acceleration'"""


@dataclass
class Operator__Age(NumberData):
    """Age of the vehicle's operator in years"""

    val: int = field(default_factory=lambda: no_default(field="Operator__Age.val"), metadata=required)
    """Age of the vehicle's operator in years"""

    name: Literal["operator/age"] = field(default="operator/age")
    """Is always 'operator/age'"""


class Operator__GenderValue(str, Enum):
    """Possible values of `Operator__Gender`."""

    MALE = "male"
    """male operator"""

    FEMALE = "female"
    """female operator"""

    DIVERSE = "diverse"
    """diverse operator"""


@dataclass
class Operator__Gender(TextData):
    """Gender of the vehicle operator"""

    val: Operator__GenderValue = field(default_factory=lambda: no_default(field="Operator__Gender.val"), metadata=required)
    """See `Operator__GenderValue` for possible values."""

    name: Literal["operator/gender"] = field(default="operator/gender")
    """Is always 'operator/gender'"""


@dataclass
class Operator__Personality(
    VectorData
):  # TODO: Wenn es drin bleiben soll, brauchen wir Quellen / Berechnungsvorschriften für alle diese Felder.
    """Tuple of the vehicle operator's personality scores"""

    val: tuple[float, float, float, float, float, float, float, float, float, float] = field(
        default_factory=lambda: no_default(field="Operator__Personality.val"), metadata=required
    )
    """
    tuple with information: 
     - openness score (lowerCI,upperCI) 
     - conscientiousness score (lowerCI,upperCI) 
     - extraversion score (lowerCI,upperCI) 
     - agreeableness score (lowerCI,upperCI) 
     - neuroticism score (lowerCI,upperCI)
     """

    name: Literal["operator/personality"] = field(default="operator/personality")
    """Is always 'operator/personality'"""


@dataclass
class Operator__BodyHeight(NumberData):
    """Body height of the vehicle operator in (m)"""

    val: float = field(default_factory=lambda: no_default(field="Operator__BodyHeight.val"), metadata=required)
    """Body height of the vehicle operator in (m)"""

    name: Literal["operator/body_height"] = field(default="operator/body_height")
    """Is always 'operator/body_height'"""
