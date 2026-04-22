
# data_handling

Lightweight utilities for data handling and validation used by the repository.

This package contains small modules to load, validate and normalize input data used by downstream processing. It's intended as a focused utility layer for projects that need consistent input handling and custom exception types.

## Quick summary

- Package name / folder: `data_handling`
- Typical entry point (for local runs): `run.py`
- Key modules:
	- `config.py` — application configuration and constants
	- `exception.py` — custom exceptions used across the package
	- `Input.py` — functions/classes for parsing and validating input
	- `run.py` — simple runner / example usage to exercise the package

## Requirements

- Python 3.8+ (3.10 recommended)
- Project dependencies are listed in `requirements.txt`.

Install dependencies in a virtual environment:

```bash
# macOS / zsh example
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## How to run

Run the package entrypoint script for a simple example or integration test:

```bash
# from the project root (where this README lives at data_handling/README.md)
python run.py
```

If `run.py` requires arguments, consult the module's docstring or open the file to see expected parameters.

## File/Module overview

- `config.py`
	- Central place for configuration constants used by the package (paths, default values, toggles).

- `exception.py`
	- Defines project-specific exception types to provide more meaningful error handling.

- `Input.py`
	- Responsible for ingesting and validating input data. This include parsing CSV, basic schema checks.

- `run.py`
	- Minimal runner script demonstrating how to use the package (or acting as a small CLI). Use it to exercise the package quickly.




