from db.connection import workout_plans_collection

class Exercise:
    def __init__(self, name, reps_range, weight, sets):
        self.name = name
        self.reps_range = reps_range
        self.weight = weight
        self.sets = sets

    def handle_create(email, day, new_data):
        print("cheguei no model")
        try:
            result = workout_plans_collection().update_one(
                {"email": email},
                {"$set": {"workouts.$[elem].exercises": new_data}},
                array_filters=[{"elem.day": day}]
            )

            if result.modified_count:
                print("Exercícios atualizados com sucesso.")
                return True
            else:
                print("Nenhuma modificação feita. Verifique se o 'day' está correto.")
                return False

        except Exception as e:
            print("Erro ao atualizar exercícios:", e)
            return e


    def update_exercise(email, day, new_data):
        print("cheguei no model")
        try:
            result = workout_plans_collection().update_one(
                {"email": email},
                {"$set": {"workouts.$[elem].exercises": new_data}},
                array_filters=[{"elem.day": day}]
            )

            if result.modified_count:
                print("Exercícios atualizados com sucesso.")
                return True
            else:
                print("Nenhuma modificação feita. Verifique se o 'day' está correto.")
                return False

        except Exception as e:
            print("Erro ao atualizar exercícios:", e)
            return e
    