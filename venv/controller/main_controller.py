from view.main_view import MainView

from controller.users_controller import UserController

class MainController:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.__user_controller = UserController(self.root, self)
        self.__main_view = MainView(self.root, self)
        self.show_main()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main(self):
        self.clear_window()
        self.__main_view.first_screen()

    def main_login(self):
        self.clear_window()
        self.__user_controller.show_login_screen()
    
    def main_profile(self, email_atual):
        self.clear_window()
        self.__user_controller.show_profile_screen(email_atual)

    def main_logout(self):
        self.clear_window()
        self.__user_controller.show_logout_screen()

    def main_cadastro(self):
        self.clear_window()
        self.__user_controller.show_register_screen()
    
    def show_home(self, email_atual):
        self.clear_window()
        self.__main_view.home_screen(email_atual)
