import httpx
from os import environ
import csv

TOKEN = environ['XIGNITE_TOKEN']

client = httpx.Client(
    http1=True
)
response = client.get(
    url="https://bonds.xignite.com/xBonds.json/ListBonds?PriceSource=FINRA&BondType=Bond&StartSymbol=A&EndSymbol=B",
    params=dict(_token=TOKEN)).json()

with open('bonds.csv', 'w') as file:
    w = csv.DictWriter(file, response.keys())
    w.writeheader()
    w.writerow(response)


