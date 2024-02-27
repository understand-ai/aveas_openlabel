"""Classes associated with an object of classification 'other'"""

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
from uai_openlabel import Object as BaseObject
from uai_openlabel import ObjectInFrame as BaseObjectInFrame
from uai_openlabel import no_default

from aveas_openlabel.object_data.all import ObjectData__All
from aveas_openlabel.object_in_frame_data.all import ObjectInFrameData__All


@dataclass
class OtherObjectInFrame(BaseObjectInFrame):
    """
    This object contains the dynamic attributes of objects with the classification 'other'.

    For the static attributes, see `OtherObject`.
    Instances of this class are found in `Frame` instances inside `AveasOpenLabel.frames`.
    """

    object_data: ObjectInFrameData__All = field(
        default_factory=lambda: no_default(field="OtherObjectInFrame.object_data"), metadata=required
    )
    """Contains the object's dynamic, time-dependent attributes"""


@dataclass
class OtherObject(BaseObject):
    """
    This object contains the static attributes of objects with the classification 'other'.

    For the dynamic attributes, see `OtherObjectInFrame`.
    Instances of this class are found in `AveasOpenLabel.objects`.
    """

    name: str = field(default_factory=lambda: no_default(field="OtherObject.name"), metadata=required)
    """A friendly identifier of the element, is not unique but employed by human users to rapidly identify elements in the scene."""

    type: Literal["other"] = field(default="other")
    """The classification of the object"""

    object_data: ObjectData__All = field(default_factory=lambda: no_default(field="OtherObject.object_data"), metadata=required)
    """Contains the object's static attributes"""
