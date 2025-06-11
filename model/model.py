from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.listaExercisesDistinct = DAO.getDistinctExercises()
        self.mapExercisesDistinct = {}
        for e in self.listaExercisesDistinct:
            self.mapExercisesDistinct[e.id] = e

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



