#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map
function and understand its purpose. Play with it in the
Python console to make sure you understand.
In this task you will write the first unit test for
utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from
unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test the function
for following inputs:

    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")

For each of these inputs, test with assertEqual that the function
returns the expected result.

The body of the test method should not be longer than 2 lines.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Args:
            unittest(__type__): _description_
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",)),
            ({"a": {"b": 2}}, ("a",)),
            ({"a": {"b": 2}}, ("a", "b"))
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_results):
        """tests
        """
        results = access_nested_map(nested_map, path)
        self.assertEqual(results, expected_results)
