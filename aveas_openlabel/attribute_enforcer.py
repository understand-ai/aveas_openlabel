"""A subclass of Attributes that allows for specifying optional and required attributes

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


from dataclasses import dataclass
from typing import Iterable


class AttributeTypesNotUniqueError(Exception):
    """Exception that is raised when the class is instantiated with two attributes of the same type."""

    def __init__(self, non_unique_types: Iterable[type]):
        super().__init__(
            f"Each Attribute type may only be provided once. This is not the case for {[o.__name__ for o in non_unique_types]}."
        )


@dataclass
class EachAttributeOnlyOnceEnforcer:
    """A base class for all Attribute classes that enforce optional and required attributes."""

    def _attribute_type_list(self) -> list[type]:
        attribute_type_list: list[type] = list()
        for dataclass_field in self.__dataclass_fields__.keys():
            value = getattr(self, dataclass_field)
            if value is None or isinstance(value, str):
                continue
            for attribute in value:
                attribute_type_list.append(attribute.__class__)
        return attribute_type_list

    def __post_init__(self) -> None:
        attribute_type_list = self._attribute_type_list()
        attribute_type_set = set(attribute_type_list)

        if len(attribute_type_list) != len(attribute_type_set):
            non_unique_types = [a for a in attribute_type_set if attribute_type_list.count(a) > 1]
            raise AttributeTypesNotUniqueError(non_unique_types)
