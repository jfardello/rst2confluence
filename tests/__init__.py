import sys
if sys.version_info <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from .test_output import OutputTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(OutputTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

