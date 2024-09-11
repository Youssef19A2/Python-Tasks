#Get your public IP
import requests
from pprintpp import pprint
url = requests.get("https://api.ipify.org/?format=json")
pprint(url.text)