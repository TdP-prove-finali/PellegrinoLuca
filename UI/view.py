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


    def load_interface(self):
        self.tabs = ft.Tabs()
        self.tab1 = ft.Tab(text="Home", content=self.creaTab1())
        self.tab2 = ft.Tab(text="Piani Fit", content=self.creaTab2())

        self.tabs.tabs.append(self.tab1)
        self.tabs.tabs.append(self.tab2)

        self._titolo_generale = ft.Text("Applicativo per la generazione di piani d’allenamento personalizzati", size=28, weight="bold", color="blue")

        self._layout_principale = ft.Column(controls=[self._titolo_generale, self.tabs], spacing=20)

        self._page.add(self._layout_principale)

        self.update_page()

    def creaTab1(self):
        pass

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
