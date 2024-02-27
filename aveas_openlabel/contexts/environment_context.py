"""The `EnvironmentContext` class and its attributes

The `EnvironmentContext` class contains `EnvironmentContextData` which provides information about the circumstances of the environment.
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
from aveas_openlabel.contexts.environment_context_data import (
    Environment__CloudCover,
    Environment__CloudCover__URadius,
    Environment__LightingConditions,
    Environment__LightingConditions__Uncertainties,
    Environment__PrecipitationIntensity,
    Environment__PrecipitationIntensity__UStdDev,
    Environment__RoadCondition,
    Environment__RoadCondition__Uncertainties,
    Environment__Temperature,
    Environment__Temperature__UStdDev,
    Environment__VisibilityRange,
    Environment__VisibilityRange__UStdDev,
    Environment__Wind__BeaufortForce,
    Environment__Wind__BeaufortForce__URadius,
    Environment__Wind__Heading,
    Environment__Wind__Heading__UStdDev,
)


@dataclass
class EnvironmentContextData(Attributes, EachAttributeOnlyOnceEnforcer):
    """
    This class contains the attributes of the `EnvironmentContext` class.

    They can be retrieved from the `num` and `text` fields according to their type.
    """

    num: list[
        Union[
            Environment__CloudCover,
            Environment__CloudCover__URadius,
            Environment__PrecipitationIntensity,
            Environment__PrecipitationIntensity__UStdDev,
            Environment__Temperature,
            Environment__Temperature__UStdDev,
            Environment__VisibilityRange,
            Environment__VisibilityRange__UStdDev,
            Environment__Wind__BeaufortForce,
            Environment__Wind__BeaufortForce__URadius,
            Environment__Wind__Heading,
            Environment__Wind__Heading__UStdDev,
        ]
    ] = field(default_factory=lambda: no_default(field="EnvironmentContextData.num"), metadata=required)
    """The numeric attributes of the `EnvironmentContext`"""

    text: list[
        Union[
            Environment__LightingConditions,
            Environment__RoadCondition,
        ]
    ] = field(default_factory=lambda: no_default(field="EnvironmentContextData.text"), metadata=required)
    """The textual attributes of the `EnvironmentContext`"""

    vec: list[
        Union[
            Environment__LightingConditions__Uncertainties,
            Environment__RoadCondition__Uncertainties,
        ]
    ] = field(default_factory=lambda: no_default(field="EnvironmentContextData.vec"), metadata=required)
    """The vectorial attributes of the `EnvironmentContext`"""


@dataclass
class EnvironmentContext(BaseContext):
    """
    An instance of this class is found in the `contexts` dict of the root `AveasOpenLabel` instance.
    """

    name: Literal["environment_context"] = field(default="environment_context")
    """Is always 'environment_context'."""

    type: Literal["EnvironmentContext"] = field(default="EnvironmentContext")
    """Is always 'EnvironmentContext', the Python class representing this object."""

    context_data: EnvironmentContextData = field(
        default_factory=lambda: no_default(field="EnvironmentContext.context_data"), metadata=required
    )
    """Contains the attributes of the `EnvironmentContext`."""
