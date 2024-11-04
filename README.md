# Project Name

## Description

IZMIRAN library for common tasks

## Documents

No additional documents are provided.

## Software Requirements

* Python 3.7+
* make

## Dependencies

* pytest
* yapf
* bandit

## Usage and installation

```bash
$ pip install izmiran
```

## Developing Process

* Used feature-flow for developing

## Release Process

### Release Process - Steo 0 - Verify and validate codebase

Run:

```bash
make all_release
```

### Release Process - Step 1 - Update version

Go to `setup,py` and update `version`

### Release Process - Step 2 - Update CHANGELOG.md

Go to `CHANGELOG.md` and update it.

### Check installation of target

```bash
$ python setup.py sdist
