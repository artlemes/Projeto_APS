from db.connection import get_database
from bson.objectid import ObjectId
import bcrypt

# Conectando ao banco de dados
db = get_database()
users_collection = db["users"]

class Usuario:
    def __init__(self, nome: str, cpf: str, celular: str, email: str, senha: str, usuario_id=None):
        self._id = ObjectId(usuario_id)
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.senha = senha

    def criptografar_senha(self, senha: str) -> str:
        senha_bytes = senha.encode('utf-8')
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
        return senha_hash.decode('utf-8')

    def verificar_senha(self, senha: str) -> bool:
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))

    def to_dict(self):
        return {
            "_id": str(self._id) if self._id else None,
            "nome": self.nome,
            "cpf": self.cpf,
            "celular": self.celular,
            "email": self.email,
            "senha": self.senha
        }

    @classmethod
    def criar_usuario(self, nome, cpf, celular, email, senha):

        senha = self.criptografar_senha(self, senha)

        usuario = self(nome, cpf, celular, email, senha)

        users_collection.insert_one(usuario.to_dict())

        return 

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
    #Faltou recriptografar a senha, o que causa um erro no login.
    def atualizar_usuario(self, usuario_email, novos_dados: dict):
        if "_id" in novos_dados:
            del novos_dados["_id"]
        resultado = users_collection.update_one(
            {"email": usuario_email},
            {"$set": novos_dados}
        )
        return resultado.modified_count > 0


    @classmethod
    def deletar_usuario(self, email):
        resultado = users_collection.delete_one({"email": email})
        return resultado.deleted_count > 0  # True se o usuário foi deletado

    def autenticar_usuário(email, senha):
        try:
            db = get_database()
            users = db['users']
            user = users.find_one({"email":email})
            print(f'o usuario {user['email']}, esta tentando fazer login')
            if user and bcrypt.checkpw(senha.encode('utf-8'), user["senha"].encode('utf-8')):
                return 1
            return 2
        except Exception as e:
            print("Erro ao fazer login:", e)
            return 3