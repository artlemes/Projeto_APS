from model.users import Usuario
from view.users_view import UsersView
from view.profile_view import ProfileView
from db.connection import get_database
from model.users import Usuario
from tkinter import messagebox

class UserController:
    def __init__(self, root, controller):
        self.root = root
        self.__main_controller = controller
        self.usuario = Usuario
        self.__users_view = UsersView(self.root, self)
        self.__profile_view = ProfileView(self.root, self)
        self.db = get_database()
        self.usuarios_collection = self.db['users']
        self.usuario_logado = None

    @staticmethod
    def cadastrar_usuario(nome: str, cpf: str, celular: str, email: str, type: str, senha: str) -> dict:
        db = get_database()
        usuarios_collection = db['users']
        
        # Verifica se o e-mail já está cadastrado
        if usuarios_collection.find_one({"email": email}):
            return {"erro": "Este e-mail já está cadastrado."}

        Usuario.criar_usuario(nome, cpf, celular, email, type, senha)
        
        return {"sucesso": "Usuário cadastrado com sucesso!"}
    
    def login_user(self, email: str, senha: str):
        res = Usuario.autenticar_usuário(email, senha)
        match res:
            case 1:
                self.usuario_logado = email
                self.__main_controller.show_home(email)

            case 2:
                messagebox.showwarning("Login", "Email ou senha incorretos.")
            case 3:
                messagebox.showerror("Login", "Erro interno durante o login.")
            case _:
                messagebox.showinfo("Login", "Erro inesperado ocorreu.")
    
    def main_screen(self):
        self.__main_controller.show_main()
    
    def logout_user(self):
        self.usuario_logado = None
        self.main_screen()
    
    def show_logout_screen(self):
        self.__users_view.logout_confirmation_screen()

    def main_home(self, email_atual):
        self.__main_controller.show_home(email_atual)
    
    def show_profile_screen(self, email_atual):
        self.__profile_view.profile_screen(email_atual)

    def show_login_screen(self):
        self.__users_view.login_screen()
    
    def show_register_screen(self):
        self.__users_view.register_screen()
    
    @staticmethod
    def listar_usuarios() -> list:
        return Usuario.listar_usuarios()
    
    @staticmethod
    def buscar_usuario_por_email(usuario_email: str) -> dict:

        usuario = Usuario.buscar_usuario_por_email(usuario_email)
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        return usuario
    
    @staticmethod
    def atualizar_usuario(email_antigo, nome: str, cpf, celular, email: str, tipo, senha: str) -> dict:
        
        usuario_antigo = Usuario.buscar_usuario_por_email(email_antigo)
        if not usuario_antigo:
            return {"erro": "Usuário não encontrado."}
        
        # Cria o objeto de usuário com os dados atualizados
        usuario = Usuario(nome, cpf, celular, email, senha, tipo)

        usuario_dicionario = Usuario.to_dict(usuario)
        
        # Atualiza o usuário no banco
        Usuario.atualizar_usuario(email_antigo, usuario_dicionario)
        
        return {"sucesso": "Usuário atualizado com sucesso!"}
    
    @staticmethod
    def excluir_usuario(email: str) -> dict:

        usuario_data = Usuario.buscar_usuario_por_email(email)
        if not usuario_data:
            return {"erro": "Usuário não encontrado."}

        Usuario.deletar_usuario(email)

        return {"sucesso": "Usuário excluído com sucesso!"}


