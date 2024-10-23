import flet as ft

class LoginView:
    def __init__(self, page: ft.Page, controller, show_signup, show_home):
        self.page = page
        self.controller = controller
        self.show_signup = show_signup
        self.show_home = show_home
    
    def build(self):
        self.username_field = ft.TextField(label="Nom d'utilisateur", width=300)
        self.password_field = ft.TextField(label="Mot de passe", password=True, width=300)

        login_button = ft.ElevatedButton(
            text="Se connecter", 
            on_click=self.on_login_click
        )

        signup_link = ft.TextButton(
            text="Pas de compte ? Inscrivez-vous", 
            on_click=lambda e: self.show_signup()
        )

        return ft.Column(
            [
                ft.Text("Page de connexion", size=24, weight=ft.FontWeight.BOLD),
                self.username_field,
                self.password_field,
                login_button,
                signup_link,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        if self.controller.login(username, password):
            self.show_home()  # Redirection vers la page d'accueil
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Échec de la connexion"))
            self.page.snack_bar.open = True
            self.page.update()
