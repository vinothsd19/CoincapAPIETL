import pandas as pd
from sqlalchemy import create_engine
import logging
from fetch_data import get_data
from transform_data import transform_data

# Configure logging
logging.basicConfig(filename='coincap_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

data = get_data()
df = transform_data(data)

def load_data(df):
    """loads data to PostgreSQL

    Args:
        df (json data): data from CoinCap API and transformed to a pandas dataframe

    Returns:
        DataFrame: CoinCap data in a pandas dataframe
    """
    try:
        engine = create_engine("postgresql://postgres:1221@localhost:5433/postgres")
        df.to_sql('coincap_assets', con=engine, if_exists='replace', index=False)
        logging.info("Data loaded successfully to PostgreSQL.")
        return "Data loaded successfully to PostgreSQL."
    except Exception as e:
        logging.error(f"Error loading data to PostgreSQL: {e}")
        return f"Error loading data to PostgreSQL: {e}"

result = load_data(df)
print(result)
