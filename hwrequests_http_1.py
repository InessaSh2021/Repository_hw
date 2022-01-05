import requests

response1 = requests.get('https://superheroapi.com/api/2619421814940190//search/Captain America')

if response1.status_code == 200:
    print('Success!')
elif response1.status_code == 404:
    print('Not Found.')

print(response1.json()) # Captain America {'intelligence': '69'}

response2 = requests.get('https://superheroapi.com/api/2619421814940190//search/Hulk')

if response2.status_code == 200:
    print('Success!')
elif response2.status_code == 404:
    print('Not Found.')

print(response2.json())  # Hulk {'intelligence': '88'}


response3 = requests.get('https://superheroapi.com/api/2619421814940190//search/Thanos')

if response3.status_code == 200:
    print('Success!')
elif response3.status_code == 404:
    print('Not Found.')

print(response3.json()) # Thanos  {'intelligence': '100'}
