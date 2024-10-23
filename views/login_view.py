import flet as ft


class LoginView:
    def __init__(self, page: ft.Page, controller, show_signup, show_home):
        self.page = page
        self.controller = controller
        self.show_signup = show_signup
        self.show_home = show_home
        page.window_width = 400
        page.window_height = 400
        page.window_center()

    def build(self):
        self.page.title = "Connexion - Gestion des informations"
        
        # Créer les champs de texte et le bouton avec des icônes
        self.username_field = ft.TextField(
            label="Nom d'utilisateur", 
            width=300,
            prefix_icon=ft.icons.PERSON  # Ajouter une icône de personne
        )
        self.password_field = ft.TextField(
            label="Mot de passe", 
            password=True, 
            width=300,
            prefix_icon=ft.icons.LOCK  # Ajouter une icône de cadenas
        )

        login_button = ft.ElevatedButton(
            text="Se connecter", 
            on_click=self.on_login_click
        )

        signup_link = ft.TextButton(
            text="Pas de compte ? Inscrivez-vous", 
            on_click=lambda e: self.show_signup()
        )

        # Centrer le contenu dans un Container
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Page de connexion", size=24, weight=ft.FontWeight.BOLD),
                    self.username_field,
                    self.password_field,
                    login_button,
                    signup_link,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,  # Centrer le contenu du Container
            padding=ft.padding.all(20),  # Optionnel : ajouter un espacement autour
        )

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        if self.controller.login(username, password):
            self.page.snack_bar = ft.SnackBar(ft.Text("La connexion est réussi !"))
            self.page.snack_bar.open = True
            self.show_home()  # Redirection vers la page d'accueil
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Échec de la connexion !"))
            self.page.snack_bar.open = True
            self.page.update()
