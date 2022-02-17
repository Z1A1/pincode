from ntpath import join
import requests
import json
from urllib.parse import urljoin
from rasa_sdk import Action


def Pin( mess,input):
    
    ur='https://api.postalpincode.in//pincode/' + mess
    
    response = requests.get(ur)
    pin=response.text
    parsed = json.loads(pin)
    json.dumps(parsed, indent=4)

    date = parsed[0]
    
    j=date['PostOffice']
    if input == 'State':
        Pin.k=j[0]['State']
        
    elif input=='District':
        Pin.k=j[0]['District'] 
    elif input =='City':
        Pin.k=j[0]['Block']       

    

    return 
