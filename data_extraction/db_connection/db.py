from dotenv import load_dotenv

import os

class DbConnectorDataSet:
    def __init__(self):
        load_dotenv()
        conn = sql.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        conn.execute("""
        CREATE TABLE IF NOT EXISTS raw_data (id SERIAL PRIMARY KEY,
                                            nom_raison_sociale TEXT,
                                            nombre_etablissements_ouverts INTEGER,
                                            activite_principale TEXT,
                                            categorie_entreprise TEXT,
                                            date_creation TEXT ,
                                            date_fermeture TEXT,
                                            etat_administratif TEXT,
                                            nature_juridique TEXT,
                                            section_activite_principale TEXT,
                                            tranche_effectif_salarie TEXT,
                                            departement VARCHAR(3))""")
        conn.commit()


    def insert_new_values(self, features):
        print("hello")

