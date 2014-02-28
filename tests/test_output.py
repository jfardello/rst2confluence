'''
Generate OutputTest methods with every src/*.rst file.
'''
import glob
import sys
import os 
import codecs

from docutils.core import publish_string
if sys.version_info <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from rst2confluence.confluence import Writer

here = os.path.abspath(os.path.dirname(__file__))


def add_test_output(cls, fname):
    def test_output(self):
        exp = self.load(fname + ".exp")
        out = self.parse(fname)
        self.assertEqual(exp, out)
    test_output.__name__ = "test_output_%s" % fname
    setattr(cls, test_output.__name__, test_output)

class OutputTest(unittest.TestCase):

    def load(self, fname):
        if fname.endswith("exp"):
            fname = os.path.join(here, "exp/%s" % fname)
        elif fname.endswith("rst"):
            fname = os.path.join(here, "rst/%s" % fname)
        with codecs.open(fname, encoding='utf-8', mode='r') as fd:
            out = fd.read()
        return out

    def parse(self, fname):
        writer = Writer()
        opts = {'output_encoding': 'unicode', 'input_encoding': 'unicode'}
        return publish_string(source=self.load(fname), writer=writer,
                settings_overrides=opts)

for _file in glob.glob("%s/rst/*.rst" % here):
    _file = os.path.basename(_file)
    add_test_output(OutputTest, _file)
