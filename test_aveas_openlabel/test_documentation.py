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

import doctest
from pathlib import Path
from types import ModuleType

import pytest


def replace_strings_in_doc(module: ModuleType, string: str, replace_with: str) -> None:
    if replace_with[0] != "/":
        # Is a path relative to the git root we need to make absolute
        module_path = module.__path__
        assert len(module_path) == 1, "Case not caught when length is not 1"

        path_to_git_root = Path(module_path[0]).parent
        replacement_path = path_to_git_root / replace_with

        assert replacement_path.exists(), "Relative paths must be relative to the git root"
    else:
        replacement_path = Path(replace_with)
        assert replacement_path.exists(), "Absolute path doesn't exist"

    old_doc = module.__doc__
    if old_doc is not None:
        new_doc = old_doc.replace(string, str(replacement_path))
        module.__doc__ = new_doc


@pytest.mark.xfail
def test_module_root_doc() -> None:
    import aveas_openlabel

    # First example is a file read example
    replace_strings_in_doc(
        aveas_openlabel, string="path/to/input.json", replace_with="test_aveas_openlabel/minimum_openlabel_example.json"
    )

    # Second example is a write example
    replace_strings_in_doc(aveas_openlabel, string="path/to/file.json", replace_with="/dev/null")

    results = doctest.testmod(m=aveas_openlabel)
    assert results.failed == 0
