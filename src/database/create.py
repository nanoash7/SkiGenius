import logging
from pymongo import MongoClient


logging.basicConfig(filename='execution.log', encoding='utf-8', level=logging.DEBUG)


def connect_to_db(uri):
    """
    Function to connect to the mongodb client
    Inputs: 
    string uri: uri of the database
    Outputs:
    MongoClient client: client object
    Exceptions: 
    In case the connection to the database fails, the error is written to the logs
    """

    client = MongoClient(uri)

    # Try to connect with the database 
    try:
        client.admin.command('ping')
        logging.info("Connection to db successful")
    except Exception as e:
        logging.error(str(e))
    
    return client

def create_db(db_name, client):
    """
    Function to create a database on the instance
    Inputs:
    str db_name: name of the database
    MongoClient client: mongodb client object 
    Output:
    Mongodb db object
    """
    db = client[db_name]
    return db

def create_collection(db, collection_name):
    """
    Function create a collection in the database
    Inputs: 
    Mongodb db object db to which the collection needs to be added
    str collection_nmae: name of the collection that needs to be created
    Outputs:
    Mongodb collection objected created on the passed db.
    """
    collection = db[collection_name]
    return collection

    


