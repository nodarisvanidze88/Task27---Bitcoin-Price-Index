import requests
import json
import sys

try:
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    user = float(sys.argv[1])
    rate = data["bpi"]["USD"]["rate_float"]*user
    print(f"{rate:,.2f}")
except (IndexError, ValueError):
    sys.exit("Incorrect sys argument")
