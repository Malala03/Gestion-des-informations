class LoginController:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        # Remplacez cette logique par votre vérification de l'utilisateur
        if username == "admin" and password == "admin":
            return True  # Connexion réussie
        return False  # Échec de la connexion
