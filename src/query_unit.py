import os
from dotenv import load_dotenv
from processor.query_generator import create_pipeline, query_neighbors
from database.create import connect_to_db

"""
Use this function to query db from front end
Example:
from query_unit import query
query(user_ip) 
Make sure that the .env file is present and contains the URI
"""

load_dotenv()
URI = os.getenv('MONGO_URI')
client = connect_to_db(URI)
db = client["ski_info"]
collection = db["resorts"]

def query(user_pref_vector):
    """
    Function to query db with user inputs from front-end

    Inputs:
    list user_pref_vector: vector containing user preferences

    Outputs:
    list results : list of dictionaries containing top 10 neighbors

    """
    pipeline = create_pipeline(user_pref_vector,10)
    results = query_neighbors(collection,pipeline)
    return results
