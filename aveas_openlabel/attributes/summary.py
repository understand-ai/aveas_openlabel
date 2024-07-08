"""Summarizing information of the object over the entire scenario"""

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
from uai_openlabel import NumberData, NumberType, VectorData, no_default


@dataclass
class Summary__Speed__Max(NumberData):
    """Maximum speed of the object over all frames in this file in (m/s)."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Speed__Max.val"), metadata=required)
    """Maximum speed of the object in (m/s)."""

    name: Literal["summary/speed/max"] = field(default="summary/speed/max")
    """Is always 'summary/speed/max'"""


@dataclass
class Summary__Speed__Max__UStdDev(NumberData):
    """Uncertainty for `Summary__Speed__Max` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Speed__Max__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/speed/max/ustddev"] = field(default="summary/speed/max/ustddev")
    """Is always 'summary/speed/max/ustddev'."""


@dataclass
class Summary__Speed__Min(NumberData):
    """Minimum speed of the object over all frames in this file in (m/s)."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Speed__Min.val"), metadata=required)
    """Minimum speed of the object in (m/s)."""

    name: Literal["summary/speed/min"] = field(default="summary/speed/min")
    """Is always 'summary/speed/min'"""


@dataclass
class Summary__Speed__Min__UStdDev(NumberData):
    """Uncertainty for `Summary__Speed__Min` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Speed__Min__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/speed/min/ustddev"] = field(default="summary/speed/min/ustddev")
    """Is always 'summary/speed/min/ustddev'."""


@dataclass
class Summary__Accel__Max(NumberData):
    """Maximum acceleration of the object over all frames in this file in (m/s^2)."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Accel__Max.val"), metadata=required)
    """Maximum acceleration of the object in (m/s^2)."""

    name: Literal["summary/accel/max"] = field(default="summary/accel/max")
    """Is always 'summary/accel/max'"""

    type: Literal[NumberType.Value] = field(default=NumberType.Value)
    """Is always 'value'"""


@dataclass
class Summary__Accel__Max__UStdDev(NumberData):
    """Uncertainty for `Summary__Accel__Max` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Accel__Max__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/accel/max/ustddev"] = field(default="summary/accel/max/ustddev")
    """Is always 'summary/accel/max/ustddev'."""


@dataclass
class Summary__Accel__Min(NumberData):
    """Minimum acceleration (strongest deceleration if negative) of the object over all frames in this file in (m/s^2)."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Accel__Min.val"), metadata=required)
    """Minimum acceleration of the object in (m/s^2)."""

    name: Literal["summary/accel/min"] = field(default="summary/accel/min")
    """Is always 'summary/accel/min'"""

    type: Literal[NumberType.Value] = field(default=NumberType.Value)
    """Is always 'value'"""


@dataclass
class Summary__Accel__Min__UStdDev(NumberData):
    """Uncertainty for `Summary__Accel__Min` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__Speed__Min__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/accel/min/ustddev"] = field(default="summary/accel/min/ustddev")
    """Is always 'summary/accel/min/ustddev'."""


@dataclass
class Summary__SteeringWheelAngle__Max(NumberData):
    """Maximum steering wheel angle of the object over all frames in this file."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringWheelAngle__Max.val"), metadata=required)
    """Maximum steering wheel angle in radians, counter clockwise."""

    name: Literal["summary/steering_wheel_angle/max"] = field(default="summary/steering_wheel_angle/max")
    """Is always 'summary/steering_wheel_angle/max'"""


@dataclass
class Summary__SteeringWheelAngle__Max__UStdDev(NumberData):
    """Uncertainty for `Summary__SteeringWheelAngle__Max` as standard deviation around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Summary__SteeringWheelAngle__Max__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/steering_wheel_angle/max/ustddev"] = field(default="summary/steering_wheel_angle/max/ustddev")
    """Is always 'summary/steering_wheel_angle/max/ustddev'."""


@dataclass
class Summary__SteeringWheelAngle__Min(NumberData):
    """Minimum steering wheel angle of the object over all frames in this file."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringWheelAngle__Min.val"), metadata=required)
    """Minimum steering wheel angle in radians, counter clockwise."""

    name: Literal["summary/steering_wheel_angle/min"] = field(default="summary/steering_wheel_angle/min")
    """Is always 'summary/steering_wheel_angle/min'"""


@dataclass
class Summary__SteeringWheelAngle__Min__UStdDev(NumberData):
    """Uncertainty for `Summary__SteeringWheelAngle__Min` as standard deviation around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Summary__SteeringWheelAngle__Min__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/steering_wheel_angle/min/ustddev"] = field(default="summary/steering_wheel_angle/min/ustddev")
    """Is always 'summary/steering_wheel_angle/min/ustddev'."""


@dataclass
class Summary__SteeringAngle__Max(NumberData):
    """Maximum steering angle (i.e. tire angle) of the object over all frames in this file."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringAngle__Max.val"), metadata=required)
    """Maximum steering angle in radians, counter clockwise."""

    name: Literal["summary/steering_angle/max"] = field(default="summary/steering_angle/max")
    """Is always 'summary/steering_angle/max'"""


@dataclass
class Summary__SteeringAngle__Max__UStdDev(NumberData):
    """Uncertainty for `Summary__SteeringAngle__Max` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringAngle__Max__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/steering_angle/max/ustddev"] = field(default="summary/steering_angle/max/ustddev")
    """Is always 'summary/steering_angle/max/ustddev'."""


@dataclass
class Summary__SteeringAngle__Min(NumberData):
    """Minimum steering angle (i.e. tire angle) of the object over all frames in this file."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringAngle__Min"), metadata=required)
    """Minimum steering angle in radians, counter clockwise."""

    name: Literal["summary/steering_angle/min"] = field(default="summary/steering_angle/min")
    """Is always 'summary/steering_angle/min'"""


@dataclass
class Summary__SteeringAngle__Min__UStdDev(NumberData):
    """Uncertainty for `Summary__SteeringAngle__Min` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Summary__SteeringAngle__Min__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/steering_angle/min/ustddev"] = field(default="summary/steering_angle/min/ustddev")
    """Is always 'summary/steering_angle/min/ustddev'."""


@dataclass
class Summary__Coordinates__ScenarioStart(VectorData):
    """Coordinate of the first frame in this file (in world coordinates)"""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Summary__Coordinates__ScenarioStart.val"), metadata=required
    )
    """The (x, y, z) coordinates of the first frame of this object (m)."""

    name: Literal["summary/coordinates/scenario_start"] = field(default="summary/coordinates/scenario_start")
    """Is always 'summary/coordinates/scenario_start'"""


@dataclass
class Summary__Coordinates__ScenarioStart__UStdDev(VectorData):
    """Uncertainty for `Summary__Coordinates__ScenarioStart` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Summary__Coordinates__ScenarioStart__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/coordinates/scenario_start/ustddev"] = field(default="summary/coordinates/scenario_start/ustddev")
    """Is always 'summary/coordinates/scenario_start/ustddev'."""


@dataclass
class Summary__Coordinates__ScenarioEnd(VectorData):
    """Coordinate of the last frame in this file (in world coordinates)"""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Summary__Coordinates__ScenarioEnd.val"), metadata=required
    )
    """The (x, y, z) coordinates of the last frame of this object (m)."""

    name: Literal["summary/coordinates/scenario_end"] = field(default="summary/coordinates/scenario_end")
    """Is always 'summary/coordinates/scenario_end'"""


@dataclass
class Summary__Coordinates__ScenarioEnd__UStdDev(VectorData):
    """Uncertainty for `Summary__Coordinates__ScenarioEnd` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Summary__Coordinates__ScenarioEnd__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["summary/coordinates/scenario_end/ustddev"] = field(default="summary/coordinates/scenario_end/ustddev")
    """Is always 'summary/coordinates/scenario_end/ustddev'."""
