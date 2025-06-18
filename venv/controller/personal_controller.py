from view.personal_view import PersonalView
from model.personal import Personal
from db.connection import users_collection


class PersonalController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__personal_view = PersonalView(self.root, self)
        self.__personal = Personal

    def main_profile(self):
        self.__main_controller.main_profile()

    def main_logout(self):
        self.__main_controller.main_logout()

    def home_screen(self):
        self.__personal_view.home_personal_screen()
