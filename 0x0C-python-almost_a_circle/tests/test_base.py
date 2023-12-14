# test_base.py
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        # Test if __init__ assigns the correct id when provided
        base_obj = Base(5)
        self.assertEqual(base_obj.id, 5)

    def test_init_without_id(self):
        # Test if __init__ assigns a unique id when not provided
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertEqual(base_obj1.id, 1)
        self.assertEqual(base_obj2.id, 2)

    def test_to_json_string(self):
        # Test if to_json_string returns a valid JSON string
        base_obj = Base(1)
        json_string = base_obj.to_json_string([{'id': 1, 'key': 'value'}])
        self.assertEqual(json_string, '[{"id": 1, "key": "value"}]')

    def test_from_json_string(self):
        # Test if from_json_string returns a valid list
        base_obj = Base(1)
        json_string = base_obj.to_json_string([{'id': 1, 'key': 'value'}])
        json_list = base_obj.from_json_string(json_string)
        self.assertEqual(json_list, [{'id': 1, 'key': 'value'}])


if __name__ == '__main__':
    unittest.main()
