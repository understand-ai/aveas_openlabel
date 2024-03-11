"""The `Event` class and its attributes

The `Event` class contains `EventData` which provides information about the event.
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
from enum import Enum
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    Attributes,
    FrameInterval,
    ObjectUid,
    TextData,
    TextType,
    VectorData,
    VectorType,
    no_default,
)
from uai_openlabel import (
    Event as BaseEvent,
)


@dataclass
class RoleAParticipantID(TextData):
    """Participant ID of traffic participant with Role A. Role A is dependent on the event type.

    lane change :       vehicle performing the lane change
    parking     :       vehicle performing the parking maneuver
    turning     :       vehicle that is turning/crossing
    overtaking  :       vehicle that is overtaking
    following   :       vehicle that is following

    """

    val: ObjectUid = field(default_factory=lambda: no_default(field="RoleAParticipantID.val"), metadata=required)
    """The ID of the traffic participant with Role A. This is the same ID as used for identifying the object. """

    name: Literal["event_participant/role_a_id"] = field(default="event_participant/role_a_id")
    """Is always 'event_participant/role_a_id'"""

    type: Literal[TextType.Value] = field(default=TextType.Value)
    """Is always 'value'"""


@dataclass
class RoleBParticipantIDs(VectorData):
    """Participant IDs of traffic participants with Role B. Role B is dependent on the event type.

    lane change :       empty
    parking     :       vehicles passing the Role A vehicle during the parking event and using the lane closest to the Role A vehicle
    turning     :       vehicles being within the scene during the turning event of the Role A vehicle and whose line of movement crosses the one of the Role A vehicle
    overtaking  :       vehicles that are being overtaken by the Role A vehicle
    following   :       vehicle that is being followed by the Role A vehicle (the vehicle immediately in front)

    """

    val: list[ObjectUid] = field(default_factory=lambda: no_default(field="RoleBParticipantIDs.val"), metadata=required)
    """The IDs of the traffic participant with Role B. This is the same ID as used for identifying the object. """

    name: Literal["event_participants/role_b_ids"] = field(default="event_participants/role_b_ids")
    """Is always 'event_participants/role_b_ids'"""

    type: Literal[VectorType.Values] = field(default=VectorType.Values)
    """Is always 'values'"""


@dataclass
class EventData(Attributes):
    """
    This class contains the attributes of the `Event` class.

    The attributes can be retrieved from the `text` and `vec` fields according to their type.
    """

    text: list[RoleAParticipantID] = field(default_factory=lambda: no_default(field="EventData.text"), metadata=required)
    """A list containing a single attribute, an instance of `RoleAParticipantID`."""

    vec: list[RoleBParticipantIDs] = field(default_factory=lambda: no_default(field="EventData.vec"), metadata=required)
    """A list containing a single attribute, an instance of `RoleBParticipantIDs`."""


class EventTypeValue(str, Enum):
    """Possible values of `Event.type`."""

    LANE_CHANGE = "lane change"
    """Lane change maneuver."""

    PARKING_MANEUVER = "parking"
    """Parking maneuver."""

    TURNING = "turning"
    """Turning maneuver."""

    OVERTAKING = "overtaking"
    """Overtaking maneuver."""

    FOLLOWING = "following"
    """Following maneuver."""


@dataclass
class Event(BaseEvent):
    """An event in the recording

    An event is an instantaneous situation that happens without a temporal interval.
    Events complement actions providing a mechanism to specify triggers or to connect actions and objects with causality relations.
    """

    event_data: EventData = field(default_factory=lambda: no_default(field="Event.event_data"), metadata=required)
    """Additional data to describe attributes of the event."""

    name: str = field(default_factory=lambda: no_default(field="Event.name"), metadata=required)
    """Name of the event, equal to type of event concatenated with ID of event. """

    frame_intervals: list[FrameInterval] = field(
        default_factory=lambda: no_default(field="Event.frame_intervals"), metadata=required
    )
    """The frame interval during which the event takes place. 
    For a lane change, the start and end frame are the same because we annotate the point in time when the center 
    of a vehicle is over the lane marking crossed during the lane change.
    """

    type: EventTypeValue = field(default_factory=lambda: no_default(field="Event.type"), metadata=required)
    """The type of the event."""
