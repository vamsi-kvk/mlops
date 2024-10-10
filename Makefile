# Makefile for Project

# Variables
PYTHON = python
PYTEST = pytest
FLAKE8 = flake8
COV_REPORT_DIR = htmlcov

# Default target
.PHONY: all
all: install install-dev lint test run

# Install production dependencies
.PHONY: install
install:
	@echo "Installing production dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

# Install development dependencies
.PHONY: install-dev
install-dev:
	@echo "Installing development dependencies..."
	$(PYTHON) -m pip install -r requirements-dev.txt

# Run the project
.PHONY: run
run:
	@echo "Running the project..."
	$(PYTHON) main.py

# Run tests and generate coverage report
.PHONY: test
test:
	@echo "Running tests and generating coverage report..."
	$(PYTEST) --cov=src --cov-report=html --cov-report=xml tests/

# Run linting
.PHONY: lint
lint:
	@echo "Running flake8 linting..."
	$(FLAKE8) src tests

# Clean up coverage reports
.PHONY: clean
clean:
	@echo "Cleaning up coverage reports..."
	rm -rf $(COV_REPORT_DIR) coverage.xml

# Run all tasks: clean, install, install-dev, lint, test, and run
.PHONY: all
all: clean install install-dev lint test run