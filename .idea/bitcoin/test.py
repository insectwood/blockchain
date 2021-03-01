import unittest
from FieldElement import FieldElement

class FieldElementTest(unittest.TestCase):

    def test_add(self):
        a = FieldElement(2, 37)
        b = FieldElement(15, 37)
        self.assertEqual(a + b, FieldElement(17, 37))
        c = FieldElement(19, 37)
        d = FieldElement(21, 37)
        self.assertEqual(c + d, FieldElement(3, 37))

if __name__ == '__main__':
    unittest.main()