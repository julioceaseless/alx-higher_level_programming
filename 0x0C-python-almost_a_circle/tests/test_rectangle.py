# test_rectangle.py
import unittest
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

    def test_negative_values(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(-3, 4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_negative_values(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(3, -4)
        msg = "height must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_zero(self):
        # Test if the class handles negative values correctly
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(0, 4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)


if __name__ == '__main__':
    unittest.main()
