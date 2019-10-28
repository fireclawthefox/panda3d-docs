# -*- coding: utf-8 -*-
#
# Panda3D documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  1 01:31:55 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import types

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autopackagesummary',
    'variations',
    'sphinx.ext.graphviz',
    'sphinxcontrib.napoleon',
    'sphinx.ext.inheritance_diagram',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Panda3D'
copyright = u'2019 Carnegie Mellon University'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.10'

# This is supposed to be the full version, but it doesn't appear to be used
# anywhere important, and I'm not keen on having to update this continuously.
release = version

# Whether to generate Python or C++ documentation.  TODO:
tags.add('python')

variations = [('python', 'Python'),
              ('cpp', 'C++')]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# Set default settings for embedded graphviz diagrams.
graphviz_dot_args = [
    "-Gfontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Nfontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Efontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Gfontsize=12.00",
    "-Nfontsize=12.00",
    "-Efontsize=12.00",
    "-Gfontcolor=#404040",
    "-Nfontcolor=#404040",
    "-Efontcolor=#404040",
    "-Gcolor=#404040",
    "-Ncolor=#404040",
    "-Ecolor=#404040",
]
graphviz_output_format = "svg"


# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'style_nav_header_background': '#735cdd',
    'logo_only': True,
    'collapse_navigation': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'display_version': False,
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Panda3D Manual"
html_logo = "_static/logo.png"
html_js_files = ['versions.js']

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/panda.css',  # override wide tables in RTD theme
    ],
    'display_github': True,
    'github_user': 'panda3d',
    'github_repo': 'panda3d-docs',
    'github_version': version,
    'conf_py_path': '/',
    'version': version,
}

# Don't copy a _sources dir -- we already have a GitHub link
html_copy_source = False

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Panda3Ddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Panda3D.tex', u'Panda3D Documentation',
   u'Panda3D', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'panda3d', u'Panda3D Documentation',
     [u'Panda3D'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Panda3D', u'Panda3D Documentation',
   u'Panda3D', 'Panda3D', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# When running the linkcheck, don't try any example.net/org/com domains.
linkcheck_ignore = [r'https?://(.+\.)?example\.(com|net|org)(/.*)?']
linkcheck_anchors = False

# Set a list of modules that do bad things when imported, and should not be
# considered for API generation.
# It's fine to keep this list here; it should never grow, because we should not
# introduce new modules that don't have proper __name__ == __main__ checks or
# rely on builtins.
autosummary_mock_imports = [
    'direct.directbase.DirectStart',
    'direct.directbase.TestStart',
    'direct.directbase.ThreeUpStart',
    'direct.directdevices.DirectFastrak',
    'direct.directdevices.DirectJoybox',
    'direct.directdevices.DirectRadamec',
    'direct.directscripts',
    'direct.directtools.DirectSession',
    'direct.directutil.DirectMySQLdb',
    'direct.directutil.DirectMySQLdbConnection',
    'direct.directutil.MemoryLeakHelpers',
    'direct.dist.commands',
    'direct.dist.icon',
    'direct.dist.pefile',
    'direct.dist.pfreeze',
    'direct.leveleditor.LevelEditorStart',
    'direct.leveleditor.testData',
    'direct.p3d.packp3d',
    'direct.p3d.pdeploy',
    'direct.p3d.pmerge',
    'direct.p3d.ppackage',
    'direct.p3d.ppatcher',
    'direct.p3d.runp3d',
    'direct.plugin_installer.make_installer',
    'direct.plugin_installer.make_xpi',
    'direct.plugin_npapi.make_osx_bundle',
    'direct.plugin_standalone.make_osx_bundle',
    'direct.showbase.VerboseImport',
    'direct.wxwidgets.WxPandaShell',
    'direct.wxwidgets.WxPandaStart',
]

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
autodoc_inherit_docstrings = False
autosummary_generate = True
# Prevent prepending module name to all classes/functions
add_module_names = False

inheritance_graph_attrs = {
    "rankdir": "BT",
    #"splines": "ortho",
}
inheritance_node_attrs = {
    "fontsize": 11,
    "style": '""',
}
inheritance_edge_attrs = {
    "arrowsize": 0.75,
    "style": '""',
}


def on_autodoc_skip_member(app, what, name, obj, skip, options):
    # Always document constructors.
    if name == '__init__':
        return False

    # Don't document method aliases.  This also has the side-effect of
    # excluding private members, which is OK.
    if isinstance(obj, types.FunctionType) and obj.__name__ != name:
        return True


def on_builder_inited(app):
    app.builder.get_relative_uri = \
        lambda from_, to, typ=None: \
            app.config.html_absolute_url_root + version + '/' + app.builder.get_target_uri(to, typ)


def on_html_page_context(app, pagename, templatename, context, doctree):
    def pathto(otheruri, resource=False, baseuri=None):
        if resource and '://' in otheruri:
            # allow non-local resources given by scheme
            return otheruri

        if not resource:
            otheruri = app.builder.get_target_uri(otheruri)

        if baseuri is None:
            baseuri = app.config.html_absolute_url_root + version + '/'

        if not baseuri.startswith('/'):
            raise BaseURIError('"baseuri" must be absolute')

        if not otheruri.startswith('/'):
            otheruri = '/' + otheruri

        if otheruri:
            if baseuri.endswith('/'):
                baseuri = baseuri[:-1]
            otheruri = baseuri + otheruri

        uri = otheruri or '#'
        return uri

    context['pathto'] = pathto


def on_config_inited(app, config):
    if config.html_absolute_url_root:
        app.connect('builder-inited', on_builder_inited)
        app.connect('html-page-context', on_html_page_context)

        # This normally runs before our hook, so it still picks up the old
        # pathto, hence we need to register it again
        from sphinx.builders.html import setup_js_tag_helper
        app.connect('html-page-context', setup_js_tag_helper)


# This is an awful hack to get the inheritance graphs to incorporate the
# current variation into the links properly, and, at the same time, not
# generate the arrow connections inverted. :-/
def generate_dot(self, name, urls={}, env=None,
                 graph_attrs={}, node_attrs={}, edge_attrs={}):
    g_attrs = self.default_graph_attrs.copy()
    n_attrs = self.default_node_attrs.copy()
    e_attrs = self.default_edge_attrs.copy()
    g_attrs.update(graph_attrs)
    n_attrs.update(node_attrs)
    e_attrs.update(edge_attrs)
    if env:
        g_attrs.update(env.config.inheritance_graph_attrs)
        n_attrs.update(env.config.inheritance_node_attrs)
        e_attrs.update(env.config.inheritance_edge_attrs)

    res = []  # type: List[str]
    res.append('digraph %s {\n' % name)
    res.append(self._format_graph_attrs(g_attrs))

    for name, fullname, bases, tooltip in sorted(self.class_info):
        if name == 'DTOOL_SUPER_BASE':
            continue

        # Write the node
        this_node_attrs = n_attrs.copy()
        if fullname in urls:
            url = urls[fullname]
            # Fix the URL reference to contain the current variation.
            if env and env.config.graphviz_output_format.lower() == 'svg' and \
               getattr(env.app.builder, 'current_variation', None):
                url = '../' \
                    + env.app.builder.current_variation[0] \
                    + '/reference/' \
                    + os.path.basename(url)

            this_node_attrs['URL'] = '"%s"' % url
            this_node_attrs['target'] = '"_top"'
        if tooltip:
            this_node_attrs['tooltip'] = tooltip
        res.append('  "%s" [%s];\n' %
                   (name, self._format_node_attrs(this_node_attrs)))

        # Write the edges
        for base_name in bases:
            if base_name == 'DTOOL_SUPER_BASE':
                continue
            res.append('  "%s" -> "%s" [%s];\n' %
                       (name, base_name,
                        self._format_node_attrs(e_attrs)))
    res.append('}\n')
    return ''.join(res)


def setup(app):
    from sphinx.ext.inheritance_diagram import InheritanceGraph
    InheritanceGraph.generate_dot = generate_dot

    app.add_config_value('html_absolute_url_root', None, 'html')
    app.connect('config-inited', on_config_inited)

    app.connect('autodoc-skip-member', on_autodoc_skip_member)
