from db.connection import get_database
from bson.objectid import ObjectId
import bcrypt

# Conectando ao banco de dados
db = get_database()
users_collection = db["users"]

class Usuario:
    def __init__(self, nome: str, cpf: str, celular: str, email: str, senha: str, type: str, usuario_id=None):
        self._id = ObjectId(usuario_id) if usuario_id else None
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.type = type
        self.senha = self.criptografar_senha(senha) if senha else None

    def criptografar_senha(self, senha: str) -> str:
        senha_bytes = senha.encode('utf-8')
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
        return senha_hash.decode('utf-8')

    def verificar_senha(self, senha: str) -> bool:
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))

    def to_dict(self):
        user_dict = {
            "nome": self.nome,
            "cpf": self.cpf,
            "celular": self.celular,
            "email": self.email,
            "type": self.type,
            "senha": self.senha
        }
        if self._id:
            user_dict["_id"] = self._id 
        return user_dict


    @classmethod
    def criar_usuario(self, nome, cpf, celular, email, type, senha):
        usuario = self(nome, cpf, celular, email, senha, type)
        resultado = users_collection.insert_one(usuario.to_dict())
        return str(resultado.inserted_id)

    @classmethod
    def buscar_usuario_por_email(self, usuario_email):
        usuario = users_collection.find_one({"email": usuario_email})
        if usuario:
            usuario["email"] = str(usuario["email"])
        return usuario

    @classmethod
    def listar_usuarios(self):
        usuarios = []
        for u in users_collection.find():
            u["_id"] = str(u["_id"])  # Transformar ObjectId em string
            usuarios.append(u)
        return usuarios

    @classmethod
    def atualizar_usuario(self, usuario_id, novos_dados: dict):
        resultado = users_collection.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": novos_dados}
        )
        return resultado.modified_count > 0  # True se algo foi alterado

    @classmethod
    def deletar_usuario(self, usuario_id):
        resultado = users_collection.delete_one({"_id": ObjectId(usuario_id)})
        return resultado.deleted_count > 0  # True se o usuário foi deletado

    # Função de login (exemplo básico)
    def login_usuario(email, senha):
        pass
