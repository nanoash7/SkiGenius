"""
Module that contains the test cases for the processor.vectorizer module
It contains the test case for the vectorize_csv function
"""

import unittest
from unittest.mock import patch
import pandas as pd

# pylint: disable=import-error
from processor.vectorizer import vectorize_csv


class TestVectorizeCSV(unittest.TestCase):
    """
    This class contains the test cases for the vectorizer that is used to convert
    the values in the source csv to an appropriate format for insertion into Mongodb
    """

    @patch("processor.vectorizer.pd.read_csv")
    def test_vectorize_csv_basic(self, mock_read_csv):
        """
        Smoke test case to ensure that the vectorize_csv function behaves as expected
        """
        mock_df = pd.DataFrame(
            {
                "Resort": ["a", "b"],
                "state_full": ["c", "d"],
                "Price": [1, 2],
                "Total snow": [1, 2],
                "A": [30, 40],
                "B": [60, 70],
            }
        )
        mock_read_csv.return_value = mock_df

        vectors, info = vectorize_csv("test.csv", ["A", "B"])

        expected_vectors = [[30, 60], [40, 70]]
        expected_info = [
            {"Resort": "a", "state_full": "c", "Price": 1, "Total snow": 1},
            {"Resort": "b", "state_full": "d", "Price": 2, "Total snow": 2},
        ]

        self.assertEqual(vectors, expected_vectors)
        self.assertEqual(info, expected_info)

    @patch("processor.vectorizer.pd.read_csv")
    @patch("logging.error")
    def test_vectorize_csv_missing_columns(self, mock_log_error, mock_read_csv):
        """
        Test case to ensure that an appropriate error is logged when
        columns that are not in the dataset are passed as an argument
        """
        mock_df = pd.DataFrame({"X": [1, 2]})
        mock_read_csv.return_value = mock_df
        vectorize_csv("test.csv", ["MissingColumn"])
        mock_log_error.assert_called_with("Given columns not found in the dataframe")

    @patch("processor.vectorizer.pd.read_csv")
    @patch("logging.error")
    def test_vectorize_csv_missing_info_columns(self, mock_log_error, mock_read_csv):
        """
        Test case to ensure that an appropriate error is logged when
        columns that are required to be in the dataset are not present
        """
        mock_df = pd.DataFrame({"A": ["a", "b"]})
        mock_read_csv.return_value = mock_df
        vectorize_csv("test.csv", ["A"])
        mock_log_error.assert_called_with(
            "Expected columns for name, state, price and snow not found."
        )
