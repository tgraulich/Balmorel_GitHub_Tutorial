project = "Balmorel GitHub Tutorial"
copyright = "2024, Tim Aidan Graulich"
author = "Tim Aidan Graulich"
release = "0.1"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

extensions = [
    "myst_parser",  # in order to use markdown
    "sphinx_tabs.tabs",
]

myst_enable_extensions = [
    "colon_fence",  # ::: can be used instead of ``` for better rendering
]

html_theme = "sphinx_rtd_theme"

def setup(app):
    app.add_css_file('css_options.css')  # may also be an URL
