import requests

# API URL
url = "http://api.marketstack.com/v2/intraday"

# Parameters
params = {
    "access_key": "b144084f657b2e0e6ec6bbad1015b52d",  # Replace with your API key
    "symbols": "AAPL",  # Apple stock symbol
    "interval": "1m",  # 1-minute data
    "date_from": "2023-12-27",  # Start date
    "date_to": "2024-12-27",  # End date
    "limit": 10000  # Number of data points to fetch (can be increased)
}

# Make the request
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
