import unittest
import autocomplete
import json
import sys
import stringdist as sd

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_complete(self):
        self.assertItemsEqual("add", self.autocorrect.complete('a'))
    ##to do:autocorrect

if __name__ == '__main__':
    unittest.main()
