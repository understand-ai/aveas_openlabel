from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    Number,
    NumberData,
    VectorData,
    no_default,
)


@dataclass
class SummarySpeedMax(NumberData):
    """
        Maximum speed (according to norm of object/motion/velocity) of the object over all frames in this slice.
    Measurement unit: m/s
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummarySpeedMax.val"), metadata=required)
    """Summary speed max value"""

    name: Literal["object/summary/speed/max"] = field(default="object/summary/speed/max")
    """Is always object/summary/speed/max"""


@dataclass
class SummarySpeedMin(NumberData):
    """
        Minimum speed (according to norm of object/motion/velocity) of the object over all frames in this slice.
    Measurement unit: m/s
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummarySpeedMin.val"), metadata=required)
    """Summary speed min value"""

    name: Literal["object/summary/speed/min"] = field(default="object/summary/speed/min")
    """Is always object/summary/speed/min"""


@dataclass
class SummaryAccelerationMax(NumberData):
    """
        Maximum acceleration (according to norm of object/motion/acceleration) of the object over all frames in this slice.
    Measurement unit: m/s²
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummaryAccelerationMax.val"), metadata=required)
    """Summary acceleration max value"""

    name: Literal["object/summary/acceleration/max"] = field(default="object/summary/acceleration/max")
    """Is always object/summary/acceleration/max"""


@dataclass
class SummaryAccelerationMin(NumberData):
    """
        Minimum acceleration (according to norm of object/motion/acceleration) of the object over all frames in this slice.
    Measurement unit: m/s²
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummaryAccelerationMin.val"), metadata=required)
    """Summary acceleration min value"""

    name: Literal["object/summary/acceleration/min"] = field(default="object/summary/acceleration/min")
    """Is always object/summary/acceleration/min"""


@dataclass
class SummarySteeringWheelAngleMax(NumberData):
    """
        Maximum steering wheel angle (according to object/interior/steering_wheel_angle) of the object over all frames in this slice.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummarySteeringWheelAngleMax.val"), metadata=required)
    """Summary steering_wheel_angle max value"""

    name: Literal["object/summary/steering_wheel_angle/max"] = field(default="object/summary/steering_wheel_angle/max")
    """Is always object/summary/steering_wheel_angle/max"""


@dataclass
class SummarySteeringWheelAngleMin(NumberData):
    """
        Minimum steering wheel angle (according to object/interior/steering_wheel_angle) of the object over all frames in this slice.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummarySteeringWheelAngleMin.val"), metadata=required)
    """Summary steering_wheel_angle min value"""

    name: Literal["object/summary/steering_wheel_angle/min"] = field(default="object/summary/steering_wheel_angle/min")
    """Is always object/summary/steering_wheel_angle/min"""


@dataclass
class SummaryMeanSteerAngleMax(NumberData):
    """
        Maximum steering angle (according to object/motion/mean_steer_angle) of the object over all frames in this slice.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummaryMeanSteerAngleMax.val"), metadata=required)
    """Summary mean_steer_angle max value"""

    name: Literal["object/summary/mean_steer_angle/max"] = field(default="object/summary/mean_steer_angle/max")
    """Is always object/summary/mean_steer_angle/max"""


@dataclass
class SummaryMeanSteerAngleMin(NumberData):
    """
        Minimum steering angle (according to object/motion/mean_steer_angle) of the object over all frames in this slice.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="SummaryMeanSteerAngleMin.val"), metadata=required)
    """Summary mean_steer_angle min value"""

    name: Literal["object/summary/mean_steer_angle/min"] = field(default="object/summary/mean_steer_angle/min")
    """Is always object/summary/mean_steer_angle/min"""


@dataclass
class SummaryCoordinatesStart(VectorData):
    """
        The (x, y, z) world coordinates of the first frame in this slice.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="SummaryCoordinatesStart.val"), metadata=required
    )
    """Summary coordinates start value"""

    name: Literal["object/summary/coordinates/start"] = field(default="object/summary/coordinates/start")
    """Is always object/summary/coordinates/start"""


@dataclass
class SummaryCoordinatesEnd(VectorData):
    """
        The (x, y, z) world coordinates of the last frame in this slice.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="SummaryCoordinatesEnd.val"), metadata=required
    )
    """Summary coordinates end value"""

    name: Literal["object/summary/coordinates/end"] = field(default="object/summary/coordinates/end")
    """Is always object/summary/coordinates/end"""
