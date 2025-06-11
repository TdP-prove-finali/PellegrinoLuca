import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.muscolo = None
        self.livello = None
        self.esercizio = None
        self.listaNonDesiderati = []


    def fillDDlevel(self):
        listaLivelli = self._model.getLivelli()
        for l in listaLivelli:
            self._view.ddlevel.options.append(ft.dropdown.Option(l))
        self._view.update_page()

    def fillDDmuscleGroup(self):
        listaMuscoli = self._model.getMuscoli()
        for m in listaMuscoli:
            self._view.ddmuscleGroup.options.append(ft.dropdown.Option(m))
        self._view.update_page()


    def leggiddLevel(self,e):
        if self._view.ddlevel.value == "None":
            self.livello = None
        else:
            self.livello = self._view.ddlevel.value

    def leggiddMuscleGroup(self,e):
        if self._view.ddmuscleGroup.value == "None":
            self.muscolo = None
        else:
            self.muscolo = self._view.ddmuscleGroup.value

    def handleEsercizi(self, e):
        elenco = self._model.getEsercizi(self.livello, self.muscolo)

        self._view.listaEserc.controls.clear()
        self.currentExercises = elenco

        if not elenco:
            self._view.listaEserc.controls.append(ft.Text("Non ci sono esercizi con questi filtri"))
        else:
            for es in elenco:
                self._view.listaEserc.controls.append(ft.Text(es.name))

        dd = self._view.ddExercise
        dd.options.clear()
        for es in elenco:
            dd.options.append(ft.dropdown.Option(es.id, es.name))
        dd.value = None
        dd.update()

        self._view.update_page()

    def handleReset(self,e):

        self.livello = None
        self.muscolo = None

        self._view.ddlevel.value = None
        self._view.ddlevel.update()

        self._view.ddmuscleGroup.value = None
        self._view.ddmuscleGroup.update()

        self._view.ddExercise.value = None
        self._view.ddExercise.options.clear()
        self._view.ddExercise.update()

        self._view.listaEserc.controls.clear()
        self._view.listaEserc.controls.append(
            ft.Text("Elenco esercizi:", color="blue")
        )

        self._view.update_page()

    def leggiddEsercizio(self, e):
        selected_id = self._view.ddExercise.value
        if selected_id is None:
            self.esercizio = None
        else:
            self.esercizio = self._model.mapExercisesDistinct[selected_id]

    def handleAddUndesired(self,e):
        self.listaNonDesiderati.append(self.esercizio)



