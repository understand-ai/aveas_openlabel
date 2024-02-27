"""Static attributes of rail vehicles"""

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
from typing import Union

from apischema.metadata import required
from uai_openlabel import ObjectData as BaseObjectData
from uai_openlabel import no_default

from aveas_openlabel.attribute_enforcer import EachAttributeOnlyOnceEnforcer
from aveas_openlabel.attributes.dimension import (
    Dimensions__CenterOfGravity,
    Dimensions__CenterOfGravity__UStdDev,
    Dimensions__Size,
    Dimensions__Size__UStdDev,
)
from aveas_openlabel.attributes.general import (
    AttachedTo,
    Classification__Uncertainties,
    IsRecorder,
)
from aveas_openlabel.attributes.impact import (
    Impact__Frame,
    Impact__Point,
    Impact__Point__UStdDev,
    Impact__Velocity,
    Impact__Velocity__UStdDev,
)
from aveas_openlabel.attributes.operator import (
    Operator__Age,
    Operator__BodyHeight,
    Operator__Gender,
    Operator__Personality,
)
from aveas_openlabel.attributes.summary import (
    Summary__Accel__Max,
    Summary__Accel__Max__UStdDev,
    Summary__Accel__Min,
    Summary__Accel__Min__UStdDev,
    Summary__Coordinates__ScenarioEnd,
    Summary__Coordinates__ScenarioEnd__UStdDev,
    Summary__Coordinates__ScenarioStart,
    Summary__Coordinates__ScenarioStart__UStdDev,
    Summary__Speed__Max,
    Summary__Speed__Max__UStdDev,
    Summary__Speed__Min,
    Summary__Speed__Min__UStdDev,
)


@dataclass
class ObjectData__Unsteerable(BaseObjectData, EachAttributeOnlyOnceEnforcer):
    """
    This class contains the static attributes of rail vehicles.

    They can be retrieved from the `boolean`, `num`, `text` and `vec` fields according to their type.
    """

    boolean: list[Union[IsRecorder]] = field(
        default_factory=lambda: no_default(field="ObjectData__Unsteerable.boolean"), metadata=required
    )
    """Contains all boolean attributes"""

    num: list[
        Union[
            Operator__Age,
            Operator__BodyHeight,
            Summary__Speed__Max,
            Summary__Speed__Max__UStdDev,
            Summary__Speed__Min,
            Summary__Speed__Min__UStdDev,
            Summary__Accel__Max,
            Summary__Accel__Max__UStdDev,
            Summary__Accel__Min,
            Summary__Accel__Min__UStdDev,
        ]
    ] = field(default_factory=lambda: no_default(field="ObjectData__Unsteerable.num"), metadata=required)
    """Contains all numeric attributes"""

    text: list[
        Union[
            AttachedTo,
            Impact__Frame,
            Operator__Gender,
        ]
    ] = field(default_factory=lambda: no_default(field="ObjectData__Unsteerable.text"), metadata=required)
    """Contains all textual attributes"""

    vec: list[
        Union[
            Classification__Uncertainties,
            Dimensions__Size,
            Dimensions__Size__UStdDev,
            Dimensions__CenterOfGravity,
            Dimensions__CenterOfGravity__UStdDev,
            Impact__Point,
            Impact__Point__UStdDev,
            Impact__Velocity,
            Impact__Velocity__UStdDev,
            Operator__Personality,
            Summary__Coordinates__ScenarioStart,
            Summary__Coordinates__ScenarioStart__UStdDev,
            Summary__Coordinates__ScenarioEnd,
            Summary__Coordinates__ScenarioEnd__UStdDev,
        ]
    ] = field(default_factory=lambda: no_default(field="ObjectData__Unsteerable.vec"), metadata=required)
    """Contains all vectorial attributes"""
