import requests
import json

# Etherscan API details
api_key = "5QWEKQCCI9VPTBFP6TRZU4HIE7AGTKAYR1"
address = "0x0bAe6494d778C57E1991F8651aef06f786fA23DC"
url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey={api_key}"

# Fetch data
response = requests.get(url)
data = response.json()

# Save data to a file
with open("transactions.json", "w") as file:
    json.dump(data, file, indent=4)

print("Transactions saved to transactions.json")