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

    def register_user(self, nome, email, password):
        try:
            res = self.__practitioner.register_practitioner(nome, email, password)
            if res == False:
                raise Exception
            Practitioner(nome, email, password)
            self.__practitioner_view.throw_message("Info", "Praticante cadastrado com sucesso!")
            self.__main_controller.main_first_screen()
        except Exception as e:
            print(e)
            type = "Error"
            text = "Erro ao cadastrar."
            self.__practitioner_view.throw_message(type, text)

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
        workout_plan = self.__main_controller.get_workout_plan()

        if not workout_plan:
            self.__practitioner_view.throw_message(
                "Error", 
                "Nenhum plano de treino encontrado."
            )
            return
        self.__main_controller.main_upadate_workout_plan()