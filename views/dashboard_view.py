import flet as ft
class DashboardView:
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller

    def build(self):
        self.page.title = "Tableau de bord - Gestion des informations"
        
        # Créer la barre de navigation avec NavigationRail
        rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.SPACE_DASHBOARD_OUTLINED, 
                    selected_icon=ft.icons.SPACE_DASHBOARD_ROUNDED, 
                    label="Tableau de bord"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.LOCATION_ON_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.LOCATION_ON_ROUNDED),
                    label="Gérer la commune",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FORMAT_PAINT_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.FORMAT_PAINT_ROUNDED),
                    label_content=ft.Text("Gérer la thématique"),
                ),
                 ft.NavigationRailDestination(
                    icon=ft.icons.PERSON_PIN_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.PERSON_PIN_ROUNDED),
                    label_content=ft.Text("Gérer les demandeurs"),
                ),
                 ft.NavigationRailDestination(
                    icon=ft.icons.QUESTION_ANSWER_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.QUESTION_ANSWER_ROUNDED),
                    label_content=ft.Text("Gérer la demande"),
                ),       
                 ft.NavigationRailDestination(
                    icon=ft.icons.INFO_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.INFO_ROUNDED),
                    label_content=ft.Text("Voirs les détails"),
                ),       
            ],
            on_change=self.on_navigation_change,  # Gérer la navigation
        )

        # Contenu principal - Par défaut, le tableau de bord est affiché
        self.body_content = ft.Text(
            value="Bienvenue sur le tableau de bord !",  # Affichage du tableau de bord par défaut
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE
        )

        logout_button = ft.ElevatedButton(
            text="Déconnexion",
            icon=ft.icons.LOGOUT,
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
        elif selected_index == 3:
            self.body_content.value = "Gérer les demandeurs."
        elif selected_index == 4:
            self.body_content.value = "Gérer la demande."
        elif selected_index == 5:
            self.body_content.value = "Voir les détails."
        # Mettre à jour la page après changement
        self.page.update()
