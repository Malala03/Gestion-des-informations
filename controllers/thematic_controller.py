from dbconnect import get_db_connection

class ThematicController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()  # Connexion à la base de données
        self.cursor = self.db.cursor()

    # Créer une nouvelle thématique (Create)
    def create_thematic(self, nom):
        try:
            sql = "INSERT INTO Thematique (nom) VALUES (%s)"
            self.cursor.execute(sql, (nom,))
            self.db.commit()
            print(f"Thématique '{nom}' créée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la création de la thématique: {e}")
            self.db.rollback()

    # Lire toutes les thématiques (Read)
    def get_all_thematics(self):
        try:
            sql = "SELECT * FROM Thematique"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des thématiques: {e}")
            return None

    # Lire une seule thématique par ID (Read)
    def get_thematic_by_id(self, thematic_id):
        try:
            sql = "SELECT * FROM Thematique WHERE id = %s"
            self.cursor.execute(sql, (thematic_id,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Erreur lors de la récupération de la thématique ID {thematic_id}: {e}")
            return None

    # Mettre à jour une thématique (Update)
    def update_thematic(self, thematic_id, nom):
        try:
            sql = "UPDATE Thematique SET nom = %s WHERE id = %s"
            self.cursor.execute(sql, (nom, thematic_id))
            self.db.commit()
            print(f"Thématique ID {thematic_id} mise à jour avec succès.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la thématique: {e}")
            self.db.rollback()

    # Supprimer une thématique (Delete)
    def delete_thematic(self, thematic_id):
        try:
            sql = "DELETE FROM Thematique WHERE id = %s"
            self.cursor.execute(sql, (thematic_id,))
            self.db.commit()
            print(f"Thématique ID {thematic_id} supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de la thématique: {e}")
            self.db.rollback()
