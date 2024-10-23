from dbconnect import get_db_connection

class LoginController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()  #connexion avec la bd
        self.cursor = self.db.cursor()

    def login(self, username, password):
        query = "SELECT * FROM Admin WHERE nom_utilisateur = %s AND mot_de_passe = %s"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        
        if result:
            return True  
        return False 