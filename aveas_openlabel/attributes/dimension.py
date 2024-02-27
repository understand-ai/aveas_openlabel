"""Size and center of gravity"""

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
from uai_openlabel import VectorData, no_default


@dataclass
class Dimensions__Size(VectorData):  # TODO: Koordinatensystem wie spezifizieren?
    """Size of this object"""

    val: tuple[float, float, float] = field(default_factory=lambda: no_default(field="Dimensions__Size.val"), metadata=required)
    """The (x, y, z) extent of the object in (m)."""

    name: Literal["dimensions/size"] = field(default="dimensions/size")
    """Is always 'dimensions/size'"""


@dataclass
class Dimensions__Size__UStdDev(VectorData):
    """Uncertainty for `Dimensions__Size` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Dimensions__Size__UStdDev"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["dimensions/size/ustddev"] = field(default="dimensions/size/ustddev")
    """Is always 'dimensions/size/ustddev'."""


@dataclass
class Dimensions__CenterOfGravity(VectorData):  # TODO: Koordinatensystem wie spezifizieren?
    """Center of gravity of this object, relative to the center of the bounding box."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Dimensions__CenterOfGravity.val"), metadata=required
    )
    """The (x, y, z) offset of the center of gravity relative to the center of the bounding box. """

    name: Literal["dimensions/center_of_gravity"] = field(default="dimensions/center_of_gravity")
    """Is always 'dimensions/center_of_gravity'"""


@dataclass
class Dimensions__CenterOfGravity__UStdDev(VectorData):
    """Uncertainty for `Dimensions__CenterOfGravity` as standard deviation around the parent indicated value."""

    val: tuple[float, float, float] = field(
        default_factory=lambda: no_default(field="Dimensions__CenterOfGravity__UStdDev.val"), metadata=required
    )
    """Standard deviation around the parent indicated value. """

    name: Literal["dimensions/center_of_gravity/ustddev"] = field(default="dimensions/center_of_gravity/ustddev")
    """Is always 'dimensions/center_of_gravity/ustddev'."""
