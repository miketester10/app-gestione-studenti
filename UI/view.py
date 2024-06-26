import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "App Gestione Studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        self._controller = None # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        # graphical elements
        self._title = None
        self.__theme_switch = None
        self._ddCorso = None
        self._btnCercaIscritti = None
        self._txtMatricola = None
        self._txtNome = None
        self._txtCognome = None
        self._btnCercaStudente = None
        self._btnCercaCorsi = None
        self._btnIscrivi = None
        self._txt_result = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # Row 0
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)

        row0 = ft.Row(spacing=400, controls=[self.__theme_switch, self._title],
                      alignment=ft.MainAxisAlignment.START)

        # Row 1
        self._ddCorso = ft.Dropdown(label="Corso",width=650)
        self._controller.fill_ddCorso()
        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_get_iscritti_by_codins)
        
        row1 = ft.Row([self._ddCorso, self._btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row 2
        self._txtMatricola = ft.TextField(label="Matricola",width=150)
        self._txtNome = ft.TextField(label="Nome",width=300, read_only=True)
        self._txtCognome = ft.TextField(label="Cognome",width=300, read_only=True)
        
        row2 = ft.Row([self._txtMatricola, self._txtNome, self._txtCognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row 3
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_get_studente_by_matricola)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_get_corsi_by_matricola)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi studente", on_click=self._controller.handle_iscrivi_studente)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row 4 - List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        self._page.add(row0, row1, row2, row3, self._txt_result)
        self.update()

    def set_controller(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self._page.theme_mode = (
            ft.ThemeMode.DARK
            if self._page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self._page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self._page.update()