"""
This module conatins methods to vectorize data
This module should also handle the encoding of columns into a numeric format
before vectorization is performed.
vectorize_csv converts a given subset of a dataframe to a list of vectors
"""

import logging
import pandas as pd

logging.basicConfig(filename="execution.log", encoding="utf-8", level=logging.DEBUG)


def vectorize_csv(file, columns):
    """
    Function to construct vectors from input CSV
    Read CSV file row by row and vectorize it row by row
    Inputs:
      str file - path to the csv file
      list columns - list of columns to be vectorized
    Outputs:
    list vectors: list of vectors (lists) to write to db
    list info: list of dicts containing other info - Name of resort, price and state
    """

    try:
        df = pd.read_csv(file)
        df_subset = df[columns]
        categorical_cols = df_subset.select_dtypes(["category", "object"]).columns
    except KeyError:
        logging.error("Given columns not found in the dataframe")
        return [], []

    df_encoded = pd.get_dummies(df_subset, columns=categorical_cols)

    try:
        info = df[["Resort", "state_full", "Price", "Total snow"]].to_dict("records")
        vectors = df_encoded.values.tolist()
    except KeyError:
        logging.error("Expected columns for name, state, price and snow not found.")
        return [], []

    return vectors, info
