from model.users import Usuario
from db.connection import get_database
from model.users import Usuario
from bson import ObjectId

class UserController:
    
    @staticmethod
    def cadastrar_usuario(nome: str, cpf: str, celular: str, email: str, type: str, senha: str) -> dict:
        db = get_database()
        usuarios_collection = db['users']
        
        # Verifica se o e-mail já está cadastrado
        if usuarios_collection.find_one({"email": email}):
            return {"erro": "Este e-mail já está cadastrado."}

        Usuario.criar_usuario(nome, cpf, celular, email, type, senha)
        
        return {"sucesso": "Usuário cadastrado com sucesso!"}
    
    @staticmethod
    def login_usuario(email: str, senha: str) -> dict:
        return Usuario.login_usuario(email, senha)
    
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
    def atualizar_usuario(self, nome, cpf, celular, email, type, senha) -> dict:

        usuario = self.buscar_usuario_por_email(email)
        
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        
        # Cria o objeto de usuário com os dados atualizados
        novo_usuario = Usuario.to_dict(nome, cpf, celular, email, type, senha)
        
        # Atualiza o usuário no banco
        Usuario.atualizar_usuario(usuario['_id'], novo_usuario)
        
        return {"sucesso": "Usuário atualizado com sucesso!"}
    
    @staticmethod
    def excluir_usuario(usuario_id: str) -> dict:

        usuario_data = Usuario.buscar_usuario_por_id(usuario_id)
        if not usuario_data:
            return {"erro": "Usuário não encontrado."}

        Usuario.deletar_usuario(usuario_id)

        return {"sucesso": "Usuário excluído com sucesso!"}
