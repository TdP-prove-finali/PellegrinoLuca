import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


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

    def handleEsercizi(self,e):
        self._view.listaEserc.controls.clear()
        elencoEsercizi =self._model.getEsercizi(self.livello, self.muscolo)
        if len(elencoEsercizi) == 0:
            self._view.listaEserc.controls.append(ft.Text("Non ci sono esercizi con questi filtri"))
        else:
            for es in elencoEsercizi:
                self._view.listaEserc.controls.append(ft.Text(es))
        self._view.update()

