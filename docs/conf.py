"""Sphinx configuration."""
from datetime import datetime


project = "Othello-CLI"
author = "Amos Law"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
exclude_patterns = ["_build"]
