"""AVEAS OpenLABEL library root

===============
AVEAS OpenLABEL
===============

Welcome to the documentation for the AVEAS OpenLABEL implementation in Python.
This library supports you in reading and writing AVEAS OpenLABEL JSON files by providing a nested dataclass structure that reflects the JSON schema.

AVEAS OpenLABEL is a subset of the base ASAM OpenLABEL specification.
This means that AVEAS OpenLABEL files are always valid ASAM OpenLABEL files.

The core class of this repository is `AveasOpenLabel`, which represents the root of the AVEAS OpenLabel JSON.

Reading AVEAS OpenLABEL files
-----------------------------

Parsing an existing AVEAS OpenLABEL JSON file can be done with

>>> import json
>>> from aveas_openlabel import AveasOpenLabel
>>> with open("path/to/input.json", "r") as f:
...     content = json.load(f)
>>> aveas_openlabel_example = AveasOpenLabel.from_dict(content)

Writing AVEAS OpenLABEL files
-----------------------------

Writing a populated OpenLABEL dataclass structure to a JSON file is similarly simple

>>> import json
>>> from aveas_openlabel import AveasOpenLabel
>>> aveas_openlabel_example = AveasOpenLabel.minimum_example()
>>> content = aveas_openlabel_example.to_dict()
>>> with open("path/to/file.json", "w") as f:
...     json.dump(content, f)

Obtaining a JSON schema file
----------------------------

A JSON schema file can be extracted from the root AveasOpenLabel class.

>>> import json
>>> from apischema.json_schema import serialization_schema
>>> from aveas_openlabel import AveasOpenLabel
>>> schema = serialization_schema(AveasOpenLabel)
>>> with open("path/to/file.json", "w") as f:
...     json.dump(schema, f)

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


# noinspection PyProtectedMember
from aveas_openlabel.aveas_openlabel import AveasOpenLabel

__all__ = [
    "AveasOpenLabel",
]
