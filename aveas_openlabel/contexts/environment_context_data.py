"""Implementation of attributes in `EnvironmentContextData`

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
from enum import Enum
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    NumberData,
    TextData,
    VectorData,
    no_default,
)


class Environment__LightingConditionsValue(str, Enum):
    """Possible values of 'lighting_conditions'"""

    DARKNESS = "darkness"
    """No significant primary lighting. Includes night time, as well as e.g. un-illuminated parking garages"""

    ARTIFICIAL = "artificial"
    """Artificial primary lighting"""

    CIVIL_TWILIGHT = "civil_twilight"
    """
    Defined as "the period of incomplete darkness when the upper limb of the sun is below the visible horizon, 
    and the center of the sun is not more than 6° below the celestial horizon". (Glossary of Marine Navigation / 
    Definitions from the US Astronomical Applications Dept.)
    """

    DAY = "day"
    """Any natural primary lighting that is not darkness or civil_twilight"""


@dataclass
class Environment__LightingConditions(TextData):
    """Primary (i.e. dominant) lighting condition that continuously and statically illuminates the relevant traffic
    area."""

    val: Environment__LightingConditionsValue = field(
        default_factory=lambda: no_default(field="Environment__LightingConditions.val"), metadata=required
    )
    """See `Environment__LightingConditionsValue` for possible values. """

    name: Literal["lighting_conditions"] = field(default="lighting_conditions")
    """Is always 'lighting_conditions'"""


@dataclass
class Environment__LightingConditions__Uncertainties(VectorData):
    """
    Uncertainty values for `Environment__LightingConditions` (must accumulate to 1)
    """

    val: tuple[float, float, float, float] = field(
        default_factory=lambda: no_default(field="Environment__LightingConditions__Uncertainties.val"), metadata=required
    )
    """Tuple with class probabilities (must accumulate to 1), in the following order: 
     - darkness
     - artificial
     - civil_twilight
     - day
    """

    name: Literal["environment/lighting_conditions/uncertainties"] = field(
        default="environment/lighting_conditions/uncertainties"
    )
    """Is always 'environment/lighting_conditions/uncertainties'"""


class Environment__RoadConditionValue(str, Enum):
    """Possible values of `Environment__RoadCondition.val`"""

    DRY = "dry"
    """Dry road condition (with good friction)"""

    WET = "wet"
    """Wet road condition (liquid water on the surface causing reduced friction)"""

    SLIPPERY = "slippery"
    """Slippery road conditions not caused by wetness, e.g. ice or leaves"""


@dataclass
class Environment__RoadCondition(TextData):
    """Describes the meteorological road surface condition."""

    val: Environment__RoadConditionValue = field(
        default_factory=lambda: no_default(field="Environment__RoadCondition.val"), metadata=required
    )
    """See `Environment__RoadConditionValue` for possible values. """

    name: Literal["road_condition"] = field(default="road_condition")
    """Is always 'road_condition'"""


@dataclass
class Environment__RoadCondition__Uncertainties(VectorData):
    """
    Uncertainty values for `Environment__RoadCondition` (must accumulate to 1)
    """

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Environment__RoadCondition__Uncertainties.val"), metadata=required
    )
    """Tuple with class probabilities (must accumulate to 1), in the following order: 
     - dry
     - wet
     - slippery
    """

    name: Literal["environment/road_condition/uncertainties"] = field(default="environment/road_condition/uncertainties")
    """Is always 'environment/road_condition/uncertainties'"""


@dataclass
class Environment__VisibilityRange(NumberData):
    """Visibility range in (m). Values can be interpreted based on Meteorological Office 1969 according to Allen Howard Perry and
    Leslie Symons. Highway Meteorology. Taylor & Francis, 2003:

    - > 40 km: excellent
    - 10-40 km: good
    - 4–10 km: moderate
    - 2–4 km: poor
    - 1–2 km: mist
    - 200–1000 m: fog
    - 40–200 m: thick fog
    - < 40 m: dense fog
    """

    val: int = field(default_factory=lambda: no_default(field="Environment__VisibilityRange.val"), metadata=required)
    """Visibility range in (m)."""

    name: Literal["environment/visibility_range"] = field(default="environment/visibility_range")
    """Is always 'environment/visibility_range'"""


@dataclass
class Environment__VisibilityRange__UStdDev(NumberData):
    """Uncertainty for `Environment__VisibilityRange` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Environment__VisibilityRange__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["environment/visibility_range/ustddev"] = field(default="environment/visibility_range/ustddev")
    """Is always 'environment/visibility_range/ustddev'. """


@dataclass
class Environment__PrecipitationIntensity(NumberData):
    """Precipitation intensity in (mm/h). Values can be interpreted based on the Glossary of Meteorology (2012). "Rain". American
    Meteorological Society:

    - 0 mm/h: none
    - 0-2.5 mm/h: light rain
    - 2.6-7.6 mm/h: moderate rain
    - 7.6-50 mm/h: heavy rain
    - 50-100 mm/h: violent rain
    - > 100 mm/h: cloudburst
    """

    val: int = field(default_factory=lambda: no_default(field="Environment__PrecipitationIntensity.val"), metadata=required)
    """Precipitation intensity in (mm/h). """

    name: Literal["environment/precipitation_intensity"] = field(default="environment/precipitation_intensity")
    """Is always 'environment/precipitation_intensity'. """


@dataclass
class Environment__PrecipitationIntensity__UStdDev(NumberData):
    """Uncertainty for `Environment__PrecipitationIntensity` as standard deviation around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Environment__PrecipitationIntensity__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["environment/precipitation_intensity/ustddev"] = field(default="environment/precipitation_intensity/ustddev")
    """Is always 'environment/precipitation_intensity/ustddev'. """


@dataclass
class Environment__Temperature(NumberData):
    """Air temperature in degrees Celsius."""

    val: int = field(default_factory=lambda: no_default(field="Environment__Temperature.val"), metadata=required)
    """The air temperature is rounded to the nearest integer. """

    name: Literal["environment/temperature_celsius"] = field(default="environment/temperature_celsius")
    """Is always 'environment/temperature_celsius'. """


@dataclass
class Environment__Temperature__UStdDev(NumberData):
    """Uncertainty for `Environment__Temperature` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Environment__Temperature__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["environment/temperature/ustddev"] = field(default="environment/temperature/ustddev")
    """Is always 'environment/temperature/ustddev'. """


@dataclass
class Environment__Wind__BeaufortForce(NumberData):
    """
    Wind speed by Beaufort wind force scale:

    - 0: Calm (2 km/h)
    - 1: Light air (2–5 km/h)
    - 2: Light breeze (6–11 km/h)
    - 3: Gentle breeze (12–19 km/h)
    - 4: Moderate breeze (20–28 km/h)
    - 5: Fresh breeze (29–38 km/h)
    - 6: Strong breeze (39–49 km/h)
    - 7: High wind (50–61 km/h)
    - 8: Gale (62–74 km/h)
    - 9: Strong gale (75–88 km/h)
    - 10: Storm (89–102 km/h)
    - 11: Violent storm (103–117 km/h)
    - 12: Hurricane-force (≥ 118 km/h)
    """

    val: int = field(default_factory=lambda: no_default(field="Environment__Wind__BeaufortForce.val"), metadata=required)
    """Wind speed by Beaufort wind force scale"""

    name: Literal["environment/wind/beaufort_force"] = field(default="environment/wind/beaufort_force")
    """Is always 'environment/wind/beaufort_force'"""


@dataclass
class Environment__Wind__BeaufortForce__URadius(NumberData):
    """Uncertainty for `Environment__Wind__BeaufortForce` as radius (plus/minus this value) around the parent indicated value."""

    val: float = field(
        default_factory=lambda: no_default(field="Environment__Wind__BeaufortForce__URadius.val"), metadata=required
    )
    """Uncertainty radius around the parent indicated value. """

    name: Literal["environment/wind/beaufort_force/uradius"] = field(default="environment/wind/beaufort_force/uradius")
    """Is always 'environment/wind/beaufort_force/uradius'."""


@dataclass
class Environment__Wind__Heading(NumberData):
    """Wind heading"""

    val: float = field(default_factory=lambda: no_default(field="Environment__Wind__Heading.val"), metadata=required)
    """Wind heading in radians, CCW with 0 = east according to ENU coordinates."""

    name: Literal["environment/wind/heading"] = field(default="environment/wind/heading")
    """Is always 'environment/wind/heading'"""


@dataclass
class Environment__Wind__Heading__UStdDev(NumberData):
    """Uncertainty for `Environment__Wind__Heading` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Environment__Wind__Heading__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["environment/wind/heading/ustddev"] = field(default="environment/wind/heading/ustddev")
    """Is always 'environment/wind/heading/ustddev'."""


@dataclass
class Environment__CloudCover(NumberData):
    """Cloud cover of the sky."""

    val: int = field(default_factory=lambda: no_default(field="Environment__CloudCover.val"), metadata=required)
    """
    Cloud cover in oktas, i.e. between 0 (completely clear) and 8 (completely cloudy). A value of 9 denotes that the
    sky is obstructed from the view, e.g. in a parking garage.
    """

    name: Literal["environment/cloud_cover"] = field(default="environment/cloud_cover")
    """Is always 'environment/cloud_cover'"""


@dataclass
class Environment__CloudCover__URadius(NumberData):
    """Uncertainty for `Environment__CloudCover` as radius (plus/minus this value) around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Environment__CloudCover__URadius.val"), metadata=required)
    """Uncertainty radius around the parent indicated value. """

    name: Literal["environment/cloud_cover/uradius"] = field(default="environment/cloud_cover/uradius")
    """Is always 'environment/cloud_cover/uradius'."""
