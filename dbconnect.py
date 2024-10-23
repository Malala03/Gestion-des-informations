import mysql.connector
from flet import *

def main(page):
    # Connexion à la base de données
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # remplacez par votre nom d'utilisateur MySQL
        password="",  # remplacez par votre mot de passe MySQL
        database="infos_db"
    )

    cursor = db.cursor()

    # Exemple d'insertion dans la table Demandeur
    def add_demandeur(nom, categorie, fonction, entite, admin_id):
        sql = "INSERT INTO Demandeur (nom, categorie, fonction, entite, admin_id) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, categorie, fonction, entite, admin_id)
        cursor.execute(sql, values)
        db.commit()

    # Ajout d'une interface utilisateur avec Flet
    def submit(e):
        nom = nom_input.value
        categorie = categorie_input.value
        fonction = fonction_input.value
        entite = entite_input.value
        admin_id = admin_id_input.value
        add_demandeur(nom, categorie, fonction, entite, admin_id)
        page.add(Text(f"Demandeur {nom} ajouté avec succès!"))

    # Champs d'entrée
    nom_input = TextField(label="Nom")
    categorie_input = TextField(label="Catégorie")
    fonction_input = TextField(label="Fonction")
    entite_input = TextField(label="Entité")
    admin_id_input = TextField(label="ID Administrateur")

    page.add(nom_input, categorie_input, fonction_input, entite_input, admin_id_input, ElevatedButton("Ajouter Demandeur", on_click=submit))

if __name__ == "__main__":
    app(target=main)
