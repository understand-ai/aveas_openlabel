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

from apischema.json_schema import serialization_schema

from aveas_openlabel import AveasOpenLabel
from aveas_openlabel.metadata import AcquisitionMethod, Metadata, RightOfUse


def test_json_schema_generation() -> None:
    schema = serialization_schema(AveasOpenLabel)
    assert len(schema) > 0


def test_must_be_instantiable_and_serializable_with_metadata_only() -> None:
    metadata = Metadata(
        right_of_use=RightOfUse.RESEARCH_ONLY,
        acquisition_method=AcquisitionMethod.IN_VEHICLE,
        acquisition_partner="test",
        acquisition_date="yyyy-MM-ddTHH:mm:ss.FFFZ",
        projection_string="example projection string",
        threshold_gttc=1.0,
        threshold_pret=1.0,
        threshold_thw=3.0,
    )
    openlabel = AveasOpenLabel(metadata=metadata)
    openlabel.to_dict()
