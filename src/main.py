from load_data import load_data
from fetch_data import get_data
from transform_data import transform_data
import logging 


# Configure logging
logging.basicConfig(filename='coincap_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    main function
    fetches data from CoinCap API, transforms it, and loads it to PostgreSQL
    """
    data = get_data()
    df = transform_data(data)
    result = load_data(df) 
    print(result)