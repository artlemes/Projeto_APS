from db.connection import workout_plans_collection

class WorkoutPlan:
    def __init__(self, email, name, goal, amount_of_sessions, workouts):
        self.email = email
        self.name = name
        self.goal = goal 
        self.amount_of_sessions = amount_of_sessions
        self.workouts = workouts

    def create_workout_plan(workout_plan_data):
        try:
            collection = workout_plans_collection()
            workout_plan = {
                "email": workout_plan_data.email,
                "name": workout_plan_data.name,
                "goal": workout_plan_data.goal,
                "sessions": workout_plan_data.amount_of_sessions,
                "workouts": workout_plan_data.workouts,
            }
            res = collection.insert_one(workout_plan)
            print(res)
            return True
        except:
            return "Erro ao Cadastrar."
    
    @staticmethod
    def delete_workout_plan(email):
        try:
            collection = workout_plans_collection()
            collection.delete_one({"email":email})
            return True 
        except Exception as e:
            print(f"Erro: {e}")

    def update_workout_plan(email, updated_data):
        try:
            collection = workout_plans_collection()
            novos_dados = {
                "name": updated_data["name"],
                "goal": updated_data["goal"],
                "sessions": updated_data["sessions"]}
            print("Novos_dados", novos_dados)
            collection.update_one(
                {"email": email},
                {"$set": novos_dados}
            )
            return True
        except Exception as e:
            print(e)
            raise Exception
        