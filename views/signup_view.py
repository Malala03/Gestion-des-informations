import flet as ft

class SignupView:
    def __init__(self, page: ft.Page, controller, show_login):
        self.page = page
        self.controller = controller
        self.show_login = show_login
        page.window_width = 400
        page.window_height = 400
        page.window_center()

    def build(self):
        self.page.title = "Inscription - Gestion des informations"
        
        # Créer les champs de texte et le bouton avec des icônes
        self.username_field = ft.TextField(
            label="Nom d'utilisateur", 
            width=300, 
            prefix_icon=ft.icons.PERSON
        )
        self.password_field = ft.TextField(
            label="Mot de passe", 
            password=True, 
            width=300, 
            prefix_icon=ft.icons.LOCK
        )

        signup_button = ft.ElevatedButton(
            text="S'inscrire", 
            on_click=self.on_signup_click
        )

        login_link = ft.TextButton(
            text="Déjà un compte ? Connectez-vous", 
            on_click=lambda e: self.show_login()
        )

        # Centrer le contenu dans un Container comme pour la page de connexion
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Page d'inscription", size=24, weight=ft.FontWeight.BOLD),
                    self.username_field,
                    self.password_field,
                    signup_button,
                    login_link,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,  # Centrer le contenu du Container
            padding=ft.padding.all(20),  # Ajouter un espacement autour si nécessaire
        )

    def on_signup_click(self, e):
        username = self.username_field.value.strip() 
        password = self.password_field.value.strip()

        # Vérifier si les champs sont vides
        if not username or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Veuillez remplir tous les champs !"))
            self.page.snack_bar.open = True
            self.page.update()
            return  # Ne pas continuer si les champs sont vides

        # Appeler la méthode signup du contrôleur si les champs sont remplis
        if self.controller.signup(username, password):
            self.page.snack_bar = ft.SnackBar(ft.Text("Inscription réussie !"))
            self.page.snack_bar.open = True
            self.show_login()  # Retour à la page de connexion
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Échec de l'inscription"))
            self.page.snack_bar.open = True
            self.page.update()
