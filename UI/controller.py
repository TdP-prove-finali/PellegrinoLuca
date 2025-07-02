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
        for i in range(1,6):
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

    def leggiddTime(self, e):
        # e.control.value è un float, arrotondiamolo ad intero:
        timeWork_min = int(e.control.value)
        # salvalo per handlePlane
        self.timeWork_min = timeWork_min
        # aggiorna la label sopra lo slider
        self._view.lblTime.value = f"Durata allenamento: {timeWork_min} min"
        self._view.lblTime.update()

    def handlePlane(self,e):

        level = self._view.ddLevelTab2.value
        if not level:
            self._view.create_alert("Seleziona un livello.")
            return

        try:
            numDay = int(self._view.ddNumWorkout.value)
        except (TypeError, ValueError):
            self._view.create_alert("Seleziona un numero di allenamenti valido.")
            return

        if getattr(self, "timeWork_min", 0) == 0:
            self._view.create_alert("Seleziona un tempo di allenamento maggiore di 0.")
            return
        timeWork = self.timeWork_min * 60


        focus = self._view.ddFocus.value
        if not focus:
            self._view.create_alert("Seleziona un obiettivo.")
            return


        listaNonDesiCompleta = []
        for es in self.listaNonDesiderati:
            nome = es.name
            for esercizio in self._model.listaExercises:
                if nome == esercizio.name:
                    listaNonDesiCompleta.append(esercizio)


        self._model.creaGrafo(level, listaNonDesiCompleta)
        #prove per verificare durante la creazione del codice
        print(f"Nodi: {self._model.getNumNodes()}")
        print(f"Archi: {self._model.getNumEdges()}")

        if self._view.ddFocus.value == "loss":

            self._model.getPathCalories(numDay, timeWork)
            piano = self._model.pathCalories
            calorie_totali = self._model.bestCals
            print(f"{piano}")

            """lp = self._view.listPlane
            lp.controls.clear()

            if not piano or all(len(g) == 0 for g in piano):
                lp.controls.append(ft.Text(
                    "Nessun piano trovato con questi parametri.",
                    color="red"
                ))
            else:
                for idx, giorno in enumerate(piano, start=1):
                    giorno_cal = sum(ex.caloriesTot for ex in giorno)
                    lp.controls.append(
                        ft.Text(f"Giorno {idx} (tot. {giorno_cal:.1f} cal):",
                                weight="bold")
                    )
                    for ex in giorno:
                        durata_min = ex.tempoTot // 60
                        lp.controls.append(
                            ft.Text(f"• {ex.name} — {durata_min}′ — {ex.caloriesTot:.1f} cal")
                        )
                    if idx < len(piano):
                        lp.controls.append(ft.Divider())

            lp.update()
            self._view.update_page()"""


        elif self._view.ddFocus.value == "strength":
            self._model.getPathReps(numDay, timeWork)








