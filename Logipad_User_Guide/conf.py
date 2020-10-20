# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LP-Docs'
copyright = '2020, DextraData GmbH'
author = 'Dirk Leese'

# The full version, including alpha/beta/rc tags
release = '1.0.0'
numfig = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

]

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {

}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./_static']
html_logo = './_images/logipad-aero-logo-black.png'

html_sidebars = {
    '**': [
        'searchbox.html',
        'navigation.html',
       
    ]
}

## Customized latex options
# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'pdflatex'
latex_toplevel_sectioning = 'chapter'
latex_additional_files = [
                            './_templates/DDSTyle.sty',
                            './_images/logipad-aero-logo-black.png',
                            './_images/DD-logo.png',
                            './_images/DD-stripes.png'
                        ]

f = open('./_templates/DDTitle.tex','r+')
DDTITLE = f.read();

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'extraclassoptions': 'openany',
    'papersize': 'a4paper',
    'releasename':" ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',
    
    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
       \usepackage{DDStyle}
    ''',

    'maketitle': DDTITLE,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0.443,0.160,0.282}, \
        InnerLinkColor={rgb}{0.443,0.160,0.282}, \
        OuterLinkColor={rgb}{0.443,0.160,0.282}',
        'tableofcontents':' ',
}