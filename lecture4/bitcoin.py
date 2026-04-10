import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=TA_CLE_API")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = price * n
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit("Request failed")