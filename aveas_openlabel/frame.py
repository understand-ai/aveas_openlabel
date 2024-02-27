"""The `Frame` class and its attributes
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
from typing import Optional, Union

from uai_openlabel import (
    Frame as BaseFrame,
)
from uai_openlabel import (
    FrameProperties as BaseFrameProperties,
)
from uai_openlabel import (
    Number,
    ObjectInFrame,
    ObjectUid,
)


@dataclass
class FrameProperties(BaseFrameProperties):
    """This object contains metadata about this frame."""

    timestamp: Optional[Union[str, Number]] = field(default=None)
    """The timestamp indicates a time instant as a numerical value to describe this frame."""


@dataclass
class Frame(BaseFrame):
    """A frame is a container of dynamic, timewise, information."""

    frame_properties: Optional[FrameProperties] = field(default=None)
    """This field contains information about this frame."""

    objects: Optional[dict[ObjectUid, ObjectInFrame]] = field(default=None)
    """
    This field contains dynamic information on OpenLABEL objects. Object values contain an "object_data" field.
    Dict keys are unique per object in the scenario. 
    Static attributes of an object can be found in `AveasOpenLabel.objects`.
    """
