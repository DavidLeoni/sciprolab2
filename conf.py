#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is the configuration file of Sphynx, edit it as needed.

import recommonmark
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser
import datetime
import glob
import os
import inspect
import zipfile
import sys
import shutil

on_rtd = os.environ.get('READTHEDOCS') == 'True'

###################   TODO EDIT AS NEEDED !!  ####################

course = "Scientific Programming Labs, 2nd part: Algorithms" 
degree = "Quantitative Computational Biology Master, CIBIO"
author = 'David Leoni' 
copyright = '2017, ' + author                              

#####    'filename' IS *VERY* IMPORTANT !!!!
#####     IT IS PREPENDED IN MANY GENERATED FILES
#####     AND IT SHOULD ALSO BE THE SAME NAME ON READTHEDOCS 
#####     (like i.e. jupman.readthedocs.org)

filename = 'sciprolab2'   # The filename without the extension

#################################################################


FORMATS = ["html", "epub", "latex"]
SYSTEMS = {
    "default" : {
        "name" : "Default system",
        "outdir":"_build/",
        "exclude_patterns": ["_build/*", "templates/exam/server/*", "private/*",  '**.ipynb_checkpoints']
    }
}
MANUALS = {
    "student": {
        "name" : "Scientific Programming Algolab",  # TODO put manual name, like "Scientific Programming"
        "audience" : "studenti",
        "args" : "",
        "output" : "",
        "exclude_patterns" : []
    }
}
manual = 'student'
system = 'default'

project = MANUALS[manual]['name']


# note if I include the project name I can't reference it from index.rst for very silly reasons, see  http://stackoverflow.com/a/23855541

def parse_date(ld):
    try:
        return datetime.datetime.strptime( str(ld), "%Y-%m-%d")
    except:
        print("\n\nERROR! NEED FORMAT 'yyyy-mm-dd', GOT INSTEAD: '" + str(ld) + "'\n\n")
        raise

    
def parse_date_str(ld):
    """
        NOTE: returns a string 
    """
    return str(parse_date(ld)).replace(' 00:00:00','')
    
def warn(msg):
    print("")
    print("   WARNING: " + str(msg))
    print("")

def super_doc_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def get_version(release):
    """ Given x.y.z-something, return x.y  """

    sl = release.split(".")
    return sl[0] + '.' + sl[1]

def zip_folder(folder, zip_path):
    
    ignored = ['.__pycache__', '.ipynb_checkpoints', '.pyc']
    
    def ignored_file(filename):
        for i in ignored:
            if filename.find(i)!=-1:
                return True
    
    folder = folder
    parent_folder = folder[len(os.path.dirname(folder.strip('/')))+1:-1]
    #print("parent_folder = " + parent_folder)
    #print("folder = " + folder)
    archive = zipfile.ZipFile(zip_path, "w")
    for dirname, dirs, files in os.walk(folder):
        #print("dirname=" + dirname)
        dirNamePrefix = dirname + "/*"
        #print("dirNamePrefix=" + dirNamePrefix)
        filenames = glob.glob(dirNamePrefix)
        #print("filenames=" + str(filenames))
        for filename in filenames:
            if os.path.isfile(filename) and not ignored_file(filename) :
                #print('Zipping: %s' % filename)                    
                name = parent_folder + '/' + filename[len(folder):]
                archive.write(filename, name, zipfile.ZIP_DEFLATED)

    archive.close()
        
    print("Wrote " + zip_path)
            
def zip_exercises():
    
    exercises =  glob.glob("exercises/*/")
    if len(exercises) > 0:
        outdir = 'overlay/_static/'
        print("Found stuff in exercises/ , zipping them to " + outdir)
        for d in exercises:
            dir_name= d[len('exercises/'):].strip('/')
            # print("dir_name = " + dir_name)
            zip_name = dir_name + '-exercises.zip'
            zip_path = outdir + zip_name
            zip_folder(d, zip_path)
        print("Done zipping exercises.") 

#zip_exercises()        
        
# Use sphinx-quickstart to create your own conf.py file!
# After that, you have to edit a few things.  See below.

# Select nbsphinx and, if needed, add a math extension (mathjax or pngmath):
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig'
    #, 'rst2pdf.pdfbuilder'
]

# Exclude build directory and Jupyter backup files:
exclude_patterns = ['_build', '**.ipynb_checkpoints', '/README.md', '/readme.md']

# Default language for syntax highlighting in reST and Markdown cells
highlight_language = 'none'

# Don't add .txt suffix to source files (available for Sphinx >= 1.5):
html_sourcelink_suffix = ''



# Execute notebooks before conversion: 'always', 'never', 'auto' (default)
nbsphinx_execute = 'never'   
    
# Use this kernel instead of the one stored in the notebook metadata:
nbsphinx_kernel_name = 'python3'

# List of arguments to be passed to the kernel that executes the notebooks:
#nbsphinx_execute_arguments = ['--InlineBackend.figure_formats={"png", "pdf"}']

# If True, the build process is continued even if an exception occurs:
#nbsphinx_allow_errors = True

# Controls when a cell will time out (defaults to 30; use -1 for no timeout):
#nbsphinx_timeout = 60

# Default Pygments lexer for syntax highlighting in code cells:
nbsphinx_codecell_lexer = 'ipython3'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Width of input/output prompts used in CSS:
#nbsphinx_prompt_width = '8ex'

# If window is narrower than this, input/output prompts are on separate lines:
#nbsphinx_responsive_width = '700px'

# -- The settings below this line are not specific to nbsphinx ------------

master_doc = 'index'



linkcheck_ignore = [r'http://localhost:\d+/']

# -- Get version information from Git -------------------------------------

try:
    from subprocess import check_output
    release = check_output(['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
    if not '.' in release[0]:
        release = '0.1.0'
        #print("Couldn't find git tag, defaulting to: " + release)
    #else:    
    #   print("Detected release from git: " + str(release))
except Exception:
    release = '0.1.0'
    #print("Couldn't find git version, defaulting to: " + release)

version  = get_version(release)
# -- Options for HTML output ----------------------------------------------

html_title = project + ' version ' + release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]    

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# DAVID: THE html_static_path SETTING WITH '_static' IS CRAP, IT JUST MARGES INSIDE _STATIC ALL THE FILES IGNORING THE SUBDIRECTORIES ! THE 'html_extra_path' IS MUCH BETTER.

html_static_path = [] 
html_extra_path = ['overlay'] 


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'


# -- Options for LaTeX output ---------------------------------------------# -- Options for LaTeX output ---------------------------------------------

#latex_elements = {
#    'papersize': 'a4paper',
#    'preamble': r"""
#\usepackage[sc,osf]{mathpazo}
#\linespread{1.05}  % see http://www.tug.dk/FontCatalogue/urwpalladio/
#\renewcommand{\sfdefault}{pplj}  % Palatino instead of sans serif
#\IfFileExists{zlmtt.sty}{
#    \usepackage[light,scaled=1.05]{zlmtt}  % light typewriter font from lmodern
#}{
#    \renewcommand{\ttdefault}{lmtt}  % typewriter font from lmodern
#}
#""",
#}


latex_show_urls = 'footnote'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, filename + '.tex', project,
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, filename, project,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, filename, project,
     author, project, '',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_basename = filename
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


# -- Options for PDF output --------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.


pdf_documents = [
   ('index', filename, project, author.replace(",","\\"))
]
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']
# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']
# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed = False
# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
#pdf_language = "en_US"
# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"
# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0
# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'
# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True
# verbosity level. 0 1 or 2
#pdf_verbosity = 0
# If false, no index is generated.
#pdf_use_index = True
# If false, no modindex is generated.
#pdf_use_modindex = True
# If false, no coverpage is generated.
#pdf_use_coverpage = True
# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'
# Documents to append as an appendix to all manuals.
#pdf_appendices = []
# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False
# Set the default DPI for images
#pdf_default_dpi = 72
# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extensions = ['vectorpdf']
# Page template name for "regular" pages
#pdf_page_template = 'cutePage'
# Show Table Of Contents at the beginning?
#pdf_use_toc = True
# How many levels deep should the table of contents be
pdf_toc_depth = 9999
# Add section number to section references
pdf_use_numbered_links = False
# Background images fitting mode
pdf_fit_background_mode = 'scale'

def setup(app):    

        app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst':True
        }, True)
        app.add_transform(AutoStructify)
        app.add_javascript('js/jupman.js')
        app.add_stylesheet('css/jupman.css')        
        zip_exercises()    
                
        # let's keep this specific to algolab for now: 
        print('Copying root algolab.py to exercises subdirs ...')
        subdirs = ['trees', 'graphs']
        for subdir in subdirs: 
            target = 'exercises/%s/algolab.py' % subdir
            shutil.copyfile('algolab.py', target)        
            print('Overwrote ' + target)


exclude_patterns.extend(MANUALS[manual]['exclude_patterns'])
exclude_patterns.extend(SYSTEMS[system]['exclude_patterns'])

templates_path = ['templates']

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
