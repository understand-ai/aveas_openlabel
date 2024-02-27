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
from typing import Union

import pytest
from uai_openlabel import Attributes, BooleanData, NumberData, TextData, VectorData

from aveas_openlabel.attribute_enforcer import (
    AttributeTypesNotUniqueError,
    EachAttributeOnlyOnceEnforcer,
)


@dataclass
class SomeBoolean(BooleanData):
    val: bool = True


@dataclass
class SomeNumber(NumberData):
    val: int = 1


@dataclass
class SomeText(TextData):
    val: str = "ABC"


@dataclass
class SomeVector(VectorData):
    val: list[str] = field(default_factory=lambda: ["A", "B"])


@dataclass
class ValidAttributes(Attributes, EachAttributeOnlyOnceEnforcer):
    @staticmethod
    def _optional_attributes() -> set[type]:
        return {SomeBoolean, SomeNumber}

    @staticmethod
    def _required_attributes() -> set[type]:
        return {SomeText, SomeVector}

    boolean: list[Union[SomeBoolean]]
    num: list[Union[SomeNumber]]
    text: list[Union[SomeText]]
    vec: list[Union[SomeVector]]


def test_enforce_attributes_works_with_valid_config() -> None:
    ValidAttributes(boolean=[SomeBoolean()], num=[SomeNumber()], text=[SomeText()], vec=[SomeVector()])


def test_enforce_attributes_rejects_duplicated_attributes() -> None:
    with pytest.raises(AttributeTypesNotUniqueError, match="SomeBoolean"):
        ValidAttributes(boolean=[SomeBoolean(), SomeBoolean()], num=[SomeNumber()], text=[SomeText()], vec=[SomeVector()])


def test_enforce_attributes_correctly_handles_uniterable_values() -> None:
    @dataclass
    class InvalidAttributes(Attributes, EachAttributeOnlyOnceEnforcer):
        @staticmethod
        def _optional_attributes() -> set[type]:
            return set()

        @staticmethod
        def _required_attributes() -> set[type]:
            return {SomeBoolean}

        boolean: list[Union[SomeBoolean]]
        num: None
        text: str  # type: ignore

    InvalidAttributes(boolean=[SomeBoolean()], num=None, text="abc")
