from dotenv import load_dotenv
import mysql.connector as sql
import os

class DbConnectorDataSet:
    def __init__(self):
        load_dotenv()
        self.conn = sql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
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

        
    def insert_new_values(self, raison_social,nb_etablissement_open, activite, categorie,date_creation, date_fermeture, etat_admin, nature_juridique, activite_principale, effectif, departement):
        """
        Méthode pour insérer les données suivantes : 
            raison_social,
            nb_etablissement_open,
            activite,
            categorie,
            date_creation,
            date_fermeture,
            etat_admin,
            nature_juridique,
            activite_principale,
            effectif,
            departement
        """
        
        requete_SQL = """INSERT INTO raw_data (nom_raison_sociale,
                nombre_etablissements_ouverts,
                activite_principale,
                categorie_entreprise,
                date_creation,
                date_fermeture,
                etat_administratif,
                nature_juridique,
                section_activite_principale,
                tranche_effectif_salarie,
                departement)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (raison_social,nb_etablissement_open, activite, categorie,date_creation, date_fermeture, etat_admin, nature_juridique, activite_principale, effectif, departement)
        self.cur.execute(requete_SQL, values)
        self.conn.commit()
        return True
        

