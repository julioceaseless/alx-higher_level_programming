# test_square.py
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_initialization(self):
        # Test if the initialization is correct
        sqr = Square(3)
        self.assertEqual(sqr.width, 3)
        self.assertEqual(sqr.height, 3)

    def test_area(self):
        # Test the area calculation
        size = [2, 3, 4]
        area = [4, 9, 16]
        for i in range(len(size)):
            sqr = Square(size[i])
            self.assertEqual(sqr.area(), area[i])

    def test_x_value(self):
        # Test the value of x
        sqr = Square(3, 12)
        self.assertEqual(sqr.x, 12)

    def test_y_value(self):
        # Test the value of y
        sqr = Square(3, 1, 12)
        self.assertEqual(sqr.y, 12)

    """ Test value types """
    def test_str_size_value(self):
        # Test if the class handles string size values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square("10")
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_str_x_value(self):
        # Test if the class handles string x values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square(1, 2, "10")
        msg = "y must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_str_y_value(self):
        # Test if the class handles string y values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square(2, 4, "10")
        msg = "y must be an integer"
        self.assertEqual(str(err.exception), msg)

    """ Test float values """
    def test_float_value(self):
        # Test if the class handles float values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square(3.14)
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_float_x_value(self):
        # Test if the class handles float  x values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square(3, 1.1, 1)
        msg = "x must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_float_y_value(self):
        # Test if the class handles float y values correctly
        with self.assertRaises(TypeError) as err:
            sqr = Square(3, 1, 2.1)
        msg = "y must be an integer"
        self.assertEqual(str(err.exception), msg)

    """ Test negative values """
    def test_negative_size_value(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(-4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_x_value(self):
        # Test if the class handles negative x values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(3, -2, 1)
        msg = "x must be >= 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_y_value(self):
        # Test if the class handles negative y values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(3, 2, -1)
        msg = "y must be >= 0"
        self.assertEqual(str(err.exception), msg)

    """ Test zero size values """
    def test_zero(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            sqr = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)


if __name__ == '__main__':
    unittest.main()
