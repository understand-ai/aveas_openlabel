# AVEAS OpenLABEL

## Installation and usage

This library can be installed via pip using `pip install aveas_openlabel` or with poetry using `poetry add aveas_openlabel`.
The documentation with minimal examples can be found here: [understand-ai.github.io/aveas_openlabel/](https://understand-ai.github.io/aveas_openlabel/)


## Development
### Poetry
This package uses Poetry, a tool for dependency management and packaging. 
Please install it via the official installer from [here](https://python-poetry.org/docs/).
In the root of the repository, you install all dependencies into a virtual environment using `poetry install`. 

### Working with this repository
This repository employs several tools to ensure a constant and good code quality. 

#### Black
[Black](https://black.readthedocs.io/en/stable/index.html) is a code formatter that we use to assure consistent code style across our projects. 
Use it in-between, or after your code changes, via `poetry run black .` in the root directory of this repository. 
Merge requests will only be merge-able if black has nothing to complain about. 

#### MyPy
[Mypy](https://mypy.readthedocs.io/en/stable/) is a static type checker for Python. 
Is assures type safety throughout our code and is necessary to ensure that our AVEAS OpenLABEL format is consistent 
with the base ASAM OpenLABEL format. 
Mypy can be run with `poetry run mypy .` in the root directory of this repository.
Merge requests will only be merge-able if MyPy has nothing to complain about. 

### Ruff
[Ruff](https://docs.astral.sh/ruff/) is a Python linter and code formatter.
It can be run with `poetry run ruff .` in the root directory of this repository.

#### Documentation
Please write docstrings for the class itself and each of its class variables. 
For inspiration of what to write into the docstring, look at the description of the object or field 
in the official ASAM OpenLABEL spec ([link](https://www.asam.net/project-detail/asam-openlabel-v100/)). 
The docstrings allow the use of reStructuredText ([link](https://pydoctor.readthedocs.io/en/latest/docformat/restructuredtext.html)).

We are using [pydoctor](https://pydoctor.readthedocs.io/en/latest/index.html) to automatically generate documentation from the docstrings in our code. 
The documentation generation can be run using `poetry run pydoctor` and is written in the directory `documentation/` 
in the root of this repository.

If administrator privileges required for this operation under MS Windows and poetry is not installed for the administrator account, poetry can be run from Powershell via:

```Start-Process poetry -ArgumentList "run pydoctor" -Verb runAs```

The documentation is ignored from Git, as it is better to generate it by hand from the latest commit. 
