from view.practitioner_view import PractitionerView 
from model.practitioner import Practitioner
from db.connection import users_collection

class PractitionerController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__practitioner_view = PractitionerView(self.root, self)
        self.__practitioner = Practitioner
        self.logged_user = None

    def main_profile(self):
        self.__main_controller.main_profile()

    def main_logout(self):
        self.__main_controller.main_logout()
    
    def home_screen(self, workout_plan):
        self.__practitioner_view.home_practitioner_screen(workout_plan)
        
    def workouts_screen(self):
        self.__main_controller.main_workouts_screen()
            
    def create_workout_plan(self):
        self.__main_controller.main_create_workout_plan()
    
    def update_workout_plan(self):
        self.__main_controller.main_upadate_workout_plan()