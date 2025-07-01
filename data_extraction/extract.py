import requests
import time
import os
from dotenv import load_dotenv
from db_connection.db import DbConnectorDataSet

#variables d'environnements
load_dotenv()

cle_api = os.getenv('CLE_API_INSEE')


max_entreprise = 1
page_size = 1
entreprise = []

# itération sur les différentes pages 
for start in range(0, max_entreprise, page_size):
    url = " https://api.insee.fr/entreprises/sirene/V3/siren"
    headers = {
        "X-INSEE-Api-Key-Integration": cle_api
    }
    params = {
    "q": "",  # Vide = pas de filtre → tout (actifs + fermés)
    "nombre": page_size,  # max : 1000
    "debut": start     # pagination
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()
    entreprise.extend(results.get("unitesLegales", []))
    if len(results.get("unitesLegales", [])) < page_size:
        break

for i in entreprise :
   for y in i:
       print(f"{i} : {i[y]}")
       print("\n")
       print("\n")
# print(len(entreprise))
# init de la connexion db
db = DbConnectorDataSet()

