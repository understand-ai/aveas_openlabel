
from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    BooleanData,
    no_default,
    NumberData,
    Number, 
    ObjectUid,
    TextData,
    VectorData,
    ThreeDBoundingBoxEuler, 
)


@dataclass
class BoundingBox(ThreeDBoundingBoxEuler):
    """
    A cuboid in 3D Euclidean space with a position defined in world coordinates and an orientation defined via Euler angles.
For vehicles, the bounding box shall be aligned with the vehicle coordinates according to ISO 8855. The width shall be chosen in accordance with the annotation / labeling guidelines ['], namely such that an overlap of the outlines of two vehicles typically implies a critical collision between the vehicles. Side-view mirrors and antennas, for example, should typically omitted.
This parameter is the primary source for object position data and hence strongly recommended.
Measurement unit: (complex)
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[float, float, float, float, float, float, float, float, float] = field(default_factory=lambda: no_default(field="BoundingBox.val"), metadata=required)
    """Bounding box"""

    name: Literal["object/motion/bounding_box"] = field(default="object/motion/bounding_box")
    """Is always object/motion/bounding_box"""


@dataclass
class BoundingBoxMaximumExtents(ThreeDBoundingBoxEuler):
    """
    Bounding box over the maximum extents of the object, including smaller or soft parts, such as antennas and side-view mirrors for vehicles, which are omitted in object/motion/bounding_box.
It shall be aligned as object/motion/bounding_box, however, the position may differ to shift the center point of the bounding box.
Measurement unit: (complex)
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[float, float, float, float, float, float, float, float, float] = field(default_factory=lambda: no_default(field="BoundingBoxMaximumExtents.val"), metadata=required)
    """Bounding box (maximum extents)"""

    name: Literal["object/motion/bounding_box_max"] = field(default="object/motion/bounding_box_max")
    """Is always object/motion/bounding_box_max"""


@dataclass
class BestDetectedSide(TextData):
    """
    The classification of the best (most accurately) detected 2D bounding box side of the object.
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: (none)
LEFT: The object's left side is detected best.
RIGHT: The object's right side is detected best.
FRONT: The object's front side is detected best.
BACK: The object's back side is detected best.
CENTER: The object's center is detected best.
    """
    val: str = field(default_factory=lambda: no_default(field="BestDetectedSide.val"), metadata=required)
    """Best detected side"""

    name: Literal["object/motion/best_detected_side"] = field(default="object/motion/best_detected_side")
    """Is always object/motion/best_detected_side"""


@dataclass
class BestDetectedPoint(VectorData):
    """
    (x, y) or (x, y, z) coordinates of best detectable point of 3D bounding box of objects.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number, Number] = field(default_factory=lambda: no_default(field="BestDetectedPoint.val"), metadata=required)
    """Best detected point"""

    name: Literal["object/motion/best_detected_point"] = field(default="object/motion/best_detected_point")
    """Is always object/motion/best_detected_point"""


@dataclass
class RoadCoordinates(VectorData):
    """
    The fine road coordinates of the center of the object's bounding box.
Measurement unit: (complex)
Value range: (unbounded)
Recommended distribution: (see data type definition)
    """
    val: tuple[str, ...] = field(default_factory=lambda: no_default(field="RoadCoordinates.val"), metadata=required)
    """Road coordinates"""

    name: Literal["object/motion/road_coordinates"] = field(default="object/motion/road_coordinates")
    """Is always object/motion/road_coordinates"""


@dataclass
class Velocity(VectorData):
    """
    Velocity data of the object in world coordinates.
Measurement unit: (complex)
Value range: (unbounded)
Recommended distribution: normal
x: (unit: m/s) Velocity along the world x coordinate of the center of the cuboid.
y: (unit: m/s) Velocity of the world y coordinate of the center of the cuboid.
z: (unit: m/s) Velocity of the world z coordinate of the center of the cuboid.
rx: (unit: rad/s) Velocity of the roll angle.
ry: (unit: rad/s) Velocity of the pitch angle.
rz: (unit: rad/s) Velocity of the yaw angle.
    """
    val: tuple[Number, Number, Number, Number, Number, Number] = field(default_factory=lambda: no_default(field="Velocity.val"), metadata=required)
    """Velocity"""

    name: Literal["object/motion/velocity"] = field(default="object/motion/velocity")
    """Is always object/motion/velocity"""


@dataclass
class SourceOfVelocity(VectorData):
    """
    List of all parameter names whose data was used to fuse / filter the velocity.
If the list contains object/motion/velocity, then a direct velocity measurement (such as direct GNSS velocities, Doppler or wheel odometry recording) must have influenced the data.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: tuple[str, ...] = field(default_factory=lambda: no_default(field="SourceOfVelocity.val"), metadata=required)
    """Source of velocity"""

    name: Literal["object/motion/velocity_source"] = field(default="object/motion/velocity_source")
    """Is always object/motion/velocity_source"""


@dataclass
class Acceleration(VectorData):
    """
    Acceleration data of the object in world coordinates
Measurement unit: (complex)
Value range: (unbounded)
Recommended distribution: normal
x: (unit: m/s²) Acceleration of the world x coordinate of the center of the cuboid.
y: (unit: m/s²) Acceleration of the world y coordinate of the center of the cuboid.
z: (unit: rad/s²) Acceleration of the world z coordinate of the center of the cuboid.
rx: (unit: rad/s²) Acceleration of the roll angle.
ry: (unit: rad/s²) Acceleration of the pitch angle.
rz: (unit: rad/s²) Acceleration of the yaw angle.
    """
    val: tuple[Number, Number, Number, Number, Number, Number] = field(default_factory=lambda: no_default(field="Acceleration.val"), metadata=required)
    """Acceleration"""

    name: Literal["object/motion/acceleration"] = field(default="object/motion/acceleration")
    """Is always object/motion/acceleration"""


@dataclass
class SourceOfAcceleration(VectorData):
    """
    List of all parameter names whose data was used to fuse / filter the acceleration.
If the list contains object/motion/acceleration, then a direct acceleration measurement (such as accelerometer recording) must have influenced the data.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: tuple[str, ...] = field(default_factory=lambda: no_default(field="SourceOfAcceleration.val"), metadata=required)
    """Source of acceleration"""

    name: Literal["object/motion/acceleration_source"] = field(default="object/motion/acceleration_source")
    """Is always object/motion/acceleration_source"""


@dataclass
class MeanSteerAngle(NumberData):
    """
    Average of the left and right hand steer angles on the front axle, according to DIN ISO 8855.
Measurement unit: rad
Value range: [−π, π]
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="MeanSteerAngle.val"), metadata=required)
    """Mean steer angle"""

    name: Literal["object/motion/mean_steer_angle"] = field(default="object/motion/mean_steer_angle")
    """Is always object/motion/mean_steer_angle"""


@dataclass
class SlipAngle(NumberData):
    """
    Angle from the vehicle's forward axis to the vertical projection of the vehicle velocity on to the ground plane, about the Z-axis, according to DIN ISO 8855.
Measurement unit: rad
Value range: [−π, π]
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="SlipAngle.val"), metadata=required)
    """Slip angle"""

    name: Literal["object/motion/slip_angle"] = field(default="object/motion/slip_angle")
    """Is always object/motion/slip_angle"""


@dataclass
class AngleRelativeToRoad(NumberData):
    """
    Angle from the tangent direction of the road that the vehicle is currently driving on, towards the vehicle's forward axis, such that the tangent direction is oriented towards the forward direction of the lane that the vehicle is currently driving on.
Positive angles denote a CCW rotation of the vehicle w.r.t. the forward direction of the road.  Values outside the range of [−π/2, π/2] typically indicate a vehicle driving against the lane's intended direction of travel.
Measurement unit: rad
Value range: [−π, π]
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="AngleRelativeToRoad.val"), metadata=required)
    """Angle relative to road"""

    name: Literal["object/motion/relative_road_angle"] = field(default="object/motion/relative_road_angle")
    """Is always object/motion/relative_road_angle"""
