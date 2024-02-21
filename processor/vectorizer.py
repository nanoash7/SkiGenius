import pandas as pd

"""
This module conatins methods to vectorize data
This module should also handle the encoding of columns into a numeric format
before vectorization is performed.
vectorize_csv converts a given subset of a dataframe to a list of vectors
"""



def vectorize_csv(file,columns):
    """
    Function to construct vectors from input CSV
    Read CSV file row by row and vectorize it row by row
    Inputs:
      str file - path to the csv file
      list columns - list of columns to be vectorized
    Outputs: 
    list vectors: list of vectors (lists) to write to db
    """
    df = pd.read_csv(file)
    df_subset = df[columns]
    categorical_cols = df_subset.select_dtypes(['category','object']).columns
    df_encoded = pd.get_dummies(df_subset, columns = categorical_cols)
    resort_names = df["Resort"]
    vectors = df_encoded.values.tolist()
    return vectors, resort_names

