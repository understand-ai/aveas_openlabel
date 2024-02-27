"""Information on occurring collisions with other objects"""

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
from uai_openlabel import TextData, VectorData, no_default


@dataclass
class Impact__Point(VectorData):  # TODO: Koordinatensystem wie spezifizieren?
    """Point of first contact of the first collision (in this object's coordinates)"""

    val: tuple[float, float] = field(default_factory=lambda: no_default(field="Impact__Point.val"), metadata=required)
    """The (x, y) coordinates of the collision point in (m)."""

    name: Literal["impact/point"] = field(default="impact/point")
    """Is always 'impact/point'"""


@dataclass
class Impact__Point__UStdDev(VectorData):
    """Uncertainty for `Impact__Point` as standard deviation around the parent indicated value."""

    val: tuple[float, float] = field(default_factory=lambda: no_default(field="Impact__Point__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["impact/point/ustddev"] = field(default="impact/point/ustddev")
    """Is always 'impact/point/ustddev'."""


@dataclass
class Impact__Velocity(VectorData):  # TODO: Koordinatensystem wie spezifizieren?
    """Relative velocity of the first contact of the first collision (in this object's coordinates)"""

    val: tuple[float, float] = field(default_factory=lambda: no_default(field="Impact__Velocity.val"), metadata=required)
    """The (x, y) components of impact velocity in (m/s)."""

    name: Literal["impact/velocity"] = field(default="impact/velocity")
    """Is always 'impact/velocity'"""


@dataclass
class Impact__Velocity__UStdDev(VectorData):
    """Uncertainty for `Impact__Velocity` as standard deviation around the parent indicated value."""

    val: tuple[float, float] = field(
        default_factory=lambda: no_default(field="Impact__Velocity__UStdDev.val"), metadata=required
    )
    """Standard deviations around the parent indicated values. """

    name: Literal["impact/velocity/ustddev"] = field(default="impact/velocity/ustddev")
    """Is always 'impact/velocity/ustddev'."""


@dataclass
class Impact__Frame(TextData):
    """Frame ID of the first contact of the first collision."""

    val: str = field(default_factory=lambda: no_default(field="Impact__Frame.val"), metadata=required)
    """The frame ID."""

    name: Literal["impact/frame"] = field(default="impact/frame")
    """Is always 'impact/frame'"""
