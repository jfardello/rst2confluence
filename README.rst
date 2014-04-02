*********************************************
Convert reStructuredText to Confluence markup
*********************************************

====================
Supported directives
====================

- bullet list
- enumerated list
- image, figure
- definition list
- simple table
- block quote
- text effect

  - strong
  - emphasis
  - monospace
- code blocks
- links
- admonitions

  - info
  - note
  - tip
  - warning
- field lists
- line blocks (except nested ones)
- docinfo
- meta


Additional features
===================

Image galleries
---------------
Images and figures with class names that begin with
``gallery-`` form a gallery::

   .. image:: cat.jpg
       :class: gallery-1
   .. image:: dog.jpg
       :class: gallery-1
   .. figure:: horse.jpg
       :class: gallery-2
       :scale: 50%

This creates two galleries: One with cat and dog, the other one with
the horse picture only.
All attributes are ignored on gallery images.

Gallery-classed images are converted to ``{gallery:include=a.jpg,b.jpg}``
Confluence markup.

=====
Usage
=====
::

    rst2confluence /path/to/file.rst

Alternativelly, you may use rst2confluence.confluence.Writer as any docutils
writer.


============
Installation
============
::

    sudo python setup.py install



=====
Tests
=====
We have some examples how ``rst2confluence`` should behave.

Check if it does what it should::

    python setup.py test

Or run a single test::

    ./run-tests.sh tests/rst/bullet_list.rst

   

===========
Other tools
===========
Use deploy-rst__ to automatically deploy rST documents into confluence.


__ https://github.com/netresearch/deploy-rst
