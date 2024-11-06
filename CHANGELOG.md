# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.1.2] - 2024-11-07

### Added

- CICD: add `publish.yml` for Github Actions which publish package to PyPI when it released.

### Changed

- DatFile: change encoding from `utf-8` to `utf-8-sig`.


## [0.1.1] - 2024-11-07

### Added

- DatFile: add `filter` method.
- DatFile: add `reverse` method.

### Fixed

- Fix mashups after merge conflicts.


## [0.1.0] - 2024-11-05

### Added

- Added basic imolementation of `izmiran.datfile.Datfile`.
- Added unit tests.
- Added integration tests.
- Added [README.md](./README.md).
- Added this file - [CHANGELOG.md](./CHANGELOG.md).
- Added basic [Makefile](./Makefile).