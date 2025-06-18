from view.workout_plan_view import WorkoutPlanView
from model.workout_plan import WorkoutPlan
from db.connection import workout_plans_collection


class WorkoutPlanController:
    def __init__(self, root, main_controller):
        self.__root = root
        self.__main_controller = main_controller
        self.__workout_plan_view = WorkoutPlanView(self.__root, self)\

    def create_workout_plan_screen(self, email):
        self.__workout_plan_view.create_workout_plan_screen(email)
    
    def create_workout_plan(self, workout_data):
        try:
            workouts_list = self.__main_controller.main_create_workouts(workout_data["days"])
            workout_plan = WorkoutPlan(workout_data["email"], workout_data["name"], workout_data["goal"], workout_data["sessions"], workouts_list)
            collection = workout_plans_collection()
            if collection.find_one({"email": workout_data["email"]}):
                text_type = "Error"
                text = "Usuário já tem um plano de treino."
                WorkoutPlanView.throw_message(text_type, text)
                return
            WorkoutPlan.create_workout_plan(workout_plan)
            text_type = "Info"
            text = "Plano de treino cadastrado com sucesso!"
            WorkoutPlanView.throw_message(text_type, text)
            self.home_screen()
        except Exception as e:
            print(e)
            text_type = "Error"
            text = "Erro ao cadastrar o plano de treino."
            WorkoutPlanView.throw_message(text_type, text)
    
    def update_workout_plan(self, updated_data):
        email = self.__main_controller.get_logged_user()
        sucesso = WorkoutPlan.update_workout_plan(email, updated_data)
        if sucesso:
            type = "Info"
            text = "Plano de treino atualizado com sucesso."
            WorkoutPlanView.throw_message(type, text)
            self.home_screen
        else:
            type = "Error"
            text = "Não foi possível atualizar o plano de treino."
            WorkoutPlanView.throw_message(type, text)
    
    def update_workout_plan_screen(self):
        data = self.get_workout_plan_by_email()
        self.__workout_plan_view.update_workout_plan_screen(data)

    @classmethod
    def update_email(self, old_email, new_email):
        try:
            collection = workout_plans_collection()
            collection.update_one(
                {"email": old_email},
                {"$set": {"email": new_email}}
            )
            return True
        except Exception as e:
            print(f"Error updating workout plan email: {e}")
            return False

    def home_screen(self):
        self.__main_controller.main_practitioner_home()
    
    def delete_workout_plan(self, email):
        try:
            WorkoutPlan.delete_workout_plan(email)
            self.home_screen()
        except Exception as e:
            print("Erro:", e)
            text_type = "Error"
            text = "Erro ao deletar o plano de treino."
            WorkoutPlanView.throw_message(text_type, text)

    def get_workout_plan_by_email(self):
        try:
            email = self.__main_controller.get_logged_user()
            collection = workout_plans_collection()
            workout_plan = collection.find_one({"email": email})
            return workout_plan
        except Exception as e:
            return False

    def get_rest_and_reps_range(self, goal, choose):
        match goal:
            case "Strengthening":
                min_rest_value = 120
                max_rest_value = 300
                min_reps_value = 1
                max_reps_value = 6
            case "Weight Loss":
                min_rest_value = 15
                max_rest_value = 45
                min_reps_value = 12
                max_reps_value = 20
            case "Hypertrophy":
                min_rest_value = 30
                max_rest_value = 90
                min_reps_value = 6
                max_reps_value = 12
        rest_time = [min_rest_value, max_rest_value]
        reps_range = [min_reps_value, max_reps_value]
        match choose:
            case "Both":
                return rest_time, reps_range
            case "Reps":
                return reps_range
            case "Rest":
                return rest_time
    