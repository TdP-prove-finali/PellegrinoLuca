from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        pass

    def getLivelli(self):
        return DAO.getLevel()

    def getMuscoli(self):
        return DAO.getMuscle()