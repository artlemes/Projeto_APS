from db.connection import get_database
from bson.objectid import ObjectId
import bcrypt
from users import Usuario

# Conectando ao banco de dados
db = get_database()
pers_collection = db["personal"]

class Personal(Usuario):
    def __init__(self, nome: str, cpf: str, celular: str, email: str, senha: str, usuario_id=None):
        super().__init__(nome, cpf, celular, email, senha, usuario_id)
        self.trainee = []
        self.traineeToAccept = []

    def criar_personal(self, nome, cpf, celular, email, senha):

        senha = super().criptografar_senha(self, senha)

        personal = self(nome, cpf, celular, email, senha)

        pers_collection.insert_one(super().to_dict(personal))

        return 

    @classmethod
    def buscar_personal_por_email(self, personal_email):
        personal = pers_collection.find_one({"email": personal_email})
        if personal:
            personal["email"] = str(personal["email"])
        return personal

    @classmethod
    def listar_personais(self):
        personais = []
        for u in pers_collection.find():
            u["_id"] = str(u["_id"])  # Transformar ObjectId em string
            personais.append(u)
        return personais

    @classmethod
    #Faltou recriptografar a senha, o que causa um erro no login.
    def atualizar_personal(self, personal_email, novos_dados: dict):
        if "_id" in novos_dados:
            del novos_dados["_id"]
        resultado = pers_collection.update_one(
            {"email": personal_email},
            {"$set": novos_dados}
        )
        return resultado.modified_count > 0


    @classmethod
    def deletar_personal(self, email):
        resultado = pers_collection.delete_one({"email": email})
        return resultado.deleted_count > 0  # True se o personal foi deletado

    def autenticar_personal(email, senha):
        try:
            db = get_database()
            personais = db['practitioner']
            personal = personais.find_one({"email":email})
            print(f'o personal {personal['email']}, esta tentando fazer login')
            if personal and bcrypt.checkpw(senha.encode('utf-8'), personal["senha"].encode('utf-8')):
                return 1
            return 2
        except Exception as e:
            print("Erro ao fazer login:", e)
            return 3