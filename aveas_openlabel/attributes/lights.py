"""Status of the lights on the vehicle"""

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
    no_default,
)


@dataclass
class Lights__Brake(BooleanData):
    """Indicates whether the brake lights are on."""

    val: bool = field(default_factory=lambda: no_default(field="Lights__Brake.val"), metadata=required)
    """True iff the brake lights are on."""

    name: Literal["lights/brake"] = field(default="lights/brake")
    """Is always 'lights/brake'"""


@dataclass
class Lights__Indicator__Left(BooleanData):
    """
    Specifies whether the left turning signal indicator light is set or not.
    This attribute follows the value of the indicator light switch and not the light itself,
    i.e. this attribute stays True throughout the entire blinking process.
    """

    val: bool = field(default_factory=lambda: no_default(field="Lights__Indicator__Left.val"), metadata=required)
    """True iff the left indicator light switch is on."""

    name: Literal["lights/indicator/left"] = field(default="lights/indicator/left")
    """Is always 'lights/indicator/left'"""


@dataclass
class Lights__Indicator__Right(BooleanData):
    """
    Specifies whether the right turning signal indicator light is set or not.
    This attribute follows the value of the indicator light switch and not the light itself,
    i.e. this attribute stays True throughout the entire blinking process.
    """

    val: bool = field(default_factory=lambda: no_default(field="Lights__Indicator__Right.val"), metadata=required)
    """True iff the right indicator light switch is on."""

    name: Literal["lights/indicator/right"] = field(default="lights/indicator/right")
    """Is always 'lights/indicator/right'"""


@dataclass
class Lights__Front(BooleanData):
    """Specifies whether the front lights are on or off."""

    val: bool = field(default_factory=lambda: no_default(field="Lights__Front.val"), metadata=required)
    """True iff the front lights are on."""

    name: Literal["lights/front"] = field(default="lights/front")
    """Is always 'lights/front'"""


@dataclass
class Lights__Daytime(BooleanData):
    """Specifies whether the daytime lights are on or off."""

    val: bool = field(default_factory=lambda: no_default(field="Lights__Daytime.val"), metadata=required)
    """True iff the daytime lights are on."""

    name: Literal["lights/daytime"] = field(default="lights/daytime")
    """Is always 'lights/daytime'"""


@dataclass
class Lights__HighBeam(BooleanData):
    """Specifies whether the high-beam lights are on or off."""

    val: bool = field(default_factory=lambda: no_default(field="Lights__HighBeam.val"), metadata=required)
    """True iff the high beam lights are on."""

    name: Literal["lights/high_beam"] = field(default="lights/high_beam")
    """Is always 'lights/high_beam'"""
