from pprint import pprint
import requests

url = "https://stackoverflow.com/"
params = {"period" : "2_days", "tag": "python"}
response = requests.get(url = url, params = params)

pprint(response.content)