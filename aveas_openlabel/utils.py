from typing import TypeVar

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


K = TypeVar("K")
V = TypeVar("V")


class ValidationError(ValueError):
    ...


def validate_dict_keys_and_value_types(dict_to_validate: dict[K, V], validation_template: dict[K, type[V]]) -> None:
    extra_keys_in_dict = set(dict_to_validate.keys()) - set(validation_template.keys())
    if len(extra_keys_in_dict):
        raise ValidationError(f"The dict to validate has the extra keys {extra_keys_in_dict}")

    missing_keys_from_template = set(validation_template.keys()) - set(dict_to_validate.keys())
    if len(missing_keys_from_template):
        raise ValidationError(f"The dict to validate is missing the keys {missing_keys_from_template}")

    for key in validation_template:
        if not isinstance(dict_to_validate[key], validation_template[key]):
            raise ValidationError(
                f"The dict entry under key {key} should be of type {validation_template[key]} "
                f"but is of type {dict_to_validate[key].__class__.__name__}"
            )
