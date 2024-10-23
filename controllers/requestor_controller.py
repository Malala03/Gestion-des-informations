from dbconnect import get_db_connection

class RequestorController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()  # Connexion à la base de données
        self.cursor = self.db.cursor()

    # Créer un nouveau demandeur (Create)
    def create_requestor(self, nom, categorie, fonction, entite):
        try:
            sql = "INSERT INTO Demandeur (nom, categorie, fonction, entite) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (nom, categorie, fonction, entite))
            self.db.commit()
            print(f"Demandeur '{nom}' créé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la création du demandeur: {e}")
            self.db.rollback()

    # Lire tous les demandeurs (Read)
    def get_all_requestors(self):
        try:
            sql = "SELECT * FROM Demandeur"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des demandeurs: {e}")
            return None

    # Lire un seul demandeur par ID (Read)
    def get_requestor_by_id(self, requestor_id):
        try:
            sql = "SELECT * FROM Demandeur WHERE id = %s"
            self.cursor.execute(sql, (requestor_id,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Erreur lors de la récupération du demandeur ID {requestor_id}: {e}")
            return None

    # Mettre à jour un demandeur (Update)
    def update_requestor(self, requestor_id, nom, categorie, fonction, entite):
        try:
            sql = "UPDATE Demandeur SET nom = %s, categorie = %s, fonction = %s, entite = %s WHERE id = %s"
            self.cursor.execute(sql, (nom, categorie, fonction, entite, requestor_id))
            self.db.commit()
            print(f"Demandeur ID {requestor_id} mis à jour avec succès.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour du demandeur: {e}")
            self.db.rollback()

    # Supprimer un demandeur (Delete)
    def delete_requestor(self, requestor_id):
        try:
            sql = "DELETE FROM Demandeur WHERE id = %s"
            self.cursor.execute(sql, (requestor_id,))
            self.db.commit()
            print(f"Demandeur ID {requestor_id} supprimé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression du demandeur: {e}")
            self.db.rollback()
