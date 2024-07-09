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
from uai_openlabel import ObjectUid, TextData, VectorData, no_default


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


@dataclass
class Impact__gTTC__ObjectIds(VectorData):
    """
    Object IDs of the opposing traffic participants with a geometrical time-to-collision (gTTC) lower than
    the value "threshold_gttc" in `Metadata`.
    """

    val: tuple[ObjectUid, ...] = field(
        default_factory=lambda: no_default(field="Impact__gTTC__ObjectIds.val"), metadata=required
    )
    """The object IDs of the opposing traffic participants."""

    name: Literal["impact/gttc/object_ids"] = field(default="impact/gttc/object_ids")
    """Is always 'impact/gttc/object_ids'."""


@dataclass
class Impact__gTTC__Values(VectorData):
    """Values of the geometrical time-to-collision (gTTC) for the traffic participants mentioned in `Impact__gTTC__ObjectIds`."""

    val: tuple[float, ...] = field(default_factory=lambda: no_default(field="Impact__gTTC__Values.val"), metadata=required)
    """Values of the geometrical time-to-collision (gTTC)."""

    name: Literal["impact/gttc/values"] = field(default="impact/gttc/values")
    """Is always 'impact/gttc/values'."""


@dataclass
class Impact__PrET__ObjectIds(VectorData):
    """
    Object IDs of the opposing traffic participants with a predicted encroachment time (PrET) lower than
    the value "threshold_pret" in `Metadata`.
    """

    val: tuple[ObjectUid, ...] = field(
        default_factory=lambda: no_default(field="Impact__PrET__ObjectIds.val"), metadata=required
    )
    """The object IDs of the opposing traffic participants."""

    name: Literal["impact/pret/object_ids"] = field(default="impact/pret/object_ids")
    """Is always 'impact/pret/object_ids'."""


@dataclass
class Impact__PrET__Values(VectorData):
    """Values of the predicted encroachment time (PrET) for the traffic participants mentioned in `Impact__PrET__ObjectIds`."""

    val: tuple[float, ...] = field(default_factory=lambda: no_default(field="Impact__PrET__Values.val"), metadata=required)
    """Values of the predicted encroachment time (PrET)."""

    name: Literal["impact/pret/values"] = field(default="impact/pret/values")
    """Is always 'impact/pret/values'."""


@dataclass
class Impact__THW__ObjectIds(VectorData):
    """
    Object IDs of the opposing traffic participants with a time headway (THW) lower than
    the value "threshold_thw" in `Metadata`.
    """

    val: tuple[ObjectUid, ...] = field(
        default_factory=lambda: no_default(field="Impact__THW__ObjectIds.val"), metadata=required
    )
    """The object IDs of the opposing traffic participants."""

    name: Literal["impact/thw/object_ids"] = field(default="impact/thw/object_ids")
    """Is always 'impact/thw/object_ids'."""


@dataclass
class Impact__THW__Values(VectorData):
    """Values of the time headway (THW) for the traffic participants mentioned in `Impact__THW__ObjectIds`."""

    val: tuple[float, ...] = field(default_factory=lambda: no_default(field="Impact__THW__Values.val"), metadata=required)
    """Values of the time headway (THW)."""

    name: Literal["impact/thw/values"] = field(default="impact/thw/values")
    """Is always 'impact/thw/values'."""
