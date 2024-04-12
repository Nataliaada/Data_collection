import json
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from pprint import pprint

client_id = "__"
client_secret = "__"

endpoint = " https://api.foursquare.com/v3/places/search"

city = input("Введите город: ")
place = input("Введите  интересующую вас категорию (например, кофейни, музеи, парки и т.д.).: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": place
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

if response.status_code == 200:
      
    data = json.loads(response.text)
    venues = data['results']
    
    some_list = []
    for ven in venues:
       
        name = ven['name']
        address = ven.get('location', {}).get('address', 'адрес не указан')
        phone = ven.get('phone', {}).get('phone','Телефон не указана')
        some_list.append({'название': name, 'адрес': address, 'Телефон': phone})
     
    df = pd.DataFrame(some_list)
else:
    print(response.status_code)

print(df.head(5))



