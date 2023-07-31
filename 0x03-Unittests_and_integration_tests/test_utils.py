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
import requests
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Args:
            unittest(__type__): _description_
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",),{"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_results):
        """tests
        """
        results = access_nested_map(nested_map, path)
        self.assertEqual(results, expected_results)
    
    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected_results):
        """
        Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises
        context manager to test that a KeyError is raised for the following inputs
        (use @parameterized.expand):
            nested_map={}, path=("a",)
            nested_map={"a": 1}, path=("a", "b")
        Also make sure that the exception message is as expected.
        """
        with self.assertRaises(expected_results) as context:
            access_nested_map(nested_map, path)
    
class TestGetJson(unittest.TestCase):
    """
    parameterized
    """
    @parameterized.expand(
        [
           ("http://example.com", {"payload": True}),
           ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, expected_results):
        mock_url_response = Mock()
        mock_url_response.json.return_value = expected_results
        with patch('requests.get', return_value=mock_url_response):
            response = get_json(url)
            self.assertEqual(response, expected_results)


class TestMemoize(unittest.TestCase):
    """
    Read about memoization and familiarize yourself with the
    utils.memoize decorator. Implement the TestMemoize(unittest.TestCase)
    class with a test_memoize method.
    Inside test_memoize, define following class
    
        class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    Use unittest.mock.patch to mock a_method. Test that when calling a_property
    twice, the correct result is returned but a_method is only called once using
    assert_called_once.
    """
    def test_memoize(self):
        """
        Test_memoize class
        """
        def test_memoize(self):
            """
            test_memoize function
            """
            class TestClass:
                """
                    class TesClass
                """
                def a_method(self):
                    """
                        a method
                    """
                    return 42

                @memoize
                def a_property(self):
                    """
                    a_property
                    """
                    return self.a_method()

                test_object = TestClass()

                with patch.object(test_object, 'a_method') as mock_method:
                    mock_method.result_value = 42

                    result1 = test_object.a_property
                    result2 = test_object.a_property

                    self.assertEqual(result1, 42)
                    self.assertEqual(result2, 42)
                    mock_method.assert_called_once()
