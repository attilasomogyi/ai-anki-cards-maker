project = 'Anki Cards Maker'
copyright = '2023, Attila Zsolt Somogyi'
author = 'Attila Zsolt Somogyi'
release = 'latest'
version = 'latest'

github_username = 'attilasomogyi'
github_repository = 'ankicardmaker'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgconverter',
    'sphinx_copybutton',
    'sphinx.ext.extlinks',
    'sphinx_toolbox',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']

html_theme = 'furo'
html_static_path = ['_static']
html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']
