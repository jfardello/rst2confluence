#!/usr/bin/env python
import imp
from setuptools import setup, find_packages

f, filename, description = imp.find_module('src/rst2confluence')
rst2confluence = imp.load_module('rst2confluence', f, filename, description)


setup(name='rst2confluence',
      version = rst2confluence.__version__,
      description='reStructuredText-to-Confluence markup converter',
      author='Kenichiro TANAKA',
      author_email='tanaka.kenichiro@gmail.com',
      maintainer='Christian Weiske',
      maintainer_email='christian.weiske@netresearch.de',
      url='https://github.com/cweiske/rst2confluence',
      packages=find_packages('src'),
      py_modules=['rst2confluence.confluence'],
      install_requires=['docutils'],
      test_suite = "tests.suite",
      package_dir = {'': 'src'},
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
      ],
      entry_points={
        'console_scripts': [
            'rst2confluence = rst2confluence.cli:main',
            ],
      },
      
     )
