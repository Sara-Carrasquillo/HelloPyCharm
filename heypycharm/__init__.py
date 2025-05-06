# heypycharm/__init__.py
"""
 -- Metadata heypycharm: Utilities for intermediate-to-advanced Python review.
"""
# Module docstring describing the package; helps tools like Sphinx and other documentation generators understand your package at a glance.

# Package version following PEP 396; allows users and tools to introspect which release is installed.
__version__ = "0.1.0"

# Author metadata; optional but a common convention for identifying maintainers.
__author__  = "Sara Carrasquillo"

# Contact email for issues or pull requests; useful if you’re publishing publicly.
__email__   = "SaraCarrasquillo007@gmail.com"

# License example declaration for open-source clarity and legal compliance.
__license__ = "MIT"

# Importing logging to configure package logging without imposing handlers on users.
import logging

# Attach a NullHandler so library consumers don’t get “No handler found” warnings by default.
logging.getLogger(__name__).addHandler(logging.NullHandler())

# --- Public API Exports ---

# Expose python_basics at the package level
from .basics import python_basics

# Expose python_intermediate at the package level for convenience.
from .intermediate import python_intermediate

# Expose python_advanced at the package level to flatten your namespace.
from .advanced import python_advanced

# Controls what `from heypycharm import *` will import; keeps your public API explicit.
__all__ = [
    "python_basics",
    "python_intermediate",
    "python_advanced",
]

# --- !Avoid Heavy Imports! ---
# Do NOT import requests, numpy, pandas, tkinter, flask, etc. in __init__.py.
# Those modules belong in their respective submodules to prevent slow import times and unnecessary dependencies.
