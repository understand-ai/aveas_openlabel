"""Operator input information"""

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
from uai_openlabel import BooleanData, NumberData, no_default


@dataclass
class Interior__HasRider(BooleanData):
    """True iff the vehicle has a rider."""

    val: bool = field(default_factory=lambda: no_default(field="Interior__HasRider.val"), metadata=required)
    """True iff the vehicle has a rider."""

    name: Literal["interior/has_rider"] = field(default="interior/has_rider")
    """Is always 'interior/has_rider'"""


@dataclass
class Interior__SteeringAngle(NumberData):
    """Steering wheel angle (left=positive)"""

    val: float = field(default_factory=lambda: no_default(field="Interior__SteeringAngle.val"), metadata=required)
    """Float of angle in (rad)."""

    name: Literal["interior/steering_angle"] = field(default="interior/steering_angle")
    """Is always 'interior/steering_angle'"""


@dataclass
class Interior__SteeringAngle__UStdDev(NumberData):
    """Uncertainty for `Interior__SteeringAngle` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Interior__SteeringAngle__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["interior/steering_angle/ustddev"] = field(default="interior/steering_angle/ustddev")
    """Is always 'interior/steering_angle/ustddev'."""


@dataclass
class Interior__AutomatedControl__Longitudinal(BooleanData):
    """Boolean indicating automated control of the vehicle.

    True iff the longitudinal motion (acceleration, braking) is at this moment effectively decided / effected by the automated system.
    This includes classical cruise control, ACC, emergency braking and any more advanced SAE Level 3+ system.
    It excludes enhancing systems such as brake boosters, ABS, ESP, and advising systems such as forward collision warning.
    """

    val: bool = field(
        default_factory=lambda: no_default(field="Interior__AutomatedControl__Longitudinal.val"), metadata=required
    )
    """True iff the automated system decides the longitudinal motion at this moment."""

    name: Literal["interior/automated_control/longitudinal"] = field(default="interior/automated_control/longitudinal")
    """Is always 'interior/automated_control/longitudinal'"""


@dataclass
class Interior__AutomatedControl__Lateral(BooleanData):
    """Boolean indicating automated control of the vehicle.

    True iff the lateral motion (steering) is at this moment effectively decided / effected by the automated system.
    This includes lane keeping and lane change assistants, parking steering assistants and any more advanced SAE Level 3+ system.
    It excludes enhancing systems such as power steering or ESP, and advising systems such as lane departure warning.
    """

    val: bool = field(default_factory=lambda: no_default(field="Interior__AutomatedControl__Lateral.val"), metadata=required)
    """True iff the automated system decides the lateral motion at this moment."""

    name: Literal["interior/automated_control/longitudinal"] = field(default="interior/automated_control/longitudinal")
    """Is always 'interior/automated_control/lateral'"""


@dataclass
class Interior__BrakePedal(NumberData):
    """Position of brake pedal.

    Position of brake pedal as range with 1=pedal fully pressed and 0=unpressed.
    """

    val: float = field(default_factory=lambda: no_default(field="Interior__BrakePedal.val"), metadata=required)
    """Proportion of accelerator pedal push position"""

    name: Literal["interior/brake_pedal"] = field(default="interior/brake_pedal")
    """Is always 'interior/brake_pedal'"""

    def __post_init__(self) -> None:
        if self.val < 0.0 or self.val > 1.0:
            raise ValueError("val can only be between 0 and 1.")


@dataclass
class Interior__AcceleratorPedal(NumberData):
    """Position of accelerator pedal.

    Position of accelerator pedal as range with 1=pedal fully pressed and 0=unpressed.
    """

    val: float = field(default_factory=lambda: no_default(field="Interior__AcceleratorPedal.val"), metadata=required)
    """Proportion of accelerator pedal push position"""

    name: Literal["interior/accelerator_pedal"] = field(default="interior/accelerator_pedal")
    """Is always 'interior/accelerator_pedal'"""

    def __post_init__(self) -> None:
        if self.val < 0.0 or self.val > 1.0:
            raise ValueError("val can only be between 0 and 1.")


@dataclass
class Interior__Gear(NumberData):
    """Currently selected gear.

    Currently selected gear, where any positive number indicates the vehicle-specific gear number, and with the following special numbers:
    - 0: Neutral or clutch pedal pushed
    - -1: Reverse
    - -2: Park
    """

    val: int = field(default_factory=lambda: no_default(field="Interior__Gear.val"), metadata=required)
    """Gear value"""

    name: Literal["interior/gear"] = field(default="interior/gear")
    """Is always 'interior/gear'"""


@dataclass
class Interior__Wiper(BooleanData):
    """Boolean indicating if wiper is turned on.

    Boolean attribute that indicates whether the windshield wiper is on. This includes time intervals when the
    wiper is not in motion, but will move again after a fixed interval. It does not include an 'automatic' setting
    when, for absence of rain, the wipers will not move in the foreseeable future.
    """

    val: bool = field(default_factory=lambda: no_default(field="Interior__Wiper.val"), metadata=required)
    """True iff the wipers are on."""

    name: Literal["interior/wiper"] = field(default="interior/wiper")
    """Is always 'interior/wiper'"""
