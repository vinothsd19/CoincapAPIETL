import pandas as pd
import logging
from fetch_data import get_data


def transform_data(data):
    """transforms data from CoinCap API

    Args:
        data (json api data): data from CoinCap API in json format

    Returns:
        DataFrame: data frame of transformed data
    """

    try:
        df = pd.DataFrame(data)
        cols = ['supply', 'rank', 'maxSupply', 'marketCapUsd', 'volumeUsd24Hr', 'priceUsd', 'changePercent24Hr', 'vwap24Hr']
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
        df = df.drop(['explorer'], axis=1)
        logging.info("Data transformed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return None
    
