import requests
import logging

# Configure logging
logging.basicConfig(filename='coincap_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_data():
    """gets data from CoinCap API

    Returns:
        json: data from CoinCap API

    """
    coincap_api_url = 'https://api.coincap.io/v2/assets'
    try:
        response = requests.get(coincap_api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()['data']
        logging.info("Data fetched successfully from CoinCap API.")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data from CoinCap API: {e}")
        return None
