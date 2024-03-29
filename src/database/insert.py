"""
This module contains a function that inserts vectorized records
into the mongodb database.
"""

# pylint: disable=import-error
from processor import vectorizer


def insert_records(collection,file, columns):
    """
    Function to write vectorized inputs from CSV to MongoDB

    Inputs: 
    mongodb collection object : collection to insert records into
    file: path to the csv that contains the data to write
    columns: columns of the dataset that needs to be written to the db
    """
    vectors,info = vectorizer.vectorize_csv(file,columns)
    doc = {}

    for detail,vector in list(zip(info,vectors)):
        doc["Name"] = detail["Resort"]
        doc["State"] = detail["state_full"]
        doc["Price"] = detail["Price"]
        doc["Snow"] = detail["Total snow"]
        doc["vector"] = vector
        collection.insert_one(doc.copy())
