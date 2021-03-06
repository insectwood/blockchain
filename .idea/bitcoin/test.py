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

    def test_sub(self):
        a = FieldElement(4, 31)
        b = FieldElement(15, 31)
        self.assertEqual(a + b, FieldElement(19, 31))
        c = FieldElement(19, 31)
        d = FieldElement(15, 31)
        self.assertEqual(c + d, FieldElement(3, 31))

    def test_mul(self):
        a = FieldElement(24, 31)
        b = FieldElement(18, 31)
        self.assertEqual(a*b, FieldElement(29, 31))

    def test_pow(self):
        a = FieldElement(15, 31)
        self.assertEqual(a**3, FieldElement(27, 31))
        b = FieldElement(11, 31)
        c = FieldElement(27, 31)
        self.assertEqual(b**5 * c, FieldElement(7, 31))

    def test_div(self):
        a = FieldElement(5, 31)
        b = FieldElement(15, 31)
        self.assertEqual(a / b, FieldElement(21, 31))
        c = FieldElement(19, 31)
        self.assertEqual(c**-2, FieldElement(14, 31))

    def test_ne(self):
        a = FieldElement(4, 31)
        b = FieldElement(4, 31)
        c = FieldElement(15, 31)
        self.assertEqual(a, b)
        self.assertTrue(a != c)
        self.assertFalse(a != b)


if __name__ == '__main__':
    unittest.main()