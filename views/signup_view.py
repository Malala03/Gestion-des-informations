import flet as ft

class SignupView:
    def __init__(self, page: ft.Page, controller, show_login):
        self.page = page
        self.controller = controller
        self.show_login = show_login

    def build(self):
        self.username_field = ft.TextField(label="Nom d'utilisateur", width=300)
        self.password_field = ft.TextField(label="Mot de passe", password=True, width=300)

        signup_button = ft.ElevatedButton(
            text="S'inscrire", 
            on_click=self.on_signup_click
        )

        login_link = ft.TextButton(
            text="Déjà un compte ? Connectez-vous", 
            on_click=lambda e: self.show_login()
        )

        return ft.Column(
            [
                ft.Text("Page d'inscription", size=24, weight=ft.FontWeight.BOLD),
                self.username_field,
                self.password_field,
                signup_button,
                login_link,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_signup_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        if self.controller.signup(username, password):
            self.page.snack_bar = ft.SnackBar(ft.Text("Inscription réussie !"))
            self.page.snack_bar.open = True
            self.show_login()  # Retour à la page de connexion
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Échec de l'inscription"))
            self.page.snack_bar.open = True
            self.page.update()
