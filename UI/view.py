import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(page)
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
        self.btnReset = None


        self.ddExercise = None
        self.btnAddToUndesired = None
        self.listaUndesiderata = None
        self.ddUndesired = None
        self.btnRemoveUndesired = None
        self.btnClearUndesired = None

        self.ddLevelTab2 = None
        self.ddNumWorkout = None
        self.tfTime = None
        self.ddFocus = None
        self.btnGenerateWork = None
        self.listPlane = None

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
            size=28, weight="bold", color="black"
        )

        self._layout_principale = ft.Column(
            controls=[self._titolo_generale, self.tabs],
            spacing=20,
            expand=True
        )
        self._page.add(self._layout_principale)
        self._page.update()

    def creaTab1(self):
        # colonna sinistra: filtri + lista Esercizi
        # Dropdown filtri
        self.ddlevel = ft.Dropdown(label="Livello",
                                   on_change=self._controller.leggiddLevel)
        self.ddmuscleGroup = ft.Dropdown(label="Gruppo muscolare",
                                         on_change=self._controller.leggiddMuscleGroup)
        self._controller.fillDDlevel()
        self._controller.fillDDmuscleGroup()

        # Pulsanti sinistra
        self.btnVistaLista = ft.ElevatedButton(
            text="Vedi esercizi", on_click=self._controller.handleEsercizi
        )
        self.btnReset = ft.ElevatedButton(
            text="Reset Filtri", on_click=self._controller.handleReset
        )

        # ListView esercizi
        self.listaEserc = ft.ListView(
            controls=[ft.Text("Elenco esercizi:", color="blue")],
            expand=True,
            spacing=8,
            auto_scroll=True
        )

        left_column = ft.Column(
            controls=[
                ft.Text("Sezione ricerca", color="blue", size=24, weight="bold"),
                ft.Row([self.ddlevel, self.ddmuscleGroup], spacing=10),
                ft.Row([self.btnVistaLista, self.btnReset], spacing=10),
                self.listaEserc
            ],
            expand=True,
            spacing=15
        )

        # colonna destra: gestione lista non desiderati
        self.ddExercise = ft.Dropdown(
            label="Seleziona esercizio",
            options=[],
            width=260,
            on_change=self._controller.leggiddEsercizio
        )
        self.btnAddToUndesired = ft.ElevatedButton(
            text="Aggiungi a non desiderati",
            on_click=self._controller.handleAddUndesired
        )
        self.listaUndesiderata = ft.ListView(
            controls=[ft.Text("Elenco non desiderati:", color="red")],
            expand=True,
            spacing=8,
            auto_scroll=True
        )
        self.ddUndesired = ft.Dropdown(
            label="Esercizi non desiderati",
            options=[],
            width=260
        )
        self.btnRemoveUndesired = ft.ElevatedButton(
            text="Rimuovi selezionato",
            on_click=self._controller.handleRemoveUndesired
        )
        self.btnClearUndesidered = ft.ElevatedButton(
            text="Svuota lista",
            on_click=self._controller.handleClearUndesired
        )

        right_column = ft.Column(
            controls=[
                ft.Text("Gestione esercizi non desiderati", color="red", size=24, weight="bold"),

                ft.Row(
                    controls=[self.ddExercise, self.btnAddToUndesired],
                    spacing=10
                ),

                self.listaUndesiderata,

                ft.Row(
                    controls=[self.ddUndesired,
                              self.btnRemoveUndesired,
                              self.btnClearUndesidered],
                    spacing=10
                ),
            ],
            expand=True,
            spacing=15
        )

        # impaginazione finale: sinistra e destra della tab1
        return ft.Container(
            padding=ft.padding.all(10),
            content=ft.Row(
                controls=[
                    left_column,
                    ft.VerticalDivider(width=1, thickness=1, color="grey"),
                    right_column
                ],
                spacing=20,
                expand=True
            )
        )

    def creaTab2(self):
        # Titolo tab
        self.titleTab2 = ft.Text("Piano d'allenamento", color="green", size=24)

        #ROW1
        # Dropdown e TextField
        self.ddLevelTab2 = ft.Dropdown(label="Livello")
        self.ddNumWorkout = ft.Dropdown(label="Num. allenamenti/sett")
        self.tfTime = ft.TextField(label="Limite durata allenamento (in minuti)")

        row1 = ft.Row(
            controls=[self.ddLevelTab2, self.ddNumWorkout, self.tfTime],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self._controller.fillDDlevelPlane()
        self._controller.fillDDnumWorkout()

        #ROW2
        # Obiettivo
        self.ddFocus = ft.Dropdown(label="Obiettivo")
        row2 = ft.Row(
            controls=[self.ddFocus],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self._controller.fillDDfocus()

        #ROW3
        # Pulsante genera
        self.btnGenerateWork = ft.ElevatedButton(text="Genera allenamento",
                                                 on_click=self._controller.handlePlane)
        row3 = ft.Row(
            controls=[self.btnGenerateWork],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # ListView per visualizzare il piano
        self.listPlane = ft.ListView(
            expand=True,
            auto_scroll=True
        )

        # Impaginazione finale tab2
        return ft.Container(
            padding=ft.padding.all(10),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[self.titleTab2],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    row1,
                    row2,
                    row3,
                    self.listPlane
                ],
                spacing=15,
                expand=True
            )
        )

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(
            title=ft.Text("Attenzione"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=lambda e: self._close_alert())
            ]
        )
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def _close_alert(self):
        self._page.dialog.open = False
        self._page.update()

    def update_page(self):
        self._page.update()
