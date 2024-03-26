"""Contains the `Metadata` class
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
    Metadata as BaseMetadata,
)
from uai_openlabel import (
    no_default,
)


class RightOfUse(str, Enum):
    """Possible values of 'right_of_use'."""

    COMMERCIAL = "commercial"
    """Commercial use of data allowed. Implying also usage for research purposes."""

    RESEARCH_ONLY = "research_only"
    """Data can only be used for research purposes."""


class AcquisitionMethod(str, Enum):
    """Possible values of 'acquisition_method'."""

    AERIAL = "aerial"
    """Aerial acquisition with plane."""

    STATIONARY = "stationary"
    """Stationary data acquisition, e.g. with infrastructure sensors."""

    IN_VEHICLE = "in-vehicle"
    """Data acquisition with moving recording vehicle."""


@dataclass
class Metadata(BaseMetadata):
    """This JSON object contains metadata about the annotation file itself."""

    aveas_schema_version: Literal["0.4.10"] = field(default="0.4.10")
    """The version of the aveas_openlabel library used to generate this file."""

    right_of_use: RightOfUse = field(default_factory=lambda: no_default(field="Metadata.right_of_use"), metadata=required)
    """Specifies the usage rights of the data."""

    acquisition_method: AcquisitionMethod = field(
        default_factory=lambda: no_default(field="Metadata.acquisition_method"), metadata=required
    )
    """Specifies the acquisition method used for obtaining the data in this file."""

    acquisition_partner: str = field(
        default_factory=lambda: no_default(field="Metadata.acquisition_partner"), metadata=required
    )
    """
    Institution or company involved in recording the data in this file. 
    This is a free-text field that may contain copyright information. 
    """

    acquisition_date: str = field(default_factory=lambda: no_default(field="Metadata.acquisition_date"), metadata=required)
    """
    The date on which the data were acquired in the format yyyy-MM-ddTHH:mm:ss.FFFZ. 
    Here, 'T' is used as time designator. '.' is used as separator for the following millisecond portion. 

    - yyyy: Year (four digits), ex. 2021
    - MM: Month with leading zero, ex. 09
    - dd: Day in month with leading zero
    - mm: Minutes with leading zero
    - ss: seconds with leading zero
    - FFF: Milliseconds with leading zeros
    - Z: 'Z' if the time zone is UTC, '±[hh]:[mm]', '±[hh][mm]', or '±[hh]' otherwise, ex. '+0100'
    """

    projection_string: str = field(default_factory=lambda: no_default(field="Metadata.projection_string"), metadata=required)
    """
    The geographic reference system used for the coordinates in this OpenLABEL-file and in corresponding OpenDRIVE-files. 
    Projection strings follow official parameter sets for proj-strings from EPSG.
    """
