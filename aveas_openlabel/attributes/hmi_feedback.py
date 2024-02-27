"""HMI feedback information"""

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
    no_default,
)


@dataclass
class HmiFeedback__Visual(NumberData):
    """Numeric ID indicating some study-specific visual feedback given to the operator, e.g. via a warning light.
    A value of 0 means that no relevant visual feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document
    referenced in the resources field.

    See also:
    - `HmiFeedback__Acoustic`
    - `HmiFeedback__Other`
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedback__Visual.val"), metadata=required)
    """Numeric ID of the study-specific visual feedback, or 0 if no visual feedback."""

    name: Literal["hmi_feedback/visual"] = field(default="hmi_feedback/visual")
    """Is always 'hmi_feedback/visual'"""


@dataclass
class HmiFeedback__Acoustic(NumberData):
    """Numeric ID indicating some study-specific acoustic feedback given to the operator, e.g. via a warning sound.
    A value of 0 means that no relevant acoustic feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document
    referenced in the resources field.

    See also:
    - `HmiFeedback__Visual`
    - `HmiFeedback__Other`
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedback__Acoustic.val"), metadata=required)
    """Numeric ID of the study-specific acoustic feedback, or 0 if no acoustic feedback"""

    name: Literal["hmi_feedback/acoustic"] = field(default="hmi_feedback/acoustic")
    """Is always 'hmi_feedback/acoustic'"""


@dataclass
class HmiFeedback__Other(NumberData):
    """Numeric ID indicating some study-specific other feedback given to the operator, e.g. haptic feedback.
    A value of 0 means that no relevant other feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document
    referenced in the resources field.

    See also:
    - `HmiFeedback__Visual`
    - `HmiFeedback__Acoustic`
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedback__Other.val"), metadata=required)
    """Numeric ID of the study-specific other feedback, or 0 if no other feedback"""

    name: Literal["hmi_feedback/other"] = field(default="hmi_feedback/other")
    """Is always 'hmi_feedback/other'"""
