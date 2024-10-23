import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller

    def build(self):
        welcome_text = ft.Text(
            value="Bienvenue dans l'application de gestion !",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE
        )

        logout_button = ft.ElevatedButton(
            text="Déconnexion",
            on_click=lambda e: self.controller.logout()
        )

        return ft.Column(
            [
                welcome_text,
                logout_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
