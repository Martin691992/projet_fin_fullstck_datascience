from dotenv import load_dotenv
import mysql.connector as sql
import os

class DbConnectorDataSet:
    def __init__(self):
        load_dotenv()
        conn = sql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cur = conn.cursor()
        cur.execute("""
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


    def insert_new_values(self, features):
        print("hello")

