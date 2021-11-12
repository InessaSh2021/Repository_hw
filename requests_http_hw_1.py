import requests
url = "https://superheroapi.com/api/2619421814940190/search/name"
params = {"name" : "Thanos, Hulk, Captain America"}
response = requests.get(url = url, params = params)
print(response.json())