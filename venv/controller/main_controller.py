from view.main_view import MainView
from controller.practitioner_controller import PractitionerController
from controller.personal_controller import PersonalController
from controller.user_controller import UserController
from controller.workout_plan_controller import WorkoutPlanController
from controller.workout_controller import WorkoutController
from controller.exercise_controller import ExerciseController

class MainController:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.__user_controller = UserController(self.root, self)
        self.__practitioner_controller = PractitionerController(self.root, self)
        self.__personal_controller = PersonalController(self.root, self)
        self.__workout_plan_controller = WorkoutPlanController(self.root, self)
        self.__workout_controller = WorkoutController(self.root, self)
        self.__exercise_controller = ExerciseController(self.root, self)
        self.__main_view = MainView(self.root, self)
        self.main_first_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_first_screen(self):
        self.clear_window()
        self.__main_view.first_screen()

    def main_create_user(self, nome, email, password ,type ):
        try:
            if type == "Personal":
                self.__personal_controller.register_user(nome, email, password)
                return True
            if type == "Praticante":
                self.__practitioner_controller.register_user(nome, email, password)
                return True
        except Exception as e:
            print (e)
            return e

    def main_login(self):
        self.clear_window()
        self.__user_controller.login_screen()
    
    def main_profile(self):
        self.clear_window()
        self.__user_controller.profile_screen()

    def main_logout(self):
        self.clear_window()
        self.__user_controller.logout_screen()

    def main_cadastro(self):
        self.clear_window()
        self.__user_controller.register_screen()
    
    def main_practitioner_home(self):
        self.clear_window()
        self.__practitioner_controller.home_screen()

    def main_personal_home(self):
        self.clear_window()
        self.__personal_controller.home_screen()

    def main_practitioner_home(self):
        self.clear_window()
        workout_plan = self.get_workout_plan()
        if workout_plan and workout_plan != None:
            self.__practitioner_controller.home_screen(workout_plan)
        else:
            workout_plan = {"name": "No data", "sessions": "No data"}
            self.__practitioner_controller.home_screen(workout_plan)
    
    def main_create_workouts(self, days):
        res = self.__workout_controller.create_workouts(days)
        return res

    def main_create_exercise(self, workout):
        self.clear_window()
        res = self.__exercise_controller.create_exercise_screen(workout)
        return res
    
    def main_workout_screen(self, workout):
        self.__workout_controller.workout_screen(workout)

    def main_delete_exercise(self, exercise, workout):
        email = self.get_logged_user()
        self.__exercise_controller.remove_exercise(email, workout, exercise)
    
    def main_update_exercise_screen(self, exercise, workout):
        self.clear_window()
        self.__exercise_controller.update_exercise_screen(exercise, workout)

    def main_workouts_screen(self):
        self.clear_window()
        self.__workout_controller.workouts_screen()

    def main_create_workout_plan(self):
        self.clear_window()
        email = self.get_logged_user()
        self.__workout_plan_controller.create_workout_plan_screen(email)
    
    def get_logged_user(self):
        return self.__user_controller.logged_user
    
    def get_workout_plan(self):
        return self.__workout_plan_controller.get_workout_plan_by_email()
    
    def get_workouts(self):
        workout_plan = self.get_workout_plan()
        workouts = workout_plan["workouts"]
        return workouts
    
    def get_rest_and_reps_range(self, choose):
        workout_plan = self.get_workout_plan()
        res = self.__workout_plan_controller.get_rest_and_reps_range(workout_plan["goal"], choose)
        return res
    
    def main_upadate_workout_plan(self):
        self.clear_window()
        self.__workout_plan_controller.update_workout_plan_screen()

    def main_update_exercise(self, exercise, workout):
        self.__exercise_controller.update_exercise(exercise, workout)