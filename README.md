![Workflow status badge](https://github.com/software-students-spring2024/3-python-package-exercise-snailman/actions/workflows/build.yml/badge.svg)
# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Description

[wordutilities](https://test.pypi.org/project/wordutilities/): A Python package that provides some functions related to English-language words.

## Contributing

### Set up virtual environment:

1. Install [pipenv](https://github.com/nyu-software-engineering/python-package-example?tab=readme-ov-file) if not already installed.
2. Clone the repository.
3. Run `pipenv shell` in your cloned repository.

### Install dependencies:

Run `pipenv install` in your virtual environment.

### Build package:

1. Run `python -m build` in the directory where `pyproject.toml` is located.
2. Verify that the built .tar archive has the correct contents using 'tar --list -f dist/wordutilities-[package-version].tar.gz'

### Test package:

1. Run `pytest` in the project directory.

## Teammates

* [Corina Luca](https://github.com/CorinaLucaFocsan)
* [Jakob Hablitz](https://github.com/jsh9965)
* [Josckar Palomeque-Elias](https://github.com/josckar)
* [Stella Zhang](https://github.com/qq3173732005)