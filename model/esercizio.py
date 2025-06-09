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

    CaloriesTot: float = field(init=False)
    TempoTot: int = field(init=False)

    def __post_init__(self):
        #in secondi (2 minuti per le pause tra una serie e l'altra, 10 s per ogni ripetizione)
        self.TempoTot = (120*self.Sets) + (10*self.Reps*self.Sets)

        #formula in cui viene diviso il tempo per 1800(secondi presenti in 30 minuti) e poi moltiplicato per il dato forntoci dal database
        self.CaloriesTot = (self.TempoTot/1800)*self.Calories30min

    def __hash__(self):
        return hash(self.Id)

