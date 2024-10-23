import flet as ft
from views.login_view import LoginView
from views.signup_view import SignupView
from views.home_view import HomeView
from controllers.login_controller import LoginController
from controllers.signup_controller import SignupController
from controllers.home_controller import HomeController

def main(page: ft.Page):
    page.title = "Application de Gestion"
    page.window_width = 400
    page.window_height = 600

    login_controller = LoginController(page)
    signup_controller = SignupController(page)
    home_controller = HomeController(page)

    # Navigation entre les pages
    def show_login():
        login_view = LoginView(page, login_controller, show_signup, show_home)
        page.clean()
        page.add(login_view.build())
        page.update()

    def show_signup():
        signup_view = SignupView(page, signup_controller, show_login)
        page.clean()
        page.add(signup_view.build())
        page.update()

    def show_home():
        home_view = HomeView(page, home_controller)
        page.clean()
        page.add(home_view.build())
        page.update()

    # Afficher la page de connexion par défaut
    show_login()

if __name__ == "__main__":
    ft.app(target=main)
