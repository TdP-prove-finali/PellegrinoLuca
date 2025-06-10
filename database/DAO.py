from database.DB_connect import DBConnect
from model.esercizio import Esercizio


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLevel():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """select distinct e.`Difficulty Level` from exercises e order by FIELD(e.`Difficulty Level`, 'beginner', 'intermediate', 'advanced')"""
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getMuscle():
        conn = DBConnect.get_connection()
        allMusclesRipetuti = []
        allMuscle = []
        cursor = conn.cursor()
        query = """select e.`Target Muscle Group` from exercises e"""
        cursor.execute(query)
        for row in cursor:
            allMusclesRipetuti.append(row[0])

        cursor.close()
        conn.close()

        for muscle in allMusclesRipetuti:
            parts = muscle.split(',')
            for p in parts:
                allMuscle.append(p.strip())

        muscleDistinct = sorted(set(allMuscle))

        return muscleDistinct

    @staticmethod
    def getAllExercises():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * from exercises e"""
        cursor.execute(query)

        for row in cursor:
            result.append(Esercizio(
                name=row["Name of Exercise"],
                sets=row["Sets"],
                reps=row["Reps"],
                benefit=row["Benefit"],
                calories30min=row["Burns Calories (per 30 min)"],
                muscleGroup=row["Target Muscle Group"],
                equipment=row["Equipment Needed"],
                level=row["Difficulty Level"],
                id=row["id_exercise"]
            ))

        cursor.close()
        conn.close()

        return result