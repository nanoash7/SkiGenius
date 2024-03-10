"""
Module that contains the tests for the test query unit
"""

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from query_unit import query


class TestQuery(unittest.TestCase):
    """
    This class contains the test functions for the query unit that
    is responsible for interacting with the processor and passing the results to the frontend
    """

    @patch("query_unit.query_neighbors")
    def test_query_no_results(self, mock_query_neighbors):
        """
        Test that ValueError is raised when no results are returned
        """

        user_pref_vector = [0] * 15
        max_price = 0
        num_results = 1
        mock_query_neighbors.return_value = iter([])

        with self.assertRaises(ValueError) as context:
            query(user_pref_vector, max_price, num_results)

        self.assertEqual(str(context.exception), "No results obtained")
