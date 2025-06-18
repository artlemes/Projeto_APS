from view.user_view import UserView
from db.connection import users_collection
from model.user import User

class UserController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__users_view = UserView(self.root, self)
        self.logged_user = None
        self.logged_user_type = None

    def register_user(self, nome, email, password, type):
        try:
            check_email = self.check_email(email)
            if not check_email:
                text_type = "Error"
                text = "Email já cadastrado!"
                UserView.throw_message(text_type, text)
                return
            self.__main_controller.main_create_user(nome, email, password, type)
        except Exception as e:
            print(e)
            text_type = "Error"
            text = "Erro ao cadastrar o usuário."
            UserView.throw_message(text_type, text)
    
    def login_user(self, email, senha):
        try:
            res = User.auth_user(email, senha)
            if isinstance(res, dict):
                self.logged_user = email
                self.logged_user_type = res["type"]
                type = "Info"
                text = "Login bem sucedido!"
                UserView.throw_message(type, text)
                self.home_screen(self.logged_user_type)
            else: raise Exception
        except:
            type = "Error"
            text = f"{res}"
            UserView.throw_message(type, res)


    def home_screen(self, type):
        if type == "Praticante":
            self.__main_controller.main_practitioner_home()
        if type == "Personal":
            self.__main_controller.main_personal_home()
    
    def logout_screen(self):
        self.__users_view.logout_confirmation_screen(self.logged_user_type)
    
    def logout_user(self):
        self.usuario_logado = None
        self.first_screen()

    def first_screen(self):
        self.__main_controller.main_first_screen()
    
    def profile_screen(self):
        self.__users_view.profile_screen()

    def login_screen(self):
        self.__users_view.login_screen()
    
    def register_screen(self):
        self.__users_view.register_screen()
    
    def check_email(self, email):
        collection = users_collection()
        if collection.find_one({"email": email}):
            return False
        else: 
            return True
    
    def update_user(self, name, email, password):
        new_password = password
        if len(password) < 50:
            new_password = User.password_crypt(password)
        novos_dados = {
            "name": name,
            "email": email,
            "password": new_password
        }
        sucesso = User.update_user(self.logged_user, novos_dados)
        if sucesso:
            self.logged_user = email
            type = "Info"
            text = "Perfil atualizado com sucesso."
            UserView.throw_message(type, text)
            return True
        else:
            type = "Error"
            text = "Não foi possível atualizar o perfil."
            UserView.throw_message(type, text)
    
    
    
    def delete_user(self, email):
        try:
            User.delete_user(email)
            self.first_screen()
        except Exception as e:
            print("Erro:", e)
    
    def get_user_by_email(self):
        usuario = User.get_user_by_email(self.logged_user)
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        return usuario
    
    def get_user_type(self):
        user = self.get_user_by_email(self.logged_user)
        return user["type"]