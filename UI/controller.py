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
        self._view.listaEserc.controls.append(
            ft.Text("Elenco esercizi:", color="blue")
        )

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
        selected = self._view.ddExercise.value
        if selected is None:
            self.esercizio = None
        else:
            # converto a intero per far combaciare con le chiavi della mappa
            selected_id = int(selected)
            self.esercizio = self._model.mapExercisesDistinct[selected_id]

    def handleAddUndesired(self, e):
        selected = self._view.ddExercise.value

        if not selected:
            self.esercizio = None
        else:
            selected_id = int(selected)
            self.esercizio = self._model.mapExercisesDistinct[selected_id]

        #se non hai selezionato nulla
        if self.esercizio is None:
            self._view.create_alert("Seleziona prima un esercizio da aggiungere.")

            de = self._view.ddExercise
            de.value = None
            de.update()
            return

        #se non è già in non_desiderati
        if self.esercizio not in self.listaNonDesiderati:
            self.listaNonDesiderati.append(self.esercizio)

            self._view.listaUndesiderata.controls.append(
                ft.Text(self.esercizio.name, color="black")
            )

            ud = self._view.ddUndesired
            ud.options.append(ft.dropdown.Option(self.esercizio.id, self.esercizio.name))
            ud.value = None
            ud.update()
        #se è già in non_desiderati
        else:
            self._view.create_alert(
                f"L'esercizio “{self.esercizio.name}” è già in lista non desiderata."
            )

        de = self._view.ddExercise
        de.value = None
        de.update()

        self._view.update_page()

    def handleRemoveUndesired(self, e):

        sel = self._view.ddUndesired.value
        if not sel:
            self._view.create_alert("Seleziona prima un esercizio da rimuovere.")
            return

        es = self._model.mapExercisesDistinct[int(sel)]

        if es in self.listaNonDesiderati:
            self.listaNonDesiderati.remove(es)
        else:
            self._view.create_alert("Errore: esercizio non in lista.")
            return

        lv = self._view.listaUndesiderata
        lv.controls.clear()
        lv.controls.append(ft.Text("Elenco non desiderati:", color="red"))
        for item in self.listaNonDesiderati:
            lv.controls.append(ft.Text(item.name, color="black"))
        lv.update()

        ud = self._view.ddUndesired
        ud.options.clear()
        for item in self.listaNonDesiderati:
            ud.options.append(ft.dropdown.Option(item.id, item.name))
        ud.value = None
        ud.update()

        self._view.update_page()

    def handleClearUndesired(self, e):

        self.listaNonDesiderati.clear()

        lv = self._view.listaUndesiderata
        lv.controls.clear()
        lv.controls.append(ft.Text("Elenco non desiderati:", color="red"))
        lv.update()

        ud = self._view.ddUndesired
        ud.options.clear()
        ud.value = None
        ud.update()

        self._view.update_page()


    def fillDDlevelPlane(self):
        listaLivelli = self._model.getLivelli()
        for l in listaLivelli:
            self._view.ddLevelTab2.options.append(ft.dropdown.Option(l))
        self._view.update_page()

    def fillDDnumWorkout(self):
        for i in range(1, 8):
            self._view.ddNumWorkout.options.append(
                ft.dropdown.Option(text=str(i), key=i)
            )
        self._view.update_page()

    def fillDDfocus(self):

        self._view.ddFocus.options.append(
            ft.dropdown.Option(text="Perdita di peso", key="loss")
        )
        self._view.ddFocus.options.append(
            ft.dropdown.Option(text="Aumento forza", key="strength")
        )

        self._view.ddFocus.on_change = self.leggiddFocus
        self._view.update_page()

    def leggiddFocus(self, e):
        sel = self._view.ddFocus.value
        if sel == "loss":
            self._view.create_alert("Selezionando perdita di peso il programma creerà un piano bilanciato, volto a massimizzare il consumo calorico")
        elif sel == "strength":
            self._view.create_alert("Selezionando aumento forza il programma creerà un piano bilanciato, volto a minimizzare il numero di ripetizioni,"
                                    "permettendo l'utilizzo di carichi maggiori")

    def handlePlane(self,e):
        pass








