"""Sphinx configuration."""
from datetime import datetime


project = "Othello"
author = "Amos Law"
copyright = f"{datetime.now().year}, {author}"
exclude_patterns = ["_build"]
html_theme = "alabaster"
html_static_path = ["_static"]
