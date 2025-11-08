# converters/currency.py
import requests

url = "https://api.frankfurter.dev/v1/latest"
resp = requests.get(url, params={"base":"USD"})
data = resp.json()
USD_BASE = data["rates"]
USD_BASE["USD"] = 1.0
#print(USD_BASE)

def convert_currency(amount: float, from_ccy: str, to_ccy: str) -> float:
    r = USD_BASE
    if from_ccy not in r or to_ccy not in r:
        raise ValueError("Currency not supported")
    usd = amount / r[from_ccy]
    return usd * r[to_ccy]
