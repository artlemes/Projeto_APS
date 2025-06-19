from view.workout_view import WorkoutView
from model.workout import Workout


class WorkoutController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__workout_view = WorkoutView(self.root, self)
        
    
    def create_workouts(self, days):
        try:
            workout_list = []
            for day in days:
                res = Workout(day, day)
                workout = {
                    "day": res.day,
                    "name": res.name,
                    "exercises": res.exercies
                }
                workout_list.append(workout)
            return workout_list
        except Exception as e: 
            print(e)
    
    def update_workout(self, day, updated_data):
        try:
            email = self.__main_controller.get_logged_user()
            Workout.update_workout(email, day, updated_data)
            type = "Info"
            text = "Treino atualizado com exito!"
            WorkoutView.throw_message(type, text)
            self.workouts_screen()
        except Exception as e:
            print("Erro:", e)
            type = "Error"
            text = "Erro ao atualizar o treino!"
            WorkoutView.throw_message(type, text)

    def workouts_screen(self):
        workouts = self.__main_controller.get_workouts()
        rest_time = self.__main_controller.get_rest_and_reps_range("Rest")
        self.__workout_view.workout_home_view(workouts, rest_time)
    
    def delete_exercise(self, exercise, workout):
        self.__main_controller.main_delete_exercise(exercise, workout)

    def workout_screen(self, workout):
        rest_time = self.__main_controller.get_rest_and_reps_range("Rest")
        self.__workout_view.view_workout(workout, rest_time)
    
    def home_screen(self):
        self.__main_controller.main_practitioner_home()

    def update_exercise(self, exercise, workout):
        self.__main_controller.main_update_exercise(exercise, workout)
    
    def create_exercise(self, workout):
        self.__main_controller.main_create_exercise(workout)

    def update_exercise_screen(self,exercise, workout):
        self.__main_controller.main_update_exercise_screen(exercise,workout)
    
    def get_workout_by_day(self, day): 
        workouts = self.__main_controller.get_workouts()
        for workout in workouts:
            if workout["day"] == day:
                return workout
        return None
    