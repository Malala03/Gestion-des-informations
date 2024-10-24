import flet as ft
from views.login_view import LoginView
from views.signup_view import SignupView
from views.dashboard_view import DashboardView
from controllers.login_controller import LoginController
from controllers.signup_controller import SignupController
from controllers.dashboard_controller import DashboardController

def main(page: ft.Page):
    login_controller = LoginController(page)
    signup_controller = SignupController(page)
    dashboard_controller = DashboardController(page)  # Correction de l'orthographe ici

    # Navigation entre les pages
    def show_login():
        login_view = LoginView(page, login_controller, show_signup, show_dashboard)
        page.clean()
        page.add(login_view.build())
        page.update()

    def show_signup():
        signup_view = SignupView(page, signup_controller, show_login)
        page.clean()
        page.add(signup_view.build())
        page.update()

    def show_dashboard():
        dashboard_view = DashboardView(page, dashboard_controller)  # Correction ici aussi
        page.clean()
        page.add(dashboard_view.build())
        page.update()

    # Afficher la page de connexion par défaut
    show_login()

if __name__ == "__main__":
    ft.app(target=main)