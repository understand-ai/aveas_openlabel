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

from typing import Any

import pytest
from uai_openlabel import Uid

from aveas_openlabel.utils import ValidationError, validate_dict_keys_and_value_types


@pytest.mark.parametrize(
    "dict_to_validate,should_raise_exception",
    [
        [{Uid("12"): "INVALID TYPE"}, True],
        [{Uid("12"): 42}, False],
        [{"INVALID KEY": 42}, True],
    ],
)
def test_validate_dict_keys_and_value_types(dict_to_validate: dict, should_raise_exception: bool) -> None:
    validation_template: dict[Any, Any] = {Uid("12"): int}

    if should_raise_exception:
        with pytest.raises(ValidationError):
            validate_dict_keys_and_value_types(dict_to_validate=dict_to_validate, validation_template=validation_template)
    else:
        validate_dict_keys_and_value_types(dict_to_validate=dict_to_validate, validation_template=validation_template)
