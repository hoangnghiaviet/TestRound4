# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Update configuration ----------------------------------------------------

import pandas as pd
input_config_path = "config.xlsx"
artifact_key_dict = {
    "Attribute Type": "artifact_type",
    "Status": "status",
    "Identifier": "id",
    "Safety Classification": "safety_level",
    "CRQ": "crq",
    "ReqIF.Text": "ReqIF.Text",
    "Title": "title",
    "Verification Criteria": "verify",
    "Created On": "created_on",
    "Description": "description",
    "VAR_FUNC_SYS": "variant",
    "Allocation": "allocation",
    "Modified On": "modified_on",
    "Contributor": "contributor",
    "Creator": "created_by"
}

config_file = pd.read_excel(input_config_path, sheet_name="AttributeMapping")
for index, row in config_file.iterrows():
    key = row["Attribute Name"]
    rst_value = row["New Attribute Name(RST FILE)"]
    if key in artifact_key_dict:
        if str(rst_value) != "nan":
            artifact_key_dict[key] = rst_value

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CodeRace'
copyright = '2023, BGSV'
author = 'EET'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

needs_types = [
               dict(directive="sys_req", title="System Requirement", prefix="SYSTEM_REQ_", color="#ac6dd1", style="artifact"),
               dict(directive="sw_req", title="Software Requirement", prefix="SOFTWARE_REQ_", color="#ac6dd1", style="artifact"),
               dict(directive=artifact_key_dict["Verification Criteria"], title="Verification Criteria", prefix="VC_", color="#fedcd2", style="artifact")
               ]

needs_extra_options = ['url',  'date', 'time', 'test_level']
for (key, value) in artifact_key_dict.items():
    if (key == "Status" and value == "status") or (key == "Identifier" and value == "id"):
        continue
    needs_extra_options.append(value)