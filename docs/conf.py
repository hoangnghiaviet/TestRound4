# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
project = 'CodeRace'
copyright = '2023, BGSdsffV'
author = 'fdsfdsf'

sys.path.insert(0, os.path.abspath('../source'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

needs_types = [
    dict(directive="sys_req", title="System Requirement",
         prefix="SYSTEM_REQ_", color="#ac6dd1", style="artifact"),
    dict(directive="sw_req", title="Software Requirement",
         prefix="SOFTWARE_REQ_", color="#ac6dd1", style="artifact"),
    dict(directive="verify", title="Verification Criteria",
         prefix="VC_", color="#fedcd2", style="artifact")
]

needs_extra_options = ['created_by', 'url',  'date', 'time',  'safety_level',  'artifact_type', 'crq',
                       'test_level']