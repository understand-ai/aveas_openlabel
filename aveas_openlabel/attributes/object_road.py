
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
class SpeedLimit(NumberData):
    """
    Applicable speed limit for this particular vehicle at its current position in (m/s). The applicable speed limit can stem from traffic signs, the specific location (e.g., within city limits), or from country-specific maxima.
Measurement unit: m/s
Value range: (unbounded)
Recommended distribution: rectangular
0: indicates no speed limit (i.e., unlimited)
    """
    val: float = field(default_factory=lambda: no_default(field="SpeedLimit.val"), metadata=required)
    """Speed limit"""

    name: Literal["object/road/speed_limit"] = field(default="object/road/speed_limit")
    """Is always object/road/speed_limit"""


@dataclass
class Classification(TextData):
    """
    The classification of the current road section, adopting the OpenStreetMap definition for key “highway” OpenStreetMap contributors, OpenStreetMap Wiki, Key:highway , including the original definitions therein.
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: probability vector
MOTORWAY: A restricted access major divided highway, normally with 2 or more running lanes plus emergency hard shoulder. Equivalent to the Freeway, Autobahn, etc..
TRUNK: The most important roads in a country's system. (Usually link larger towns.)
PRIMARY: The next most important roads in a country's system. (Often link towns.)
SECONDARY: The next most important roads in a country's system. (Often link towns.)
TERTIARY: The next most important roads in a country's system. (Often link smaller towns and villages)
BELOW_TERTIARY: The least important through roads in a country's system – i.e. minor roads of a lower classification than tertiary, but which serve a purpose other than access to properties. (Often link villages and hamlets.) This class corresponds to the “unclassified” highway type in OpenStreetMap, renamed to avoid misunderstandings in terminology.
RESIDENTIAL: Roads which serve as an access to housing, without function of connecting settlements. Often lined with housing.
MOTORWAY_LINK: The link roads (sliproads/ramps) leading to/from a motorway from/to a motorway or lower class highway. Normally with the same motorway restrictions.
TRUNK_LINK: The link roads (sliproads/ramps) leading to/from a trunk road from/to a trunk road or lower class highway.
PRIMARY_LINK: The link roads (sliproads/ramps) leading to/from a primary road from/to a primary road or lower class highway.
SECONDARY_LINK: The link roads (sliproads/ramps) leading to/from a secondary
LIVING_STREET: For living streets, which are residential streets where pedestrians have legal priority over cars, speeds are kept very low.
SERVICE: For access roads to, or within an industrial estate, camp site, business park, car park, alleys, etc. Can be used in conjunction with service=* to indicate the type of usage and with access=* to indicate who can use it and in what circumstances.
PEDESTRIAN: For roads used mainly/exclusively for pedestrians in shopping and some residential areas which may allow access by motorised vehicles only for very limited periods of the day. To create a ‘square’ or ‘plaza’ create a closed way and tag as pedestrian and also with area=yes.
TRACK: Roads for mostly agricultural or forestry uses. Note: Although tracks are often rough with unpaved surfaces, this tag is not describing the quality of a road but its use.
BUS_GUIDEWAY: A busway where the vehicle is guided by the way (though not a railway) and is not suitable for other traffic. Please note: this is not a normal bus lane.
ESCAPE: For runaway truck ramps, runaway truck lanes, emergency escape ramps, or truck arrester beds. It enables vehicles with braking failure to safely stop.
RACEWAY: A course or track for (motor) racing
ROAD: A road/way/street/motorway/etc. of unknown type. It can stand for anything ranging from a footpath to a motorway.
BUSWAY: A dedicated roadway for bus rapid transit systems.
    """
    val: str = field(default_factory=lambda: no_default(field="Classification.val"), metadata=required)
    """Classification"""

    name: Literal["object/road/classification"] = field(default="object/road/classification")
    """Is always object/road/classification"""


@dataclass
class Junction(TextData):
    """
    The classification of the current road section.
Measurement unit: (dimensionless)
Value range: (enumeration)
Recommended distribution: (none)
NONE: Vehicle is not at a junction
T_INTERSECTION: A T intersection
X_INTERSECTION: A crossing
ROUNDABOUT: A roundabout
    """
    val: str = field(default_factory=lambda: no_default(field="Junction.val"), metadata=required)
    """Junction"""

    name: Literal["object/road/junction"] = field(default="object/road/junction")
    """Is always object/road/junction"""


@dataclass
class LeftLegallyUsable(NumberData):
    """
    Number of lanes left of vehicle’s position that the vehicle is legally permitted to use.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="LeftLegallyUsable.val"), metadata=required)
    """Left (legally usable)"""

    name: Literal["object/road/number_lanes/left_legal"] = field(default="object/road/number_lanes/left_legal")
    """Is always object/road/number_lanes/left_legal"""


@dataclass
class LeftPhysicallyUsable(NumberData):
    """
    Number of lanes left of vehicle’s position that the vehicle can physically reach, excluding its current lane. This includes lanes the vehicle is not allowed to drive on.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="LeftPhysicallyUsable.val"), metadata=required)
    """Left (physically usable)"""

    name: Literal["object/road/number_lanes/left_physical"] = field(default="object/road/number_lanes/left_physical")
    """Is always object/road/number_lanes/left_physical"""


@dataclass
class RightLegallyUsable(NumberData):
    """
    Number of lanes right of vehicle’s position that the vehicle is legally permitted to use.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
    """
    val: int = field(default_factory=lambda: no_default(field="RightLegallyUsable.val"), metadata=required)
    """Right (legally usable)"""

    name: Literal["object/road/number_lanes/right_legal"] = field(default="object/road/number_lanes/right_legal")
    """Is always object/road/number_lanes/right_legal"""


@dataclass
class RightPhysicallyUsable(NumberData):
    """
    Number of lanes right of vehicle’s position that the vehicle can physically reach, excluding its current lane. This includes lanes the vehicle is not allowed to drive on.
Measurement unit: (dimensionless)
Value range: (unbounded)
Recommended distribution: rectangular
-1: Indicates that this attribute is not applicable.
    """
    val: int = field(default_factory=lambda: no_default(field="RightPhysicallyUsable.val"), metadata=required)
    """Right (physically usable)"""

    name: Literal["object/road/number_lanes/right_physical"] = field(default="object/road/number_lanes/right_physical")
    """Is always object/road/number_lanes/right_physical"""
