#Write code to find automatically bitcoin rate
import requests
from pprintpp import pprint
url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
pprint(url.json())