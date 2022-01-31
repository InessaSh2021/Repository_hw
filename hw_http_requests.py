import requests

herolist = ['Hulk', 'Captain', 'America', 'Thanos']

def getdata(herolist):
  resultdata = {}
  for hero in herolist:
    response = requests.get('https://superheroapi.com/api/2619421814940190//search/Hulk')
    if response.status_code == 200:
      print('Success!')
    elif response.status_code == 404:
      print('Not Found.')
    print(response.json())
    resultdata['Hulk'] = 88
    
    response = requests.get('https://superheroapi.com/api/2619421814940190//search/Thanos')
    print(response.json())
    resultdata['Thanos'] = 100
    
    response = requests.get('https://superheroapi.com/api/2619421814940190//search/Captain')
    print(response.json()) 
    resultdata['Captain_America'] = 69 

    resultdata_list = list(resultdata.values())
      
    maximum_intelligence = max(resultdata_list)
    
    for key, values in resultdata.items():
      if values == maximum_intelligence:
        print('Самый умный герой', key)
    
  print('intelligence', maximum_intelligence)

getdata(herolist)