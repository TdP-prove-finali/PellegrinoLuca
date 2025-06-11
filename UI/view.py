import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        #page stuff
        self._page = page
        self._page.title = "Prova finale: Pellegrino Luca"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        self.tabs = None
        self.tab1 = None
        self.tab2 = None

        self.ddlevel = None
        self.ddmuscleGroup = None
        self.listaEserc = None
        self.btnVistaLista = None


    def load_interface(self):

        self.tabs = ft.Tabs(
            tabs=[
                ft.Tab(text="Home", content=self.creaTab1()),
                ft.Tab(text="Piani Fit", content=self.creaTab2())
            ],
            expand=True
        )

        self._titolo_generale = ft.Text(
            "Applicativo per la generazione di piani d’allenamento personalizzati",
            size=28, weight="bold", color="blue"
        )

        self._layout_principale = ft.Column(
            controls=[self._titolo_generale, self.tabs],
            spacing=20,
            expand=True
        )

        self._page.add(self._layout_principale)
        self._page.update()

    def creaTab1(self):
        # Dropdowns
        self.ddlevel = ft.Dropdown(label="Livello",
                                   on_change=self._controller.leggiddLevel)
        self.ddmuscleGroup = ft.Dropdown(label="Gruppo muscolare",
                                         on_change=self._controller.leggiddMuscleGroup)
        self._controller.fillDDlevel()
        self._controller.fillDDmuscleGroup()

        # Pulsanti
        self.btnVistaLista = ft.ElevatedButton(
            text="Vedi esercizi", on_click=self.controller.handleEsercizi
        )

        self.btnReset = ft.ElevatedButton(
            text="Reset Filtri", on_click=self.controller.handleReset
        )

        # Lista esercizi
        self.listaEserc = ft.ListView(
            controls=[ft.Text("Elenco esercizi:", color="blue")],
            expand=True,
            spacing=8,
            auto_scroll=True
        )

        return ft.Container(
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    ft.Row([ft.Text("Sezione ricerca", color="blue", size=24, weight="bold")]),
                    ft.Row([self.ddlevel, self.ddmuscleGroup], spacing=10),
                    ft.Row([self.btnVistaLista, self.btnReset], spacing=10),
                    ft.Row([self.listaEserc], expand=True)
                ],
                spacing=15,
                expand=True
            )
        )

    def creaTab2(self):
        pass


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
