"""Implementation of attributes in `ScenarioContextData`

"""

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
from uai_openlabel import (
    BooleanData,
    NumberData,
    TextData,
    VectorData,
    no_default,
)


@dataclass
class Scenario__IsStaged(BooleanData):
    """True iff the scenario contains staged (i.e. previously defined) behavior. This can include simulator studies
    where other vehicles drive on specifically set trajectories, or real-world scenarios when one or several vehicles
    are driven by specifically instructed operators. It does not include simulations where vehicle behavior is
    stochastically determined by a behavior model.
    """

    val: bool = field(default_factory=lambda: no_default(field="Scenario__IsStaged.val"), metadata=required)
    """True iff the scenario contains staged (i.e. previously defined) behavior."""

    name: Literal["scenario/is_staged"] = field(default="scenario/is_staged")
    """Is always 'scenario/is_staged'"""


@dataclass
class Scenario__IsBiased(BooleanData):
    """True iff the scenario likely does NOT represent purely natural conditions due to recording- or study-specific
    influence, for example due to a conspicuous recording vehicle affecting the driving behavior of other traffic
    participants, or due to unusual staged behavior (cf. `Scenario__IsStaged`).
    """

    val: bool = field(default_factory=lambda: no_default(field="Scenario__IsBiased.val"), metadata=required)
    """Value indicating if scenario is biased or not."""

    name: Literal["scenario/is_biased"] = field(default="scenario/is_biased")
    """Is always 'scenario/is_biased'"""


@dataclass
class Scenario__IsSampled(BooleanData):
    """True iff the scenario has been sampled from a real scenario or not. See also `Scenario__IsSampled__ReferenceToSourceScenario`."""

    val: bool = field(default_factory=lambda: no_default(field="Scenario__IsSampled.val"), metadata=required)
    """Value indicating if scenario is a sampled one or not."""

    name: Literal["scenario/is_sampled"] = field(default="scenario/is_sampled")
    """Is always 'scenario/is_sampled'"""


@dataclass
class Scenario__IsSampled__ReferenceToSourceScenario(TextData):
    """Specifying the scenario ID of the source scenario the scenario was sampled from. Only required if `Scenario__IsSampled` is True."""

    val: str = field(
        default_factory=lambda: no_default(field="Scenario__IsSampled__ReferenceToSourceScenario.val"), metadata=required
    )
    """The scenario ID of the source scenario."""

    name: Literal["scenario/is_sampled/reference_to_source_scenario"] = field(
        default="scenario/is_sampled/reference_to_source_scenario"
    )
    """Is always 'scenario/is_sampled/reference_to_source_scenario'"""


@dataclass
class Scenario__MinimumVehicleDistanceS(NumberData):
    """The minimum distance between a moving vehicle and another traffic participant occurring in the scenario in the direction of the road's reference line."""

    val: float = field(default_factory=lambda: no_default(field="Scenario__MinimumVehicleDistanceS.val"), metadata=required)
    """The value of the minimum distance in direction of the road's reference line."""

    name: Literal["scenario/minimum_vehicle_distance_s"] = field(default="scenario/minimum_vehicle_distance_s")
    """Is always 'scenario/minimum_vehicle_distance_s'"""


@dataclass
class Scenario__MinimumVehicleDistanceS__UStdDev(NumberData):
    """Uncertainty for `Scenario__MinimumVehicleDistanceS` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="FrameMinimumVehicleDistanceS__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["scenario/minimum_vehicle_distance_s/ustddev"] = field(default="scenario/minimum_vehicle_distance_s/ustddev")
    """Is always 'scenario/minimum_vehicle_distance_s/ustddev'."""


@dataclass
class Scenario__MinimumVehicleDistanceS__Frame(TextData):
    """Specifying the frame ID for which Scenario__MinimumVehicleDistanceS occurs."""

    val: str = field(
        default_factory=lambda: no_default(field="Scenario__MinimumVehicleDistanceS__Frame.val"), metadata=required
    )
    """The frame ID for which Scenario__MinimumVehicleDistanceS occurs."""

    name: Literal["scenario/minimum_vehicle_distance_s/frame"] = field(default="scenario/minimum_vehicle_distance_s/frame")
    """Is always 'scenario/minimum_vehicle_distance_s/frame'"""


@dataclass
class Scenario__ContainsHighway(BooleanData):
    """Indicating if the scenario is (partially) taking place on highways."""

    val: bool = field(default_factory=lambda: no_default(field="Scenario__ContainsHighway.val"), metadata=required)
    """True iff the scenario is (partially) taking place on highways."""

    name: Literal["scenario/contains_highway"] = field(default="scenario/contains_highway")
    """Is always 'scenario/contains_highway'"""


@dataclass
class Scenario__ContainsUrban(BooleanData):
    """Indicating if the scenario is (partially) taking place in urban environments."""

    val: bool = field(default_factory=lambda: no_default(field="Scenario__ContainsUrban.val"), metadata=required)
    """True iff the scenario is (partially) taking place in urban environments."""

    name: Literal["scenario/contains_urban"] = field(default="scenario/contains_urban")
    """Is always 'scenario/contains_urban'"""


@dataclass
class Scenario__ContainsRural(BooleanData):
    """Indicating if the scenario is (partially) taking place in rural environments."""

    val: bool = field(default_factory=lambda: no_default(field="Scenario__ContainsRural.val"), metadata=required)
    """True iff the scenario is (partially) taking place in rural environments."""

    name: Literal["scenario/contains_rural"] = field(default="scenario/contains_rural")
    """Is always 'scenario/contains_rural'"""


@dataclass
class Scenario__Course(VectorData):
    """Describing the course of a scenario using a sequence of road names in case of in-vehicle or aerial data acquisition or the scenario location using a single road/intersection name in case of stationary data acquisition. The aim of this field is to quickly give the user an idea of where the scenario takes place."""

    val: list[str] = field(default_factory=lambda: no_default(field="Scenario__Course.val"), metadata=required)
    """List of road names for in-vehicle/aerial acquisition, road/intersection name for stationary acquisition."""

    name: Literal["scenario/course"] = field(default="scenario/course")
    """Is always 'scenario/course'"""


@dataclass
class Scenario__MinimumVehicleSpeed(NumberData):
    """Minimum speed of moving vehicles in the scenario.

    Indicating the minimum velocity of all vehicles involved in the scenario that have a velocity of greater than
    zero at least once during the scenario.
    """

    val: float = field(default_factory=lambda: no_default(field="Scenario__MinimumVehicleSpeed.val"), metadata=required)
    """The value of the minimum vehicle velocity."""

    name: Literal["scenario/minimum_vehicle_speed"] = field(default="scenario/minimum_vehicle_speed")
    """Is always 'scenario/minimum_vehicle_speed'"""


@dataclass
class Scenario__MinimumVehicleSpeed__UStdDev(NumberData):
    """Uncertainty for `Scenario__MinimumVehicleSpeed` as standard deviation around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Scenario__MinimumVehicleSpeed__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value."""

    name: Literal["scenario/minimum_vehicle_speed/ustddev"] = field(default="scenario/minimum_vehicle_speed/ustddev")
    """Is always 'scenario/minimum_vehicle_speed/ustddev'."""


@dataclass
class Scenario__MinimumVehicleSpeed__Frame(TextData):
    """Specifying the frame ID for which Scenario__MinimumVehicleSpeed occurs."""

    val: str = field(default_factory=lambda: no_default(field="Scenario__MinimumVehicleSpeed__Frame.val"), metadata=required)
    """The frame ID for which Scenario__MinimumVehicleSpeed occurs."""

    name: Literal["scenario/minimum_vehicle_speed/frame"] = field(default="scenario/minimum_vehicle_speed/frame")
    """Is always 'scenario/minimum_vehicle_speed/frame'"""


@dataclass
class Scenario__MaximumVehicleSpeed(NumberData):
    """Indicating the maximum velocity of all vehicles involved in this scenario."""

    val: float = field(default_factory=lambda: no_default(field="Scenario__MaximumVehicleSpeed.val"), metadata=required)
    """The value of the maximum vehicle velocity."""

    name: Literal["scenario/maximum_vehicle_speed"] = field(default="scenario/maximum_vehicle_speed")
    """Is always 'scenario/maximum_vehicle_speed'"""


@dataclass
class Scenario__MaximumVehicleSpeed__UStdDev(NumberData):
    """Uncertainty for `Scenario__MaximumVehicleSpeed` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Scenario__MaximumVehicleSpeed.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["scenario/maximum_vehicle_speed/ustddev"] = field(default="scenario/maximum_vehicle_speed/ustddev")
    """Is always 'scenario/maximum_vehicle_speed/ustddev'."""


@dataclass
class Scenario__MaximumVehicleSpeed__Frame(TextData):
    """Specifying the frame ID for which Scenario__MaximumVehicleSpeed occurs."""

    val: str = field(default_factory=lambda: no_default(field="Scenario__MaximumVehicleSpeed__Frame.val"), metadata=required)
    """The frame ID for which Scenario__MaximumVehicleSpeed occurs."""

    name: Literal["scenario/maximum_vehicle_speed/frame"] = field(default="scenario/maximum_vehicle_speed/frame")
    """Is always 'scenario/maximum_vehicle_speed/frame'"""


@dataclass
class Scenario__Start__Location(TextData):
    """Describes the location where the scenario started in human-readable format, e.g. “on-ramp Moensheim”."""

    val: str = field(default_factory=lambda: no_default(field="Scenario__Start__Location.val"), metadata=required)
    """The start location of the scenario."""

    name: Literal["scenario/start/location"] = field(default="scenario/start/location")
    """Is always 'scenario/start/location'"""


@dataclass
class Scenario__Start__Coordinates(VectorData):
    """
    Contains the coordinates of the start location of the scenario using the coordinate system also used within the OpenDRIVE file.
    In the case of aerial data acquisition, this refers to the initial position of the plane.
    In the case of in-vehicle data acquisition, to the initial position of the recording vehicle.
    """

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Scenario__Start__Coordinates.val"), metadata=required
    )
    """The coordinates of the start position in the order x, y, z."""

    name: Literal["scenario/start/coordinates"] = field(default="scenario/start/coordinates")
    """Is always 'scenario/start/coordinates'"""


@dataclass
class Scenario__End__Location(TextData):
    """Describes the location where the scenario ended in human-readable format, e.g. “on-ramp Moensheim”."""

    val: str = field(default_factory=lambda: no_default(field="Scenario__End__Location.val"), metadata=required)
    """The end location of the scenario."""

    name: Literal["scenario_end/location"] = field(default="scenario_end/location")
    """Is always 'scenario/end/location'"""


@dataclass
class Scenario__End__Coordinates(VectorData):
    """
    Contains the coordinates of the end location of the scenario using the coordinate system also used within the OpenDRIVE file.
    In the case of aerial data acquisition, this refers to the final position of the plane.
    In the case of in-vehicle data acquisition, to the final position of the recording.
    """

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Scenario__End__Coordinates.val"), metadata=required
    )
    """The coordinates of the end position in the order x, y, z."""

    name: Literal["scenario/end/coordinates"] = field(default="scenario/end/coordinates")
    """Is always 'scenario/end/coordinates'"""


@dataclass
class Scenario__RatioAverageSpeedToSpeedLimit(NumberData):
    """The average ratio between speed and speed limit over all road-based traffic participants and all frames in the file.

    In case no speed limit is present, the denominator is set to the maximum available speed limit of
    the country (e.g. 130 km/h for Germany) and 20 km/h is added to it (resulting in 150 km/h for Germany).
    """

    val: float = field(
        default_factory=lambda: no_default(field="Scenario__RatioAverageSpeedToSpeedLimit.val"), metadata=required
    )
    """The average ratio between speed and speed limit over all road-based traffic participants and all frames in the file."""

    name: Literal["scenario/ratio_average_speed_to_speed_limit"] = field(default="scenario/ratio_average_speed_to_speed_limit")
    """Is always 'scenario/ratio_average_speed_to_speed_limit'"""


@dataclass
class Scenario__RatioAverageSpeedToSpeedLimit__UStdDev(NumberData):
    """Uncertainty for `Scenario__RatioAverageSpeedToSpeedLimit` as standard deviation around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Scenario__RatioAverageSpeedToSpeedLimit__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["scenario/ratio_average_speed_to_speed_limit/ustddev"] = field(
        default="scenario/ratio_average_speed_to_speed_limit/ustddev"
    )
    """Is always 'scenario/ratio_average_speed_to_speed_limit/ustddev'."""


@dataclass
class Scenario__WeekdayNumber(NumberData):
    """Weekday number according to ISO 8601."""

    val: int = field(default_factory=lambda: no_default(field="Scenario__WeekdayNumber.val"), metadata=required)
    """Integer Weekday number (Monday=1, Sunday = 7)."""

    name: Literal["scenario/weekday_number"] = field(default="scenario/weekday_number")
    """Is always 'scenario/weekday_number'"""
