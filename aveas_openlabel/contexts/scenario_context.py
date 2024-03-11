"""The `ScenarioContext` class and its attributes

The `ScenarioContext` class contains `ScenarioContextData` which provides information about the circumstances of the scenario.
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
from typing import Literal, Union

from apischema.metadata import required
from uai_openlabel import (
    Attributes,
    no_default,
)
from uai_openlabel import (
    Context as BaseContext,
)

from aveas_openlabel.attribute_enforcer import EachAttributeOnlyOnceEnforcer
from aveas_openlabel.contexts.scenario_context_data import (
    Scenario__ContainsHighway,
    Scenario__ContainsRural,
    Scenario__ContainsUrban,
    Scenario__Course,
    Scenario__End__Coordinates,
    Scenario__End__Location,
    Scenario__IsBiased,
    Scenario__IsSampled,
    Scenario__IsSampled__ReferenceToSourceScenario,
    Scenario__IsStaged,
    Scenario__MaximumVehicleSpeed,
    Scenario__MaximumVehicleSpeed__Frame,
    Scenario__MaximumVehicleSpeed__UStdDev,
    Scenario__MinimumVehicleDistanceS,
    Scenario__MinimumVehicleDistanceS__Frame,
    Scenario__MinimumVehicleDistanceS__UStdDev,
    Scenario__MinimumVehicleSpeed,
    Scenario__MinimumVehicleSpeed__Frame,
    Scenario__MinimumVehicleSpeed__UStdDev,
    Scenario__RatioAverageSpeedToSpeedLimit,
    Scenario__RatioAverageSpeedToSpeedLimit__UStdDev,
    Scenario__Start__Coordinates,
    Scenario__Start__Location,
    Scenario__WeekdayNumber,
)


@dataclass
class ScenarioContextData(Attributes, EachAttributeOnlyOnceEnforcer):
    """
    This class contains the attributes of the `ScenarioContext` class.

    They can be retrieved from the `boolean`, `num`, `text`, and `vec` fields according to their type.
    """

    boolean: list[
        Union[
            Scenario__ContainsRural,
            Scenario__ContainsUrban,
            Scenario__ContainsHighway,
            Scenario__IsSampled,
            Scenario__IsBiased,
            Scenario__IsStaged,
        ]
    ] = field(default_factory=lambda: no_default(field="ScenarioContextData.boolean"), metadata=required)
    """The boolean attributes of the `ScenarioContext`"""

    num: list[
        Union[
            Scenario__MinimumVehicleSpeed,
            Scenario__MinimumVehicleSpeed__UStdDev,
            Scenario__MaximumVehicleSpeed,
            Scenario__MaximumVehicleSpeed__UStdDev,
            Scenario__MinimumVehicleDistanceS,
            Scenario__MinimumVehicleDistanceS__UStdDev,
            Scenario__WeekdayNumber,
            Scenario__RatioAverageSpeedToSpeedLimit,
            Scenario__RatioAverageSpeedToSpeedLimit__UStdDev,
        ]
    ] = field(default_factory=lambda: no_default(field="ScenarioContextData.num"), metadata=required)
    """The numeric attributes of the `ScenarioContext`"""

    text: list[
        Union[
            Scenario__Start__Location,
            Scenario__End__Location,
            Scenario__IsSampled__ReferenceToSourceScenario,
            Scenario__MinimumVehicleSpeed__Frame,
            Scenario__MaximumVehicleSpeed__Frame,
            Scenario__MinimumVehicleDistanceS__Frame,
        ]
    ] = field(default_factory=lambda: no_default(field="ScenarioContextData.text"), metadata=required)
    """The textual attributes of the `ScenarioContext`"""

    vec: list[Union[Scenario__Start__Coordinates, Scenario__End__Coordinates, Scenario__Course]] = field(
        default_factory=lambda: no_default(field="ScenarioContextData.vec"), metadata=required
    )
    """The vectorial attributes of the `ScenarioContext`"""


@dataclass
class ScenarioContext(BaseContext):
    """
    An instance of this class is found in the `contexts` dict of the root `AveasOpenLabel` instance.
    """

    name: Literal["scenario_context"] = field(default="scenario_context")
    """Is always 'scenario_context'."""

    type: Literal["ScenarioContext"] = field(default="ScenarioContext")
    """Is always 'ScenarioContext', the Python class representing this object."""

    context_data: ScenarioContextData = field(
        default_factory=lambda: no_default(field="ScenarioContext.context_data"), metadata=required
    )
    """Contains the attributes of the `ScenarioContext`."""
