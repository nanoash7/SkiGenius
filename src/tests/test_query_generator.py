"""
This module contains the test cases for the functions within the
 query_generator module. It contains test cases for the following:

 create_pipeline: function that creats the pipeline
 query_neighbors: queries mongodb for top n neighbors
"""

import unittest
import os

# pylint: disable=import-error
from database.create import connect_to_db
from processor.query_generator import create_pipeline, query_neighbors


class TestQueryGenerator(unittest.TestCase):
    """
    Class to test query generator that creates pipelines and performs the aggregation query
    """

    def test_create_pipeline_consistency(self):
        """
        Test case to check if the pipeline created is consistent with inputs
        """
        query = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # query size 15
        topn = 3
        pipeline = create_pipeline(query, topn)
        expected_pipeline = [
            {"$search": {"knnBeta": {"vector": query, "path": "vector", "k": topn}}},
            {"$limit": topn},
            {
                "$project": {
                    "Name": 1,
                    "Price": 1,
                    "State": 1,
                    "Snow": 1,
                    "score": {"$meta": "searchScore"},
                }
            },
        ]
        self.assertEqual(pipeline, expected_pipeline)

    def test_empty_query(self):
        """
        Test case to ensure exception is thrown when an empty query is passed
        """
        query = []
        topn = 3
        with self.assertRaises(ValueError):
            create_pipeline(query, topn)

    def test_query_length(self):
        """
        Test case to ensure exception is thrown when query length is too short
        """
        query = [1, 2, 3]
        topn = 3
        with self.assertRaises(ValueError):
            create_pipeline(query, topn)

    def test_zero_top_n(self):
        """
        Test case to ensure that the value of number of neighbors is positive
        """
        query = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # query size 15
        topn = 0
        with self.assertRaises(ValueError):
            create_pipeline(query, topn)

    def test_query(self):
        """
        Smoke test to ensure the query function executes as expected
        """
        query = [
            -1.6528925619834711,
            111.19777183999996,
            131.1634609908,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
        ]
        topn = 1
        uri = os.getenv("MONGO_URI")
        client = connect_to_db(uri)
        db = client["ski_info"]
        collection = db["resorts"]
        pipeline = create_pipeline(query, topn)
        results = query_neighbors(collection, pipeline)
        self.assertIsNotNone(results)
