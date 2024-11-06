###############################################################################
#
# BSD 2-Clause License
#
# Copyright (c) 2024, Danil Borchevkin
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################

# *****************************************************************************
# * INCLUDES
# *****************************************************************************

# TODO add includes if needed

# *****************************************************************************
# * FUNCTIONS
# *****************************************************************************

# TODO add functions here

# *****************************************************************************
# * VARIABLES
# *****************************************************************************

SHELL := /bin/bash
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# *****************************************************************************
# * TARGETS - MANDATORY
# *****************************************************************************

# Init repository / project
.PHONY: init
init: clean
	mkdir -p ROOT_DIR/artifacts/build/debug
	mkdir -p ROOT_DIR/artifacts/build/release
	mkdir -p ROOT_DIR/artifacts/reports/check_style
	mkdir -p ROOT_DIR/artifacts/reports/check_static
	mkdir -p ROOT_DIR/artifacts/reports/check_security
	mkdir -p ROOT_DIR/artifacts/reports/test_unit
	mkdir -p ROOT_DIR/artifacts/reports/test_integration
	mkdir -p ROOT_DIR/artifacts/reports/test_e2e


# Clean
.PHONY: clean
clean:
	rm -rf ROOT_DIR/artifacts


# Apply codestyle to all codebase
.PHONY: apply_style
apply_style:
	$(error Target not implemented)


# Check codestyle and return error if ther ere some violence, 
# generate a report into ./artifacts/reports/check_style/
.PHONY: check_style
check_style:
	$(error Target not implemented)


# Run static analyzers, generate an analyze report into ./artifacts/reports/check_static/
.PHONY: check_static
check_static:
	$(error Target not implemented)


# Run security analyzers, generate an analyze report into ./artifacts/reports/check_security/
.PHONY: check_security
check_security:
	$(error Target not implemented)


# Build project in debug configuration
.PHONY: build_debug
build_debug:
	$(error Target not implemented)


# Build project in release configuraiton
.PHONY: build_release
build_release:
	$(error Target not implemented)


# Run unit tests, generate a test report and a gcov report into ./artifacts/reports/test_unit/
.PHONY: test_unit
test_unit: build_debug
	pytest


# Run integration testing and generate artifacts into ./artifacts/reports/test_integration/
.PHONY: test_integration
test_integration: build_debug
	pytest


# Test E2E and generate artifacts into ./artifacts/reports/test_e2e/
.PHONY: test_e2e
test_e2e: build_debug
	$(info Target not implemented)


# Build docs and generate a docs bundle into ./artifacts/docs
.PHONY: docs_build
docs_buld:
	$(error Target not implemented)
	#python -m pydoc -w my_module


# Run debug workflow
.PHONY: all_debug
all_debug:
	init build_debug


# Run release workflow
.PHONY: all_release
all_release:
	init check_style check_static check_security build_release 
	test_unit test_integration docs_build

# *****************************************************************************
# * TARGETS - PROJECT-SPECIFIC
# *****************************************************************************

.PHONY: install
install:
	python setup.py sdist
	pip install .


.PHONY: publish
publish: install
	python3 -m twine upload --repository pypi dist/*

# *****************************************************************************
# * END OF MAKEFILE
# *****************************************************************************