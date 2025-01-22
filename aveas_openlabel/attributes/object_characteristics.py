
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
class ObjectClassification(TextData):
    """
    
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: probability vector
ANIMAL: None
HUMAN: None
HUMAN/PEDESTRIAN: None
HUMAN/ROAD_WORKER: None
VEHICLE: None
VEHICLE/BICYCLE: None
VEHICLE/BUS: None
TRUCK: None
CAR: None
VAN: None
MOBILITY_DEVICE: None
MOTORCYCLE: None
RAIL_VEHICLE: None
TRAILER: None
PUSHABLE_PULLABLE: None
    """
    val: str = field(default_factory=lambda: no_default(field="ObjectClassification.val"), metadata=required)
    """Object classification"""

    name: Literal["object/characteristics/object_classification"] = field(default="object/characteristics/object_classification")
    """Is always object/characteristics/object_classification"""


@dataclass
class DriverSide(TextData):
    """
    Describes on which side the driver is located, in particular due to left-hand vs. right-hand traffic, but also due to specific vehicle configurations. This information may be used for visibility or impact hazard estimations.
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: probability vector
NOT_APPLICABLE: Driver location cannot be specified, for example for vehicles without a human rider or teleoperation.
LEFT: Driver is located on the left side of the vehicle.
RIGHT: Driver is located on the right side of the vehicle.
CENTER: Driver is located in the center of the vehicle.
    """
    val: str = field(default_factory=lambda: no_default(field="DriverSide.val"), metadata=required)
    """Driver side"""

    name: Literal["object/characteristics/driver_side"] = field(default="object/characteristics/driver_side")
    """Is always object/characteristics/driver_side"""


@dataclass
class SpecialPurpose(TextData):
    """
    Association of a road user to a special purpose or service (i.e., excluding personal and regular commercial vehicles or purposes). To indicate whether a vehicle is currently on an emergency mission (by using its emergency lights), see object/lights/emergency.
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: probability vector
NONE: Road user has no known special purpose.
RECREATION: Recreational vehicles (camper trailers, motorhomes, etc.)
CONSTRUCTION: Road works / construction.
POLICE: Police / law enforcement.
FIRE_DEPARTMENT: Fire department and technical rescue response services.
EMERGENCY_MEDICAL: Emergency medical services (EMS), ambulance or parametric services, patient transport.
MILITARY: Military forces.
OTHER: Any special service not listed above.
    """
    val: str = field(default_factory=lambda: no_default(field="SpecialPurpose.val"), metadata=required)
    """Special purpose"""

    name: Literal["object/characteristics/special_purpose"] = field(default="object/characteristics/special_purpose")
    """Is always object/characteristics/special_purpose"""


@dataclass
class CenterOfGravity(VectorData):
    """
    Center of gravity of this object, relative to the center of the bounding box.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number, Number] = field(default_factory=lambda: no_default(field="CenterOfGravity.val"), metadata=required)
    """Center of gravity"""

    name: Literal["object/characteristics/center_of_gravity"] = field(default="object/characteristics/center_of_gravity")
    """Is always object/characteristics/center_of_gravity"""


@dataclass
class Mass(NumberData):
    """
    Mass of the object. This value refers to the actual vehicle mass (as required, e.g., to estimate crash impact severity).
For the maximum allowable mass of the vehicle type, see object/characteristics/gross_vehicle_mass.
Measurement unit: kg
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="Mass.val"), metadata=required)
    """Mass"""

    name: Literal["object/characteristics/mass"] = field(default="object/characteristics/mass")
    """Is always object/characteristics/mass"""


@dataclass
class GrossVehicleMass(NumberData):
    """
    Maximum operating mass (or maximum authorized mass) of a vehicle as specified by the manufacturer including vehicle body, fuel, driver, passengers and cargo but excluding that of any trailers.
This value is used for classification of the vehicle type, whereas
Measurement unit: kg
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="GrossVehicleMass.val"), metadata=required)
    """Gross vehicle mass"""

    name: Literal["object/characteristics/gross_vehicle_mass"] = field(default="object/characteristics/gross_vehicle_mass")
    """Is always object/characteristics/gross_vehicle_mass"""


@dataclass
class CurbMass(NumberData):
    """
    Mass of the vehicle including structure, fluids and full fuel tank, but no passengers or cargo. Commonly called “curb weight” or “kerb weight”.
Measurement unit: kg
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="CurbMass.val"), metadata=required)
    """Curb mass"""

    name: Literal["object/characteristics/curb_mass"] = field(default="object/characteristics/curb_mass")
    """Is always object/characteristics/curb_mass"""


@dataclass
class Axles(NumberData):
    """
    Number of axles (only for objects of Vehicle class).
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="Axles.val"), metadata=required)
    """Axles"""

    name: Literal["object/characteristics/axles"] = field(default="object/characteristics/axles")
    """Is always object/characteristics/axles"""


@dataclass
class Wheels(NumberData):
    """
    Number of wheels (only for objects of Vehicle class).
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="Wheels.val"), metadata=required)
    """Wheels"""

    name: Literal["object/characteristics/wheels"] = field(default="object/characteristics/wheels")
    """Is always object/characteristics/wheels"""


@dataclass
class IndependentWheels(NumberData):
    """
    Number of wheels (only for objects of Vehicle class) where dual wheels (e.g., in trucks) are counted as a single wheel.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="IndependentWheels.val"), metadata=required)
    """Independent wheels"""

    name: Literal["object/characteristics/independent_wheels"] = field(default="object/characteristics/independent_wheels")
    """Is always object/characteristics/independent_wheels"""


@dataclass
class Seats(NumberData):
    """
    Number of seats (occupied or unoccupied, only for objects of Vehicle class).
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="Seats.val"), metadata=required)
    """Seats"""

    name: Literal["object/characteristics/seats"] = field(default="object/characteristics/seats")
    """Is always object/characteristics/seats"""


@dataclass
class Passengers(NumberData):
    """
    Number of passengers actually present in/on the vehicle (only for objects of Vehicle class).
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="Passengers.val"), metadata=required)
    """Passengers"""

    name: Literal["object/characteristics/passengers"] = field(default="object/characteristics/passengers")
    """Is always object/characteristics/passengers"""


@dataclass
class MaximumSpeed(NumberData):
    """
    Maximum permitted or possible speed for the vehicle in its present configuration. This can be the maximum design speed of the vehicle, speed limits for trailers, or speed limits for specific vehicle classes that apply regardless of road-specific speed limits.
Measurement unit: m/s
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: float = field(default_factory=lambda: no_default(field="MaximumSpeed.val"), metadata=required)
    """Maximum speed"""

    name: Literal["object/characteristics/maximum_speed"] = field(default="object/characteristics/maximum_speed")
    """Is always object/characteristics/maximum_speed"""


@dataclass
class HasRider(BooleanData):
    """
    True iff the vehicle or animal has a rider or operator, as the mounted human controlling or supervising its motion.
Measurement unit: N/A
Value range: (unbounded)
Recommended distribution: probability of assigned value
    """
    val: bool = field(default_factory=lambda: no_default(field="HasRider.val"), metadata=required)
    """Has rider"""

    name: Literal["object/characteristics/has_rider"] = field(default="object/characteristics/has_rider")
    """Is always object/characteristics/has_rider"""


@dataclass
class HasEngine(BooleanData):
    """
    True iff the vehicle is completely or partly powered by an engine. Should be specified only for light vehicle types such as PEDAL_CYCLE or KICK_SCOOTER where engines are not equipped by default, to indicate pedelecs or e-scooters.
Measurement unit: N/A
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: bool = field(default_factory=lambda: no_default(field="HasEngine.val"), metadata=required)
    """Has engine"""

    name: Literal["object/characteristics/has_engine"] = field(default="object/characteristics/has_engine")
    """Is always object/characteristics/has_engine"""


@dataclass
class IsRecorder(BooleanData):
    """
    Indicates whether the object is the recording entity in this scenario. If True, this object is the recording entity of the scenario.
Measurement unit: N/A
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: bool = field(default_factory=lambda: no_default(field="IsRecorder.val"), metadata=required)
    """Is recorder"""

    name: Literal["object/characteristics/is_recorder"] = field(default="object/characteristics/is_recorder")
    """Is always object/characteristics/is_recorder"""


@dataclass
class ConnectedTo(VectorData):
    """
    Identified objects in a scene may be physically connected to other objects as trailers to trucks. If so, an object of type CONNECTION_GROUP can be created to store information about this connection.
The connected_to parameter then either points from the individual connected parts towards the single UID of the CONNECTION_GROUP object, or from the CONNECTION_GROUP to the connected objects.
No two non-CONNECTION_GROUP objects shall be connected directly through this parameter.
Measurement unit: N/A
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: tuple[ObjectUid, ...] = field(default_factory=lambda: no_default(field="ConnectedTo.val"), metadata=required)
    """Connected to"""

    name: Literal["object/characteristics/connected_to"] = field(default="object/characteristics/connected_to")
    """Is always object/characteristics/connected_to"""


@dataclass
class TowedBy(TextData):
    """
    Single UID of the object that tows this object, for example the UID of the tractor from the perspective of a trailer. Should be used in combination with object/characteristics/connected_to when set.
See also object/characteristics/position_fifth_wheel and object/characteristics/position_kingpin.
Measurement unit: N/A
Value range: (unbounded)
Recommended distribution: (none)
    """
    val: ObjectUid = field(default_factory=lambda: no_default(field="TowedBy.val"), metadata=required)
    """Towed by"""

    name: Literal["object/characteristics/towed_by"] = field(default="object/characteristics/towed_by")
    """Is always object/characteristics/towed_by"""


@dataclass
class PositionOfTheTangentialPoint(VectorData):
    """
    Position (x,y) or (x,y,z) in vehicle coordinates of one point whose path usually aligns with the X axis of the bounding box during turns without significant dynamics. The point shall be centered along the Y axis of the bounding box (i.e., having y = 0) unless there are specific reasons for a different convention.
For typical front-steered two-axle vehicles, this point is located at the center of the rear axle. Required in case of detailed kinematic simulation / prediction models.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="PositionOfTheTangentialPoint.val"), metadata=required)
    """Position of the tangential point"""

    name: Literal["object/characteristics/position_tangential"] = field(default="object/characteristics/position_tangential")
    """Is always object/characteristics/position_tangential"""


@dataclass
class PositionOfTheFifthWheel(VectorData):
    """
    Position (x,y) or (x,y,z) of the fifth wheel in object coordinates, which is the position at which a trailer (by its position of object/characteristics/position_kingpin) is attached to this vehicle.
Required in case of detailed kinematic simulation / prediction models. When multiple trailers (double, triple configuration) are used, an intermediate trailer may have both a fifth wheel and a kingpin specified.
See also object/characteristics/towed_by.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="PositionOfTheFifthWheel.val"), metadata=required)
    """Position of the fifth wheel"""

    name: Literal["object/characteristics/position_fifth_wheel"] = field(default="object/characteristics/position_fifth_wheel")
    """Is always object/characteristics/position_fifth_wheel"""


@dataclass
class PositionOfTheKingpin(VectorData):
    """
    Position (x,y) or (x,y,z) of the kingpin in object coordinates, which is the position at which a trailer attaches to the towing vehicle (at its respective position of object/characteristics/position_fifth_wheel).
When multiple trailers (double, triple configuration) are used, an intermediate trailer may have both a fifth wheel and a kingpin specified.
See also object/characteristics/towed_by.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="PositionOfTheKingpin.val"), metadata=required)
    """Position of the kingpin"""

    name: Literal["object/characteristics/position_kingpin"] = field(default="object/characteristics/position_kingpin")
    """Is always object/characteristics/position_kingpin"""


@dataclass
class GlobalPosition(VectorData):
    """
    global 2D coordinates of the position  𝑔𝑖 = (𝑥𝑖, 𝑦𝑖) of a vehicle 𝑖 in a selected global inertial system. The position of a vehicle is defined by the center point of a vehicles shape.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="GlobalPosition.val"), metadata=required)
    """Global position"""

    name: Literal["object/characteristics/global_position"] = field(default="object/characteristics/global_position")
    """Is always object/characteristics/global_position"""


@dataclass
class Chamfer(VectorData):
    """
    2D outline shape parameters (in the x,y plane) for the chamfer outline model. The elements define the x coordinate offsets from the rear and front, respectively, at which a 45° chamfer at the bounding box corners meets the sides of the bounding box.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
a: (unit: m) Rear chamfer
b: (unit: m) Front chamfer
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="Chamfer.val"), metadata=required)
    """Chamfer"""

    name: Literal["object/characteristics/outline/chamfer"] = field(default="object/characteristics/outline/chamfer")
    """Is always object/characteristics/outline/chamfer"""


@dataclass
class Polygon(VectorData):
    """
    2D outline shape parameters (in the x,y plane) for the polygon (𝑃𝑖) outline model with the coordinates of the vertices 𝑝′𝑖,𝑣 = (𝑥′𝑖,𝑣, 𝑦′𝑖,𝑣) in vehicle coordinates (𝑣 = 1, ... , 𝑉 the vertices of the polygon) of vehicle 𝑖. The vertices shall start at the rear right edge point of the vehicle (𝑥′𝑖,0, 𝑦′𝑖,0), then describe the outline in CCW order, without self-intersections of the polygon, and such that the final point in the polygon can be connected to the first point to form the final side.
The global coordinates of the polygons vertices can be computed by superimposing the vehicle's global position coordinates 𝑔𝑖 = (𝑥𝑖, 𝑦𝑖) with the local coordinates of the vertices 𝑝′𝑖,𝑣, which are rotated by an angle 𝛼 relative to the global coordinate system.
 vertices of polygon 𝑃𝑖 : 𝑝𝑖,𝑣 = 𝑔𝑖 + 𝑟𝑜𝑡(𝛼) × 𝑝′𝑖,𝑣
with 𝑟𝑜𝑡(𝛼) the rotation matrix in 2D.
Measurement unit: m
Value range: (unbounded)
Recommended distribution: normal
    """
    val: tuple[Number, Number] = field(default_factory=lambda: no_default(field="Polygon.val"), metadata=required)
    """Polygon"""

    name: Literal["object/characteristics/outline/polygon"] = field(default="object/characteristics/outline/polygon")
    """Is always object/characteristics/outline/polygon"""
