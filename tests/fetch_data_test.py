import requests
# Define the API endpoint URL
url = 'https://api.coincap.io/v2/assets'
# Make a GET request to the API endpoint
response = requests.get(url)
# Check the response status code
if response.status_code == 200:
    # Print the response content
    print("data fetched successfully")
else:
    # Handle the error
    print('Error: {0}'.format(response.status_code)) 
      