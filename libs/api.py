import requests
from cachetools import cached, TTLCache


class OpenExchangeClient:
    URL = "https://openexchangerates.org/api"

    def __init__(self, api_id):
        self.api_id = api_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.URL}/latest.json?app_id={self.api_id}").json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[to_currency]
            return from_in_usd * to_rate
