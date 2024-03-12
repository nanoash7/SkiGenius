"""
This module contains code to initialize the mongodb database
with the desired features.
"""

import os

from dotenv import load_dotenv

# pylint: disable=import-error
from database.create import connect_to_db
from database.create import create_db
from database.create import create_collection
from database.insert import insert_records

load_dotenv()

URI = os.environ["MONGO_URI"]
client = connect_to_db(URI)
db = create_db("ski_info", client)
collection = create_collection(db, "resorts")
columns = [
    "Difficulty",
    "Scaled_Latitude",
    "Scaled_Longitude",
    "Open January",
    "Open February",
    "Open March",
    "Open April",
    "Open May",
    "Open June",
    "Open July",
    "Open August",
    "Open September",
    "Open October",
    "Open November",
    "Open December",
]
insert_records(collection, "../data/df_merged_scaled_final.csv", columns)
