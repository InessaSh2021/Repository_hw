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
    n = int(input('Введите intelligence Hulk ', ))
    resultdata['Hulk'] = n
  
    
    response = requests.get('https://superheroapi.com/api/2619421814940190//search/Thanos')
    print(response.json())
    n1 = int(input('Введите intelligence Thanos ', ))
    resultdata['Thanos'] = n1
    
    
    response = requests.get('https://superheroapi.com/api/2619421814940190//search/Captain')
    print(response.json()) 
    n2 = int(input('Введите intelligence Captain_America ', ))
    resultdata['Captain_America'] = n2 

    resultdata_list = list(resultdata.values())     
    maximum_intelligence = max(resultdata_list)
    
    
    for key, values in resultdata.items():
      if values == maximum_intelligence:
        print('Самый умный герой', key)
             
    print('intelligence', maximum_intelligence)
    break
  
getdata(herolist)
