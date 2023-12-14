# test_square.py
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        # Test the area calculation
        sqr = Square(3)
        self.assertEqual(sqr.area(), 9)

    def test_initialization(self):
        # Test if the initialization is correct
        sqr = Square(3)
        self.assertEqual(sqr.width, 3)
        self.assertEqual(sqr.height, 3)

    def test_negative_values(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(-3)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_values(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(-4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_zero(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            square = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)


if __name__ == '__main__':
    unittest.main()
