import unittest
import autocorrect
import stringdist as sd

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_complete(self):
        self.assertEqual("and", autocorrect.complete('a'))
    def test_lev(self):
        self.assertEqual(sd.rdlevenshtein('abcd!', 'abcde'), 1)

    def test_correct(self):
        cl=autocorrect.get_closest_k_words('a',2)
        self.assertEqual(cl[0][0],'as')
if __name__ == '__main__':
    unittest.main()