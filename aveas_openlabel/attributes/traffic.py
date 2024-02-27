"""Traffic density and intensity"""

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
    NumberData,
    NumberType,
    no_default,
)


@dataclass
class Traffic__Density(NumberData):
    """Density of the traffic on the road section the vehicle is currently on.

    The density of the traffic is the number of vehicles with the center of their bounding box within
    a 50m range before and after the vehicle containing this attribute.

    The vehicle containing this attribute is counted as well.
    """

    val: float = field(default_factory=lambda: no_default(field="Traffic__Density.val"), metadata=required)
    """Number of vehicles """

    name: Literal["traffic/density"] = field(default="traffic/density")
    """Is always 'traffic/density'"""

    type: Literal[NumberType.Value] = field(default=NumberType.Value)
    """Is always 'value'"""


@dataclass
class Traffic__Density__UStdDev(NumberData):
    """Uncertainty for `Traffic__Density` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Traffic__Density__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["traffic/density/ustddev"] = field(default="traffic/density/ustddev")
    """Is always 'traffic/density/ustddev'. """


@dataclass
class Traffic__Volume(NumberData):
    """Intensity of the traffic on the road section the vehicle is currently on.

    The intensity of the traffic is measured over a time frame of at least 10 minutes.
    The unit of the traffic intensity is vehicles per hour.

    The vehicle containing this attribute is counted as well.
    """

    val: float = field(default_factory=lambda: no_default(field="Traffic__Volume.val"), metadata=required)
    """The traffic intensity in vehicles per hour"""

    name: Literal["traffic/volume"] = field(default="traffic/volume")
    """Is always 'traffic/volume'"""

    type: Literal[NumberType.Value] = field(default=NumberType.Value)
    """Is always 'value'"""


@dataclass
class Traffic__Volume__UStdDev(NumberData):
    """Uncertainty for `Traffic__Volume` as standard deviation around the parent indicated value."""

    val: float = field(default_factory=lambda: no_default(field="Traffic__Volume__UStdDev.val"), metadata=required)
    """Standard deviation around the parent indicated value. """

    name: Literal["traffic/volume/ustddev"] = field(default="traffic/volume/ustddev")
    """Is always 'traffic/volume/ustddev'. """
