import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller

    def build(self):
        self.page.title = "Accueil - Gestion des informations"
        # Créer la barre de navigation avec NavigationRail
        rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.SPACE_DASHBOARD_OUTLINED, selected_icon=ft.icons.SPACE_DASHBOARD_ROUNDED, label="Dashboard"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.SPACE_DASHBOARD_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED),
                    label="Demande des informations",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.DETAILS),
                    label_content=ft.Text("Détails"),
                ),
            ],
            on_change=self.on_navigation_change,  # Gérer la navigation
        )

        # Contenu principal (par défaut, page de bienvenue)
        self.body_content = ft.Text(
            value="Bienvenue dans l'application de gestion !",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE
        )

        logout_button = ft.ElevatedButton(
            text="Déconnexion",
            on_click=lambda e: self.controller.logout()
        )

        # Mise en page avec la barre de navigation à gauche et le contenu principal à droite
        return ft.Row(
            [
                rail,  # NavigationRail à gauche
                ft.VerticalDivider(width=1),  # Séparateur vertical
                ft.Column(
                    [
                        self.body_content,
                        logout_button,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True  # Prendre toute la place disponible pour la colonne
                ),
            ],
            expand=True  # Expande pour occuper toute la fenêtre
        )

    def on_navigation_change(self, e):
        # Mettre à jour le contenu en fonction de la sélection dans le NavigationRail
        selected_index = e.control.selected_index

        if selected_index == 0:
            self.body_content.value = "Bienvenue sur le tableau de bord !"
        elif selected_index == 1:
            self.body_content.value = "Affichage des demandes d'informations."
        elif selected_index == 2:
            self.body_content.value = "Affichage des détails."

        # Mettre à jour la page après changement
        self.page.update()

