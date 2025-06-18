from db.connection import workout_plans_collection

class Workout:
    def __init__(self, day, name):
        self.day = day
        self.name = name
        self.exercies = []

    def update_workout(email, day, new_data):
        try:
            update_fields = {}
            if "name" in new_data:
                update_fields["workouts.$[elem].name"] = new_data["name"]
            if "exercises" in new_data:
                update_fields["workouts.$[elem].exercises"] = new_data["exercises"]

            workout_plans_collection().update_one(
                {"email": email},
                {"$set": update_fields},
                array_filters=[{"elem.day": day}])
            return True
        except Exception as e:
            print("Erro ao atualizar treino", e)
            return e