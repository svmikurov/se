"""Configuration file for the Sphinx documentation builder."""

project = 'SE'
copyright = '2026, Sergei Mikurov'
author = 'Sergei Mikurov'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = []

templates_path: list[str] = ['_templates']
exclude_patterns: list[str] = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme: str = 'alabaster'
html_static_path:  list[str] = ['_static']
