from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    BooleanData,
    Number,
    NumberData,
    ObjectUid,
    TextData,
    VectorData,
    no_default,
)


@dataclass
class CharacteristicsObjectClassification(TextData):
    """

    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - ANIMAL: None
     - HUMAN: None
     - HUMAN/PEDESTRIAN: None
     - HUMAN/ROAD_WORKER: None
     - VEHICLE: None
     - VEHICLE/BICYCLE: None
     - VEHICLE/BUS: None
     - TRUCK: None
     - CAR: None
     - VAN: None
     - MOBILITY_DEVICE: None
     - MOTORCYCLE: None
     - RAIL_VEHICLE: None
     - TRAILER: None
     - PUSHABLE_PULLABLE: None
    """

    val: str = field(default_factory=lambda: no_default(field="CharacteristicsObjectClassification.val"), metadata=required)
    """Characteristics object_classification value"""

    name: Literal["object/characteristics/object_classification"] = field(
        default="object/characteristics/object_classification"
    )
    """Is always object/characteristics/object_classification"""


@dataclass
class CharacteristicsDriverSide(TextData):
    """
        Describes on which side the driver is located, in particular due to left-hand vs. right-hand traffic, but also due to specific vehicle configurations. This information may be used for visibility or impact hazard estimations.
    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - NOT_APPLICABLE: Driver location cannot be specified, for example for vehicles without a human rider or teleoperation.
     - LEFT: Driver is located on the left side of the vehicle.
     - RIGHT: Driver is located on the right side of the vehicle.
     - CENTER: Driver is located in the center of the vehicle.
    """

    val: str = field(default_factory=lambda: no_default(field="CharacteristicsDriverSide.val"), metadata=required)
    """Characteristics driver_side value"""

    name: Literal["object/characteristics/driver_side"] = field(default="object/characteristics/driver_side")
    """Is always object/characteristics/driver_side"""


@dataclass
class CharacteristicsSpecialPurpose(TextData):
    """
        Association of a road user to a special purpose or service (i.e., excluding personal and regular commercial vehicles or purposes). To indicate whether a vehicle is currently on an emergency mission (by using its emergency lights), see object/lights/emergency.
    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - NONE: Road user has no known special purpose.
     - RECREATION: Recreational vehicles (camper trailers, motorhomes, etc.)
     - CONSTRUCTION: Road works / construction.
     - POLICE: Police / law enforcement.
     - FIRE_DEPARTMENT: Fire department and technical rescue response services.
     - EMERGENCY_MEDICAL: Emergency medical services (EMS), ambulance or parametric services, patient transport.
     - MILITARY: Military forces.
     - OTHER: Any special service not listed above.
    """

    val: str = field(default_factory=lambda: no_default(field="CharacteristicsSpecialPurpose.val"), metadata=required)
    """Characteristics special_purpose value"""

    name: Literal["object/characteristics/special_purpose"] = field(default="object/characteristics/special_purpose")
    """Is always object/characteristics/special_purpose"""


@dataclass
class CharacteristicsCenterOfGravity(VectorData):
    """
        Center of gravity of this object, relative to the center of the bounding box.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsCenterOfGravity.val"), metadata=required
    )
    """Characteristics center_of_gravity value"""

    name: Literal["object/characteristics/center_of_gravity"] = field(default="object/characteristics/center_of_gravity")
    """Is always object/characteristics/center_of_gravity"""


@dataclass
class CharacteristicsMass(NumberData):
    """
        Mass of the object. This value refers to the actual vehicle mass (as required, e.g., to estimate crash impact severity).
    For the maximum allowable mass of the vehicle type, see object/characteristics/gross_vehicle_mass.
    Measurement unit: kg
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="CharacteristicsMass.val"), metadata=required)
    """Characteristics mass value"""

    name: Literal["object/characteristics/mass"] = field(default="object/characteristics/mass")
    """Is always object/characteristics/mass"""


@dataclass
class CharacteristicsGrossVehicleMass(NumberData):
    """
        Maximum operating mass (or maximum authorized mass) of a vehicle as specified by the manufacturer including vehicle body, fuel, driver, passengers and cargo but excluding that of any trailers.
    This value is used for classification of the vehicle type, whereas
    Measurement unit: kg
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="CharacteristicsGrossVehicleMass.val"), metadata=required)
    """Characteristics gross_vehicle_mass value"""

    name: Literal["object/characteristics/gross_vehicle_mass"] = field(default="object/characteristics/gross_vehicle_mass")
    """Is always object/characteristics/gross_vehicle_mass"""


@dataclass
class CharacteristicsCurbMass(NumberData):
    """
        Mass of the vehicle including structure, fluids and full fuel tank, but no passengers or cargo. Commonly called “curb weight” or “kerb weight”.
    Measurement unit: kg
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="CharacteristicsCurbMass.val"), metadata=required)
    """Characteristics curb_mass value"""

    name: Literal["object/characteristics/curb_mass"] = field(default="object/characteristics/curb_mass")
    """Is always object/characteristics/curb_mass"""


@dataclass
class CharacteristicsAxles(NumberData):
    """
        Number of axles (only for objects of Vehicle class).
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="CharacteristicsAxles.val"), metadata=required)
    """Characteristics axles value"""

    name: Literal["object/characteristics/axles"] = field(default="object/characteristics/axles")
    """Is always object/characteristics/axles"""


@dataclass
class CharacteristicsWheels(NumberData):
    """
        Number of wheels (only for objects of Vehicle class).
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="CharacteristicsWheels.val"), metadata=required)
    """Characteristics wheels value"""

    name: Literal["object/characteristics/wheels"] = field(default="object/characteristics/wheels")
    """Is always object/characteristics/wheels"""


@dataclass
class CharacteristicsIndependentWheels(NumberData):
    """
        Number of wheels (only for objects of Vehicle class) where dual wheels (e.g., in trucks) are counted as a single wheel.
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="CharacteristicsIndependentWheels.val"), metadata=required)
    """Characteristics independent_wheels value"""

    name: Literal["object/characteristics/independent_wheels"] = field(default="object/characteristics/independent_wheels")
    """Is always object/characteristics/independent_wheels"""


@dataclass
class CharacteristicsSeats(NumberData):
    """
        Number of seats (occupied or unoccupied, only for objects of Vehicle class).
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="CharacteristicsSeats.val"), metadata=required)
    """Characteristics seats value"""

    name: Literal["object/characteristics/seats"] = field(default="object/characteristics/seats")
    """Is always object/characteristics/seats"""


@dataclass
class CharacteristicsPassengers(NumberData):
    """
        Number of passengers actually present in/on the vehicle (only for objects of Vehicle class).
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="CharacteristicsPassengers.val"), metadata=required)
    """Characteristics passengers value"""

    name: Literal["object/characteristics/passengers"] = field(default="object/characteristics/passengers")
    """Is always object/characteristics/passengers"""


@dataclass
class CharacteristicsMaximumSpeed(NumberData):
    """
        Maximum permitted or possible speed for the vehicle in its present configuration. This can be the maximum design speed of the vehicle, speed limits for trailers, or speed limits for specific vehicle classes that apply regardless of road-specific speed limits.
    Measurement unit: m/s
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="CharacteristicsMaximumSpeed.val"), metadata=required)
    """Characteristics maximum_speed value"""

    name: Literal["object/characteristics/maximum_speed"] = field(default="object/characteristics/maximum_speed")
    """Is always object/characteristics/maximum_speed"""


@dataclass
class CharacteristicsHasRider(BooleanData):
    """
        True iff the vehicle or animal has a rider or operator, as the mounted human controlling or supervising its motion.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: probability of assigned value
    """

    val: bool = field(default_factory=lambda: no_default(field="CharacteristicsHasRider.val"), metadata=required)
    """Characteristics has_rider value"""

    name: Literal["object/characteristics/has_rider"] = field(default="object/characteristics/has_rider")
    """Is always object/characteristics/has_rider"""


@dataclass
class CharacteristicsHasEngine(BooleanData):
    """
        True iff the vehicle is completely or partly powered by an engine. Should be specified only for light vehicle types such as PEDAL_CYCLE or KICK_SCOOTER where engines are not equipped by default, to indicate pedelecs or e-scooters.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: bool = field(default_factory=lambda: no_default(field="CharacteristicsHasEngine.val"), metadata=required)
    """Characteristics has_engine value"""

    name: Literal["object/characteristics/has_engine"] = field(default="object/characteristics/has_engine")
    """Is always object/characteristics/has_engine"""


@dataclass
class CharacteristicsIsRecorder(BooleanData):
    """
        Indicates whether the object is the recording entity in this scenario. If True, this object is the recording entity of the scenario.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: bool = field(default_factory=lambda: no_default(field="CharacteristicsIsRecorder.val"), metadata=required)
    """Characteristics is_recorder value"""

    name: Literal["object/characteristics/is_recorder"] = field(default="object/characteristics/is_recorder")
    """Is always object/characteristics/is_recorder"""


@dataclass
class CharacteristicsConnectedTo(VectorData):
    """
        Identified objects in a scene may be physically connected to other objects as trailers to trucks. If so, an object of type CONNECTION_GROUP can be created to store information about this connection.
    The connected_to parameter then either points from the individual connected parts towards the single UID of the CONNECTION_GROUP object, or from the CONNECTION_GROUP to the connected objects.
    No two non-CONNECTION_GROUP objects shall be connected directly through this parameter.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: tuple[ObjectUid, ...] = field(
        default_factory=lambda: no_default(field="CharacteristicsConnectedTo.val"), metadata=required
    )
    """Characteristics connected_to value"""

    name: Literal["object/characteristics/connected_to"] = field(default="object/characteristics/connected_to")
    """Is always object/characteristics/connected_to"""


@dataclass
class CharacteristicsTowedBy(TextData):
    """
        Single UID of the object that tows this object, for example the UID of the tractor from the perspective of a trailer. Should be used in combination with object/characteristics/connected_to when set.
    See also object/characteristics/position_fifth_wheel and object/characteristics/position_kingpin.
    Measurement unit: N/A
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: ObjectUid = field(default_factory=lambda: no_default(field="CharacteristicsTowedBy.val"), metadata=required)
    """Characteristics towed_by value"""

    name: Literal["object/characteristics/towed_by"] = field(default="object/characteristics/towed_by")
    """Is always object/characteristics/towed_by"""


@dataclass
class CharacteristicsPositionTangential(VectorData):
    """
        Position (x,y) or (x,y,z) in vehicle coordinates of one point whose path usually aligns with the X axis of the bounding box during turns without significant dynamics. The point shall be centered along the Y axis of the bounding box (i.e., having y = 0) unless there are specific reasons for a different convention.
    For typical front-steered two-axle vehicles, this point is located at the center of the rear axle. Required in case of detailed kinematic simulation / prediction models.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsPositionTangential.val"), metadata=required
    )
    """Characteristics position_tangential value"""

    name: Literal["object/characteristics/position_tangential"] = field(default="object/characteristics/position_tangential")
    """Is always object/characteristics/position_tangential"""


@dataclass
class CharacteristicsPositionFifthWheel(VectorData):
    """
        Position (x,y) or (x,y,z) of the fifth wheel in object coordinates, which is the position at which a trailer (by its position of object/characteristics/position_kingpin) is attached to this vehicle.
    Required in case of detailed kinematic simulation / prediction models. When multiple trailers (double, triple configuration) are used, an intermediate trailer may have both a fifth wheel and a kingpin specified.
    See also object/characteristics/towed_by.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsPositionFifthWheel.val"), metadata=required
    )
    """Characteristics position_fifth_wheel value"""

    name: Literal["object/characteristics/position_fifth_wheel"] = field(default="object/characteristics/position_fifth_wheel")
    """Is always object/characteristics/position_fifth_wheel"""


@dataclass
class CharacteristicsPositionKingpin(VectorData):
    """
        Position (x,y) or (x,y,z) of the kingpin in object coordinates, which is the position at which a trailer attaches to the towing vehicle (at its respective position of object/characteristics/position_fifth_wheel).
    When multiple trailers (double, triple configuration) are used, an intermediate trailer may have both a fifth wheel and a kingpin specified.
    See also object/characteristics/towed_by.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsPositionKingpin.val"), metadata=required
    )
    """Characteristics position_kingpin value"""

    name: Literal["object/characteristics/position_kingpin"] = field(default="object/characteristics/position_kingpin")
    """Is always object/characteristics/position_kingpin"""


@dataclass
class CharacteristicsGlobalPosition(VectorData):
    """
        global 2D coordinates of the position  𝑔𝑖 = (𝑥𝑖, 𝑦𝑖) of a vehicle 𝑖 in a selected global inertial system. The position of a vehicle is defined by the center point of a vehicles shape.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsGlobalPosition.val"), metadata=required
    )
    """Characteristics global_position value"""

    name: Literal["object/characteristics/global_position"] = field(default="object/characteristics/global_position")
    """Is always object/characteristics/global_position"""


@dataclass
class CharacteristicsOutlineChamfer(VectorData):
    """
        2D outline shape parameters (in the x,y plane) for the chamfer outline model. The elements define the x coordinate offsets from the rear and front, respectively, at which a 45° chamfer at the bounding box corners meets the sides of the bounding box.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    Elements of vector:
     - a: (unit: m) Rear chamfer
     - b: (unit: m) Front chamfer
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsOutlineChamfer.val"), metadata=required
    )
    """Characteristics outline chamfer value"""

    name: Literal["object/characteristics/outline/chamfer"] = field(default="object/characteristics/outline/chamfer")
    """Is always object/characteristics/outline/chamfer"""


@dataclass
class CharacteristicsOutlinePolygon(VectorData):
    """
        2D outline shape parameters (in the x,y plane) for the polygon (𝑃𝑖) outline model with the coordinates of the vertices 𝑝′𝑖,𝑣 = (𝑥′𝑖,𝑣, 𝑦′𝑖,𝑣) in vehicle coordinates (𝑣 = 1, ... , 𝑉 the vertices of the polygon) of vehicle 𝑖. The vertices shall start at the rear right edge point of the vehicle (𝑥′𝑖,0, 𝑦′𝑖,0), then describe the outline in CCW order, without self-intersections of the polygon, and such that the final point in the polygon can be connected to the first point to form the final side.
    The global coordinates of the polygons vertices can be computed by superimposing the vehicle's global position coordinates 𝑔𝑖 = (𝑥𝑖, 𝑦𝑖) with the local coordinates of the vertices 𝑝′𝑖,𝑣, which are rotated by an angle 𝛼 relative to the global coordinate system.
     vertices of polygon 𝑃𝑖 : 𝑝𝑖,𝑣 = 𝑔𝑖 + 𝑟𝑜𝑡(𝛼) × 𝑝′𝑖,𝑣
    with 𝑟𝑜𝑡(𝛼) the rotation matrix in 2D.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number] = field(
        default_factory=lambda: no_default(field="CharacteristicsOutlinePolygon.val"), metadata=required
    )
    """Characteristics outline polygon value"""

    name: Literal["object/characteristics/outline/polygon"] = field(default="object/characteristics/outline/polygon")
    """Is always object/characteristics/outline/polygon"""
