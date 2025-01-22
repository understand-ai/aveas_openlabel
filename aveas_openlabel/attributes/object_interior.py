from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    BooleanData,
    NumberData,
    no_default,
)


@dataclass
class InteriorSteeringWheelAngle(NumberData):
    """
        Steering-wheel angle (CCW), according to DIN ISO 8855.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="InteriorSteeringWheelAngle.val"), metadata=required)
    """Interior steering_wheel_angle value"""

    name: Literal["object/interior/steering_wheel_angle"] = field(default="object/interior/steering_wheel_angle")
    """Is always object/interior/steering_wheel_angle"""


@dataclass
class InteriorGear(NumberData):
    """
        Currently selected gear, where any positive number indicates the vehicle-specific gear number, and non-positive numbers encode special gears.
    Measurement unit: (dimensionless)
    Value range: [-2, ∞]
    Recommended distribution: (none)
    Possible values:
     - 0: Neutral or clutch pedal pushed
     - -1: Reverse
     - -2: Park
    """

    val: int = field(default_factory=lambda: no_default(field="InteriorGear.val"), metadata=required)
    """Interior gear value"""

    name: Literal["object/interior/gear"] = field(default="object/interior/gear")
    """Is always object/interior/gear"""


@dataclass
class InteriorWiper(BooleanData):
    """
        True iff the windshield wiper is on.
    This includes time intervals when the wiper is not in motion, but will move again after a fixed interval. It does not include an ‘automatic’ setting when, for absence of rain, the wipers will not move in the foreseeable future.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="InteriorWiper.val"), metadata=required)
    """Interior wiper value"""

    name: Literal["object/interior/wiper"] = field(default="object/interior/wiper")
    """Is always object/interior/wiper"""


@dataclass
class InteriorPedalBrake(NumberData):
    """
        Position of the brake pedal.
    Measurement unit: (dimensionless)
    Value range: [0, 1]
    Recommended distribution: rectangular
    Possible values:
     - 0: Pedal unpressed.
     - 1: Pedal fully pressed.
    """

    val: float = field(default_factory=lambda: no_default(field="InteriorPedalBrake.val"), metadata=required)
    """Interior pedal brake value"""

    name: Literal["object/interior/pedal/brake"] = field(default="object/interior/pedal/brake")
    """Is always object/interior/pedal/brake"""


@dataclass
class InteriorPedalAccelerator(NumberData):
    """
        Position of the accelerator pedal.
    Measurement unit: (dimensionless)
    Value range: [0, 1]
    Recommended distribution: rectangular
    Possible values:
     - 0: Pedal unpressed.
     - 1: Pedal fully pressed.
    """

    val: float = field(default_factory=lambda: no_default(field="InteriorPedalAccelerator.val"), metadata=required)
    """Interior pedal accelerator value"""

    name: Literal["object/interior/pedal/accelerator"] = field(default="object/interior/pedal/accelerator")
    """Is always object/interior/pedal/accelerator"""


@dataclass
class InteriorPedalClutch(NumberData):
    """
        Position of the clutch pedal.
    Measurement unit: (dimensionless)
    Value range: [0, 1]
    Recommended distribution: rectangular
    Possible values:
     - 0: Pedal unpressed.
     - 1: Pedal fully pressed.
    """

    val: float = field(default_factory=lambda: no_default(field="InteriorPedalClutch.val"), metadata=required)
    """Interior pedal clutch value"""

    name: Literal["object/interior/pedal/clutch"] = field(default="object/interior/pedal/clutch")
    """Is always object/interior/pedal/clutch"""


@dataclass
class InteriorAutomatedControlLongitudinal(BooleanData):
    """
        Boolean indicating automated control of the vehicle in longitudinal direction.
    True iff the longitudinal motion (acceleration, braking) is at this moment effectively decided / effected by the automated system.
    This includes classical cruise control, adaptive cruise control (ACC), automated emergency braking (AEB), and any more advanced SAE Level 3+ system.
    It excludes enhancing systems such as brake boosters, ABS, and advising systems such as forward collision warning.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="InteriorAutomatedControlLongitudinal.val"), metadata=required)
    """Interior automated_control longitudinal value"""

    name: Literal["object/interior/automated_control/longitudinal"] = field(
        default="object/interior/automated_control/longitudinal"
    )
    """Is always object/interior/automated_control/longitudinal"""


@dataclass
class InteriorAutomatedControlLateral(BooleanData):
    """
        Boolean indicating automated control of the vehicle in lateral direction.
    True iff the lateral motion (steering) is at this moment effectively decided / effected by the automated system.
    This includes lane keeping and lane change assistants, parking steering assistants and any more advanced SAE Level 3+ system.
    It excludes enhancing systems such as power steering or ESP, and advising systems such as lane departure warning.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="InteriorAutomatedControlLateral.val"), metadata=required)
    """Interior automated_control lateral value"""

    name: Literal["object/interior/automated_control/lateral"] = field(default="object/interior/automated_control/lateral")
    """Is always object/interior/automated_control/lateral"""
