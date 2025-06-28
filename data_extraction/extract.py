import requests
import time
from db_connection.db import DbConnectorDataSet

# On utilise ici l'API du gouvernement français afin de récupérer les données sur les entreprises.
# La documentation est disponible via le lien ci-après : https://recherche-entreprises.api.gouv.fr
#  

# request = "https://recherche-entreprises.api.gouv.fr/search?page=1&per_page=25&est_association=false&est_collectivite_territoriale=false&est_service_public=false&est_l100_3=false"


# response = requests.get(request)
# results = response.json()
# print(results["total_results"])
# print(results["page"])
# print(results["per_page"])
# print(results["total_pages"])
db = DbConnectorDataSet()

