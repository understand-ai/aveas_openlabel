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
from typing import Optional, Sequence, Union

from apischema.metadata import required
from uai_openlabel import (
    URI,
    Context,
    ContextUid,
    CoordinateSystem,
    CoordinateSystemUid,
    EventUid,
    FrameInterval,
    Object,
    ObjectUid,
    OntologyUid,
    ResourceUid,
    Stream,
    StreamUid,
    Uid,
    no_default,
)
from uai_openlabel import (
    DetailedOntology as Ontology,
)
from uai_openlabel import (
    OpenLabel as BaseOpenLabel,
)

from aveas_openlabel.event import Event
from aveas_openlabel.frame import Frame
from aveas_openlabel.metadata import AcquisitionMethod, Metadata, RightOfUse

__all__: list[str] = []


@dataclass
class AveasOpenLabel(BaseOpenLabel):
    """The AVEAS OpenLABEL class.

    The AVEAS OpenLABEL specification is a subset of the standard ASAM OpenLABEL standard.
    Any OpenLABEL file generated according to the AVEAS OpenLABEL specification is always a valid ASAM OpenLABEL file.
    """

    metadata: Metadata = field(default_factory=lambda: no_default(field="AveasOpenLabel.metadata"), metadata=required)
    """
        This JSON object contains metadata about the annotation file itself (see `Metadata`). 
    """

    # actions: NOT SPECIFIED FOR AVEAS OPENLABEL

    contexts: Optional[dict[ContextUid, Context]] = field(default=None)
    """Information on the contexts of the scenario
    """

    coordinate_systems: Optional[dict[CoordinateSystemUid, CoordinateSystem]] = field(default=None)
    """
        This field contains OpenLABEL coordinate systems. 
        Coordinate system keys can be any string, for example, a friendly coordinate system name.
    """

    events: Optional[dict[EventUid, Event]] = field(default=None)
    """
        This field contains the events that occurred in the scenario. 
    """

    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    """
        The interval of frames contained in this scenario. 
    """

    frames: Optional[dict[Uid, Frame]] = field(default=None)
    """
        This field contains the frames that contain the dynamic attributes of the classifications found in `aveas_openlabel.classifications`.
        The keys of this dict are frame IDs. 
    """

    objects: Optional[dict[ObjectUid, Object]] = field(default=None)
    """
        This field contains the static attributes of the classifications found in `aveas_openlabel.classifications`. 
        Each unique object in a scenario is distinguishable by a unique identifier.
    """

    ontologies: Optional[dict[OntologyUid, Union[URI, Ontology]]] = field(default=None)
    """
         This field contains OpenLABEL ontologies. 
         Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs.
         Ontology values may be strings, such as URLs. 
         containing a URI string and optional Sequences of included and excluded terms.
    """

    # relations: NOT SPECIFIED FOR AVEAS OPENLABEL

    resources: Optional[dict[ResourceUid, URI]] = field(default=None)
    """
        This field contains OpenLABEL resources. 
        Resource keys are strings containing numerical UIDs or 32 bytes UUIDs.
        Resource values are strings that describe an external resource, for example, file name, URLs, that may be
        used to link data of the OpenLABEL annotation content with external existing content.
    """

    streams: Optional[dict[StreamUid, Stream]] = field(default=None)
    """
        Streams (cameras, lidars) that were used to record the data. 
        Information about the sensors, such as intrinsic calibration information, is contained in this field. 
    """

    # tags: NOT SPECIFIED FOR AVEAS OPENLABEL

    @classmethod
    def minimum_example(cls: type["AveasOpenLabel"]) -> "AveasOpenLabel":
        return cls(
            metadata=Metadata(
                right_of_use=RightOfUse.RESEARCH_ONLY,
                acquisition_method=AcquisitionMethod.IN_VEHICLE,
                acquisition_partner="foo bar institute",
                acquisition_date="2000-01-01T01:01:01.001Z",
                projection_string="example projection string",
            )
        )
