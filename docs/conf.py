# Project information
project = 'DexRobot Python SDK'
copyright = '2024, DexRobot'
author = 'DexRobot'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx.ext.intersphinx',  # Link to other project's documentation
    'sphinx_autodoc_typehints'  # Better type hints support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_rtype = True
