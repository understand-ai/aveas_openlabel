from dataclasses import dataclass, field
from typing import Optional, Sequence

from apischema.metadata import required
from uai_openlabel import (
    AttributeName,
    ElementDataPointer,
    FrameInterval,
    ObjectData,
    OntologyUid,
    ResourceUid,
    no_default,
)
from uai_openlabel import (
    Object as OpenLabelObject,
)
from uai_openlabel import (
    ObjectInFrame as OpenLabelObjectInFrame,
)


@dataclass
class Object(OpenLabelObject):
    """
    A structure to represent information about physical entities in scenes.
    Examples of objects are pedestrians, cars, the ego-vehicle, traffic signs, lane markings, building, and trees.

    :param name: A friendly identifier of the element, is not unique but employed by human users to rapidly identify elements in the scene, for example, Peter.
    :param type: The classification of the object
    :param frame_intervals: An array of frame intervals where the object exists.
    :param ontology_uid: A string identifier of the ontology which contains the definition of the type of the element.
    :param resource_uid: A string identifier of the resource which contains additional information on the type of the element.
    :param object_data: Container of static information about the object.
    :param object_data_pointers: Pointers to element data at frames.
    """

    name: str = field(default_factory=lambda: no_default(field="Object.name"), metadata=required)
    type: str = field(default_factory=lambda: no_default(field="Object.type"), metadata=required)

    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    ontology_uid: Optional[OntologyUid] = field(default=None)
    resource_uid: Optional[ResourceUid] = field(default=None)
    object_data: Optional[ObjectData] = field(default=None)
    object_data_pointers: Optional[dict[AttributeName, ElementDataPointer]] = field(default=None)


@dataclass
class ObjectInFrame(OpenLabelObjectInFrame):
    object_data: ObjectData = field(
        default_factory=lambda: no_default(field="ObjectInFrame.object_data"),
        metadata=required,
    )
