# test_rectangle.py
import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test the area calculation
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_initialization(self):
        # Test if the initialization is correct
        rect = Rectangle(3, 4)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)

    """ Test negative values """
    def test_negative_width_value(self):
        # Test if the class handles negative width values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(-3, 4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_height_value(self):
        # Test if the class handles negative height values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(3, -4)
        msg = "height must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_x_value(self):
        # Test if the class handles negative x value correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(3, 4, -4)
        msg = "x must be >= 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_y_value(self):
        # Test if the class handles negative y value correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(3, 4, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(err.exception), msg)

    """ Test string values """
    def test_str_width_value(self):
        # Test if the class handles non-integer values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle("three", 10)
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_str_height_value(self):
        # Test if the class handles non-integer values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, "10")
        msg = "height must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_str_x_value(self):
        # Test if the class handles string x values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, 10, "one")
        msg = "x must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_str_y_value(self):
        # Test if the class handles string y values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, 10, 1, "one")
        msg = "y must be an integer"
        self.assertEqual(str(err.exception), msg)

    """ Test float values"""
    def test_float_x_value(self):
        # Test if the class handles float  x values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, 10, 1.1, 1)
        msg = "x must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_float_y_value(self):
        # Test if the class handles float y values correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, 10, 1, 2.1)
        msg = "y must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_float_height_value(self):
        # Test if the class handles float height value correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3, 5.5)
        msg = "height must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_float_width_value(self):
        # Test if the class handles float width value correctly
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(3.5, 10)
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    """ test zero values """
    def test_zero_width(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(0, 4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_zero_height(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(4, 0)
        msg = "height must be > 0"
        self.assertEqual(str(err.exception), msg)


if __name__ == '__main__':
    unittest.main()
