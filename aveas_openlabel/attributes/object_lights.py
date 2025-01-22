from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    BooleanData,
    no_default,
)


@dataclass
class LightsBrake(BooleanData):
    """
        True iff the brake lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsBrake.val"), metadata=required)
    """Lights brake value"""

    name: Literal["object/lights/brake"] = field(default="object/lights/brake")
    """Is always object/lights/brake"""


@dataclass
class LightsFront(BooleanData):
    """
        True iff the front lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsFront.val"), metadata=required)
    """Lights front value"""

    name: Literal["object/lights/front"] = field(default="object/lights/front")
    """Is always object/lights/front"""


@dataclass
class LightsDaytime(BooleanData):
    """
        True iff the daytime lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsDaytime.val"), metadata=required)
    """Lights daytime value"""

    name: Literal["object/lights/daytime"] = field(default="object/lights/daytime")
    """Is always object/lights/daytime"""


@dataclass
class LightsHighbeam(BooleanData):
    """
        True iff the high-beam lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsHighbeam.val"), metadata=required)
    """Lights highbeam value"""

    name: Literal["object/lights/highbeam"] = field(default="object/lights/highbeam")
    """Is always object/lights/highbeam"""


@dataclass
class LightsEmergency(BooleanData):
    """
        True iff the emergency vehicle lights are on. This refers to vehicle-specific lights according to the classification in object/characteristics/special_purpose. For hazard lights, see object/lights/indicator/left and object/lights/indicator/right.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsEmergency.val"), metadata=required)
    """Lights emergency value"""

    name: Literal["object/lights/emergency"] = field(default="object/lights/emergency")
    """Is always object/lights/emergency"""


@dataclass
class LightsIndicatorLeft(BooleanData):
    """
        True iff the left turning signal indicator light is on.
    This attribute follows the value of the indicator light switch and not the light itself, i.e., this attribute stays True throughout the entire blinking process.
    When both left and right indicators are on at the same time, this implies the vehicle’s hazard lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsIndicatorLeft.val"), metadata=required)
    """Lights indicator left value"""

    name: Literal["object/lights/indicator/left"] = field(default="object/lights/indicator/left")
    """Is always object/lights/indicator/left"""


@dataclass
class LightsIndicatorRight(BooleanData):
    """
        True iff the right turning signal indicator light is on.
    This attribute follows the value of the indicator light switch and not the light itself, i.e., this attribute stays True throughout the entire blinking process.
    When both left and right indicators are on at the same time, this implies the vehicle’s hazard lights are on.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="LightsIndicatorRight.val"), metadata=required)
    """Lights indicator right value"""

    name: Literal["object/lights/indicator/right"] = field(default="object/lights/indicator/right")
    """Is always object/lights/indicator/right"""
