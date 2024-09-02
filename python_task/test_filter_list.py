"""Testing the `filter_list` function."""
import unittest
from python_task.filter_list import filter_list

class TestFilterList(unittest.TestCase):
    """
    Test case class for the `filter_list` function.

    This class contains unit tests for the `filter_list` function to verify its 
    correctness and handle edge cases. The tests include checking the output of 
    the function when given valid input and ensuring that the function raises 
    the appropriate exception when the input list is of invalid length.
    """

    def test_filter_list_valid(self):
        """
        Test filtering a valid list.

        This test checks whether the `filter_list` function correctly filters a list 
        of integers according to a specified condition (e.g., returning only prime 
        numbers). The test compares the function's output to the expected result.
        """
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = filter_list(input_list)
        expected_result = [1, 5, 7, 11, 13, 17, 19]
        self.assertEqual(result, expected_result)

    def test_filter_list_invalid_length(self):
        """
        Test filtering a list of invalid length.

        This test verifies that the `filter_list` function raises a `ValueError` 
        when the input list does not meet the required length condition (e.g., 
        the list must contain exactly 20 elements).
        """
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            filter_list(input_list)

    def test_filter_list_exact_multiple_of_10(self):
        """
        Test filtering a list with length exactly a multiple of 10.

        This test checks the function with a list length of exactly 10, 
        which should be valid and correctly filtered.
        """
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = filter_list(input_list)
        expected_result = [1, 5, 7]
        self.assertEqual(result, expected_result)

    def test_filter_list_multiple_of_10_larger(self):
        """
        Test filtering a larger list with length a multiple of 10.

        This test checks the function with a list length of 30, which 
        is a valid multiple of 10, to verify correct filtering.
        """
        input_list = list(range(1, 31))
        result = filter_list(input_list)
        expected_result = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]
        self.assertEqual(result, expected_result)

    def test_filter_list_empty(self):
        """
        Test filtering an empty list.

        This test verifies that the function handles an empty list without 
        raising an exception, which should be considered a valid case since 
        0 is a multiple of 10.
        """
        input_list = []
        result = filter_list(input_list)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_filter_list_large_numbers(self):
        """
        Test filtering a list with large numbers.

        This test checks the function with a list containing large integers
        to ensure it handles larger values correctly.
        """
        input_list = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008, 1000000009, 1000000010]
        result = filter_list(input_list)
        expected_result = [1000000001, 1000000005, 1000000007]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
