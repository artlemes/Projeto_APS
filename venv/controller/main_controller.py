from view.main_view import MainView
from view.login_view import LoginView
from view.register_view import RegisterView
from controller.users_controller import UserController
from view.profile_view import ProfileView

class MainController:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.show_main()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main(self):
        self.clear_window()
        self.current_view = MainView(self.root, self)
        self.current_view.first_screen()
    
    def show_profile(self):
        self.clear_window()
        self.current_view = ProfileView(self.root, self)
        self.current_view.profile_screen()

    def show_login(self):
        self.clear_window()
        self.current_view = LoginView(self.root, self)
        self.current_view.login_screen()

    def show_cadastro(self):
        self.clear_window()
        self.current_view = RegisterView(self.root, self)
        self.current_view.register_screen()
