import requests
import time
import os
from dotenv import load_dotenv
# from db_connection.db import DbConnectorDataSet

#variables d'environnements
load_dotenv()

request_token = requests.post('https://registre-national-entreprises.inpi.fr/api/sso/login',json={
    "username": os.getenv('ID_INPI'),
    "password": os.getenv('MDP_INPI') 
})

token = request_token.json()['token']
url = "https://registre-national-entreprises.inpi.fr/api/companies?submitDateTo=2021-08-15&submitDateFrom=2021-08-01"

print(token)
data = requests.get(url=url, headers={
    "Authorization" : f"Bearer {token}"
})
response = data.json()


# print(response)


