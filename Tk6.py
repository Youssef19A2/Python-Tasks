#Get your location
import requests
from pprintpp import pprint

url = requests.get("https://ipinfo.io/")
pprint(url.json())