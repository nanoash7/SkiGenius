"""
Use this module to query db from front end

Example:
from query_unit import query
query(user_ip)
Make sure that the .env file is present and contains the URI
"""

import os
import logging
from dotenv import load_dotenv, find_dotenv

# pylint: disable=import-error
from processor.query_generator import create_pipeline, query_neighbors
from database.create import connect_to_db

logging.basicConfig(filename="execution.log", encoding="utf-8", level=logging.DEBUG)
load_dotenv(find_dotenv())
URI = os.getenv("MONGO_URI")
client = connect_to_db(URI)
db = client["ski_info"]
collection = db["resorts"]


def query(user_pref_vector, max_price, num_results):
    """
    Function to query db with user inputs from front-end

    Inputs:
    list user_pref_vector: vector containing user preferences

    Outputs:
    list results : list of dictionaries containing top num_results neighbors.
                   First 3 entries are static and following entries are sorted
                   by descending snow amount.
    """
    pipeline = create_pipeline(user_pref_vector, num_results)
    results = query_neighbors(collection, pipeline)
    try:
        next(results)
    except StopIteration as e:
        raise ValueError("No results obtained") from e
    n_results = list(results)
    price_filtered_results = []

    for obj in n_results:
        if float(obj["Price"]) <= max_price:
            price_filtered_results.append(obj)

    def snow_compare(obj):
        return float(obj["Snow"])

    snow_sorted_results = price_filtered_results[0:3] + sorted(
        price_filtered_results[3:], key=snow_compare, reverse=True
    )

    return snow_sorted_results
