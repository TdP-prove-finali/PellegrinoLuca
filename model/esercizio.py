from dataclasses import dataclass, field


@dataclass
class Esercizio:
    name: str
    sets: int
    reps: int
    benefit: str
    calories30min: int
    muscleGroup: str
    equipment: str
    level: str
    id: int

    caloriesTot: float = field(init=False)
    tempoTot: int = field(init=False)

    def __post_init__(self):
        #in secondi (2 minuti per le pause tra una serie e l'altra, 10 s per ogni ripetizione)
        self.tempoTot = (120*self.sets) + (10*self.reps*self.sets)

        #formula in cui viene diviso il tempo per 1800(secondi presenti in 30 minuti) e poi moltiplicato per il dato forntoci dal database
        self.caloriesTot = (self.tempoTot/1800)*self.calories30min

    def __hash__(self):
        return hash(self.Id)

    def __str__(self):
        return f"Esercizio: {self.name}, calorie(per 30 min): {self.calories30min}, livello: {self.level}, muscoli: {self.muscleGroup}"

