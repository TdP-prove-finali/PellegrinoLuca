import copy
import itertools

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.listaExercisesDistinct = DAO.getDistinctExercises()
        self.mapExercisesDistinct = {}
        self.listaExercises = DAO.getAllExercises()
        self.mapExercises = {}

        for e in self.listaExercisesDistinct:
            self.mapExercisesDistinct[e.id] = e
        for es in self.listaExercises:
            self.mapExercises[es.id] = es

        self.grafo = nx.Graph()

        self.pathCalories = []
        self.pathReps = []
        self.bestCals = []
        self.bestReps = []


    def getLivelli(self):
        return DAO.getLevel()

    def getMuscoli(self):
        return DAO.getMuscle()

    def getEsercizi(self, livello, muscolo):
        # definisco due flag di “nessun filtro”
        no_livello = livello in (None, "", "None")
        no_muscolo = muscolo in (None, "", "None")

        if no_livello and no_muscolo:
            # nessun filtro applicato
            return DAO.getDistinctExercises()

        if no_livello:
            # solo muscolo
            return DAO.getExercisesByMuscolo(muscolo)

        if no_muscolo:
            # solo livello
            return DAO.getExercisesByLivello(livello)

        # entrambi i filtri
        return DAO.getExercisesByLivelloEMuscolo(livello, muscolo)

    def getAllExercises(self):
        return DAO.getAllExercises()

    def creaGrafo(self, level, listaNonDesi):

        self.grafo.clear()
        exercises = DAO.getExercisesLevel(level)

        listaDesiCompl = []
        for es in exercises:
            desi = True
            nome = es.name
            for esercizio in listaNonDesi:
                if nome == esercizio.name:
                    desi = False
            if desi:
                listaDesiCompl.append(es)

        self.grafo.add_nodes_from(listaDesiCompl)


        edges = [
            (u, v) for u, v in itertools.combinations(listaDesiCompl, 2)
            if u.name != v.name
        ]

        self.grafo.add_edges_from(edges)


    def getPathCalories(self,numDay, timeWork):
        self.pathCalories = [[] for _ in range(numDay)]
        self.bestCals = [0 for _ in range(numDay)]

        for i in range(1, numDay+1):
            for n in self.get_nodes():

                check = False
                for ogg in self.pathCalories:
                    for eser in ogg:
                        if eser.id == n.id:
                            check = True
                            break

                if not check and i >= 2:
                    for esercizio in self.pathCalories[i - 2]:
                        if esercizio.name == n.name:
                            check = True
                            break

                if not check:
                    if n.tempoTot <= timeWork:
                        partial = []
                        partial.append(n)
                        time_used = n.tempoTot
                        self.ricorsione(partial, i, timeWork, time_used)

    def ricorsione(self, partial, day, timeWork, time_used):

        n_last = partial[-1]

        neighbors = self.getAdmissibleNeighbs(n_last, partial, day, timeWork, time_used)

        if len(neighbors) == 0:
            cals_accDay = self.calcolaCals(partial)
            if cals_accDay > self.bestCals[day-1]:
                self.bestCals[day-1] = cals_accDay + 0.0
                self.pathCalories[day-1] = partial[:]
            return

        for n in neighbors:
            partial.append(n)
            new_time = time_used + n.tempoTot
            self.ricorsione(partial, day, timeWork, new_time)
            partial.pop()


    def getAdmissibleNeighbs(self, n_last, partial, day, timeWork, time_used):

        all_neigh = list(self.grafo.neighbors(n_last))
        result = []

        for es in all_neigh:

            skip = False
            for ogg in self.pathCalories:
                for eser in ogg:
                    if eser.id == es.id:
                        skip = True
                        break

            if not skip and day >= 2:
                for esercizio in self.pathCalories[day-2]:
                    if esercizio.name == es.name:
                        skip = True
                        break

            if not skip:
                for elem in partial:
                    if elem.name == es.name:
                        skip = True
                        break

            if not skip and time_used + es.tempoTot > timeWork:
                skip = True

            # se non ho trovato alcuna corrispondenza lo aggiungo
            if not skip:
                result.append(es)

        return result


    def calcolaCals(self, myList):
        weight = 0
        for es in myList:
            weight += es.caloriesTot
        return weight


    def getPathReps(self, numDay, timeWork):

        self.pathReps = [[] for _ in range(numDay)]
        self.bestReps = [float('inf') for _ in range(numDay)]

        for i in range(1, numDay+1):
            for n in self.get_nodes():

                check = False
                for ogg in self.pathReps:
                    for eser in ogg:
                        if eser.id == n.id:
                            check = True
                            break

                if not check and i >= 2:
                    for esercizio in self.pathReps[i - 2]:
                        if esercizio.name == n.name:
                            check = True
                            break

                if not check:
                    if n.tempoTot <= timeWork:
                        partial = []
                        partial.append(n)
                        time_used = n.tempoTot
                        self.ricorsioneReps(partial, i, timeWork, time_used)


    def ricorsioneReps(self,partial, day, timeWork, time_used):

        n_last = partial[-1]

        neighbors = self.getAdmissibleNeighbsReps(n_last, partial, day, timeWork, time_used)

        if len(neighbors) == 0:
            reps_accDay = self.calcolaReps(partial)
            if reps_accDay < self.bestReps[day-1]:
                self.bestReps[day-1] = reps_accDay + 0.0
                self.pathReps[day-1] = partial[:]
            return

        for n in neighbors:
            partial.append(n)
            new_time = time_used + n.tempoTot
            self.ricorsioneReps(partial, day, timeWork, new_time)
            partial.pop()


    def getAdmissibleNeighbsReps(self, n_last, partial, day, timeWork, time_used):

        all_neigh = list(self.grafo.neighbors(n_last))
        result = []

        for es in all_neigh:

            skip = False
            for ogg in self.pathReps:
                for eser in ogg:
                    if eser.id == es.id:
                        skip = True
                        break

            if not skip and day >= 2:
                for esercizio in self.pathReps[day-2]:
                    if esercizio.name == es.name:
                        skip = True
                        break

            if not skip:
                for elem in partial:
                    if elem.name == es.name:
                        skip = True
                        break

            if not skip and time_used + es.tempoTot > timeWork:
                skip = True

            # se non ho trovato alcuna corrispondenza lo aggiungo
            if not skip:
                result.append(es)

        return result

    def calcolaReps(self, myList):
        weight = 0
        for es in myList:
            weight += es.punteggioForPath
        return weight/len(myList)


    def getNumNodes(self):
        return len(self.grafo.nodes())

    def getNumEdges(self):
        return len(self.grafo.edges())

    def get_nodes(self):
        return self.grafo.nodes()

    def get_edges(self):
        return self.grafo.edges()



