#!/usr/bin/env python

"""
A minimal front end to the Docutils Publisher, producing Confluence Wiki output.
"""
try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except ImportError:
    pass
    
from docutils.core import publish_cmdline, default_description
from . import confluence

def main():
    
    description = ('Generates documents in Confluence Wiki format from standalone '
                   'reStructuredText sources.  ' + default_description)
    publish_cmdline(writer=confluence.Writer(), description=description)


if __name__ == '__main__':
    main()
