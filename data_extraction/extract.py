import requests
import time
import os
from dotenv import load_dotenv
from db_connection.db import DbConnectorDataSet

#variables d'environnements
load_dotenv()

cle_api = os.getenv('CLE_API_INSEE')

url = " https://api.insee.fr/api-sirene/3.11/siren"
headers = {
        "X-INSEE-Api-Key-Integration": cle_api
}
params = {
    "q": "",  # Vide = pas de filtre → tout (actifs + fermés)
    "nombre": 1,  # max : 1000
    "debut": 0     # pagination
}
response = requests.get(url, headers=headers, params=params)
response.raise_for_status()

results = response.json()
for i in results:
    print(i)
for i in results['unitesLegales']:
    print(i)
# init de la connexion db
db = DbConnectorDataSet()

