import time

from libs.api import OpenExchangeClient

API_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = OpenExchangeClient(API_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)
print(f'{usd_amount} is equal to {gbp_amount:.2f}')
