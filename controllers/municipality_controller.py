from dbconnect import get_db_connection

class MunicipalityController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()  # Connexion à la base de données
        self.cursor = self.db.cursor()

    # Créer une nouvelle commune (Create)
    def create_municipality(self, nom, region, superficie, densite, population):
        try:
            sql = "INSERT INTO Commune (nom, region, superficie, densite, population) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (nom, region, superficie, densite, population))
            self.db.commit()
            print(f"Commune '{nom}' créée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la création de la commune: {e}")
            self.db.rollback()

    # Lire toutes les communes (Read)
    def get_all_municipalities(self):
        try:
            sql = "SELECT * FROM Commune"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des communes: {e}")
            return None

    # Lire une seule commune par ID (Read)
    def get_municipality_by_id(self, municipality_id):
        try:
            sql = "SELECT * FROM Commune WHERE id = %s"
            self.cursor.execute(sql, (municipality_id,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Erreur lors de la récupération de la commune ID {municipality_id}: {e}")
            return None

    # Mettre à jour une commune (Update)
    def update_municipality(self, municipality_id, nom, region, superficie, densite, population):
        try:
            sql = """
            UPDATE Commune 
            SET nom = %s, region = %s, superficie = %s, densite = %s, population = %s 
            WHERE id = %s
            """
            self.cursor.execute(sql, (nom, region, superficie, densite, population, municipality_id))
            self.db.commit()
            print(f"Commune ID {municipality_id} mise à jour avec succès.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la commune: {e}")
            self.db.rollback()

    # Supprimer une commune (Delete)
    def delete_municipality(self, municipality_id):
        try:
            sql = "DELETE FROM Commune WHERE id = %s"
            self.cursor.execute(sql, (municipality_id,))
            self.db.commit()
            print(f"Commune ID {municipality_id} supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de la commune: {e}")
            self.db.rollback()
