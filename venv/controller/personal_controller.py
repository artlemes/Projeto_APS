from view.personal_view import PersonalView
from model.personal import Personal
from db.connection import users_collection


class PersonalController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__personal_view = PersonalView(self.root, self)
        self.__personal = Personal
    
    def register_user(self, nome, email, password):
        try:
            res = self.__personal.register_personal(nome, email, password)
            if res == False:
                raise Exception
            Personal(nome, email, password)
            self.__personal_view.throw_message("Info", "Personal cadastrado com sucesso!")
            self.__main_controller.main_first_screen()
        except Exception as e:
            print(e)
            type = "Error"
            text = "Erro ao cadastrar."
            self.__personal_view.throw_message(type, text)

    def main_profile(self):
        self.__main_controller.main_profile()

    def main_logout(self):
        self.__main_controller.main_logout()

    def home_screen(self):
        self.__personal_view.home_personal_screen()
