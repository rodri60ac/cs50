import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif not sys.argv[1].isnumeric():
    sys.exit("Command-line argument is not a number")


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Loading Error")

response = r.json()
bitcoin = response['bpi']['USD']['rate_float']
total_usd = float(sys.argv[1]) * bitcoin
print(f"${total_usd:,.4f}")


