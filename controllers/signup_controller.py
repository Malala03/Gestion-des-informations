from dbconnect import get_db_connection

class SignupController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()   #connexion avec la bd
        self.cursor = self.db.cursor() 

    def signup(self, username, password):
        # Vérifier si l'utilisateur existe déjà
        check_query = "SELECT * FROM Admin WHERE nom_utilisateur = %s"
        self.cursor.execute(check_query, (username,))
        if self.cursor.fetchone():
            return False  # Nom d'utilisateur déjà pris

        # Insérer le nouvel administrateur
        insert_query = "INSERT INTO Admin (nom_utilisateur, mot_de_passe) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (username, password))
        self.db.commit()
        return True  # Inscription réussie
