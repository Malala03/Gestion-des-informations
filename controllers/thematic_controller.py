from dbconnect import get_db_connection

class ThematicController:
    def __init__(self, page):
        self.page = page
        self.db = get_db_connection()  #connexion avec la bd
        self.cursor = self.db.cursor()