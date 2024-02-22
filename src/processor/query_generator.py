
def create_pipeline(query,topn):
    """
    Function to the query vector and desired number of neighbors 
    to form query pipeline

    Inputs: 
    list query: list containing user preferences 
    int topn: number of neighbors to be returned

    Outputs:
    pipeline object: this object's aggregate method can be called 
    in order to obtain an iterator containing the results 
    """
    pipeline = [
    {
        "$search": {
            "knnBeta": {
                "vector": query,
                "path": "vector",
                "k": topn
            }
        }
    },
    {
        "$limit": topn
    },
    {
        "$project": {
            "Name": 1,
            "Price": 1,
            "State": 1,
            "Snow": 1,
            'score': {
                '$meta': 'searchScore'
            }
        }
    }
]
    return pipeline


def query_neighbors(collection,pipeline):
    """
    Function to query the db and aggregate results as configured in the pipeline
    
    Inputs: 
    mongodb object collection: collection object returned by mongodb
    pipeline: pipeline json consisting of the required information as returned by
    create_pipeline

    Outputs:
    list results: list of dicts consisting of the requested number of nearest neighbors
    """
    results = collection.aggregate(pipeline)
    return results
