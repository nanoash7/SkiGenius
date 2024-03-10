"""
Module containing the test cases for the database module
They test the functions for connecting to the db,
creating a new db instance and a new collection instance.

contains the test cases for
- create.py - connect_to_db , create_db, create_collection fucntions
- insert.py - insert_records fucntion
"""

import os
import unittest
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

# import mongomock

# pylint: disable=import-error
from database.create import connect_to_db, create_collection, create_db


load_dotenv()
URI = os.getenv("MONGO_URI")


class TestDatabase(unittest.TestCase):
    """
    Class to contain the test cases for the database operations
    """

    def test_connect_to_db(self):
        """
        Test case to test the successful connection to the DB
        """
        client = connect_to_db(URI)
        # Assert connection was successful
        self.assertIsInstance(client, MongoClient)
        self.assertTrue(client.admin.command("ping"))

    def test_create_db(self):
        """
        Test case to test if the db is created successfully
        """
        client = connect_to_db(URI)
        db = create_db("ski_info", client)
        self.assertIsNotNone(db)
        self.assertIsInstance(db, Database)

    def test_create_collection(self):
        """
        Test case to test if collection is created successfully within the sepcified db
        """
        client = connect_to_db(URI)
        db = create_db("ski_info", client)
        collection = create_collection(db, "resorts")
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)
