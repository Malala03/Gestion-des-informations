class HomeController:
    def __init__(self, page):
        self.page = page
    
    

    def logout(self):
        self.page.snack_bar = ft.SnackBar(ft.Text("Déconnexion réussie !"))
        self.page.snack_bar.open = True
        self.page.update()
