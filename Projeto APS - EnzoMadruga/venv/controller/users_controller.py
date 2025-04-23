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
                messagebox.showinfo("Login", "✅ Login bem-sucedido!")
                self.__main_controller.show_home()

            case 2:
                messagebox.showwarning("Login", "❌ Email ou senha incorretos.")
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

    def main_home(self):
        self.__main_controller.show_home()
    
    def show_profile_screen(self):
        self.__profile_view.profile_screen()

    def show_login_screen(self):
        self.__users_view.login_screen()
    
    def show_register_screen(self):
        self.__users_view.register_screen()
    
    @staticmethod
    def listar_usuarios() -> list:
        return Usuario.listar_usuarios()
    
    @staticmethod
    def buscar_usuario_por_id(usuario_id: str) -> dict:

        usuario = Usuario.buscar_usuario_por_id(usuario_id)
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        return usuario
    
    @staticmethod
    def atualizar_usuario(usuario_id: str, nome: str, cpf: str, celular: str, type, email: str, senha: str) -> dict:
        
        usuario_data = Usuario.buscar_usuario_por_id(usuario_id)
        if not usuario_data:
            return {"erro": "Usuário não encontrado."}
        
        # Cria o objeto de usuário com os dados atualizados
        usuario = Usuario.to_dict(nome, cpf, celular, email, type, senha)
        
        # Atualiza o usuário no banco
        Usuario.atualizar_usuario(usuario_id, usuario)
        
        return {"sucesso": "Usuário atualizado com sucesso!"}
    
    @staticmethod
    def excluir_usuario(usuario_id: str) -> dict:

        usuario_data = Usuario.buscar_usuario_por_id(usuario_id)
        if not usuario_data:
            return {"erro": "Usuário não encontrado."}

        Usuario.deletar_usuario(usuario_id)

        return {"sucesso": "Usuário excluído com sucesso!"}


