from db.connection import get_database
from bson.objectid import ObjectId
import bcrypt
from users import pratic
from workoutPlan import WorkoutPlan
from personal import Personal

# Conectando ao banco de dados
db = get_database()
pract_collection = db["practitioner"]

class Practitioner(pratic):
    def __init__(self, nome: str, cpf: str, celular: str, email: str, senha: str, pratic_id=None):
        super().__init__(nome, cpf, celular, email, senha, pratic_id)
        self.workoutPlan = WorkoutPlan()
        self.personalTrainer = Personal()

    def criar_pratic(self, nome, cpf, celular, email, senha):

        senha = super().criptografar_senha(self, senha)

        pratic = self(nome, cpf, celular, email, senha)

        pract_collection.insert_one(super().to_dict(pratic))

        return 

    @classmethod
    def buscar_pratic_por_email(self, pratic_email):
        pratic = pract_collection.find_one({"email": pratic_email})
        if pratic:
            pratic["email"] = str(pratic["email"])
        return pratic

    @classmethod
    def listar_praticantes(self):
        pratics = []
        for u in pract_collection.find():
            u["_id"] = str(u["_id"])  # Transformar ObjectId em string
            pratics.append(u)
        return pratics

    @classmethod
    #Faltou recriptografar a senha, o que causa um erro no login.
    def atualizar_pratic(self, pratic_email, novos_dados: dict):
        if "_id" in novos_dados:
            del novos_dados["_id"]
        resultado = pract_collection.update_one(
            {"email": pratic_email},
            {"$set": novos_dados}
        )
        return resultado.modified_count > 0


    @classmethod
    def deletar_pratic(self, email):
        resultado = pract_collection.delete_one({"email": email})
        return resultado.deleted_count > 0  # True se o pratic foi deletado

    def autenticar_pratic(email, senha):
        try:
            db = get_database()
            praticantes = db['practitioner']
            praticante = praticantes.find_one({"email":email})
            print(f'o pratic {praticante['email']}, esta tentando fazer login')
            if praticante and bcrypt.checkpw(senha.encode('utf-8'), praticante["senha"].encode('utf-8')):
                return 1
            return 2
        except Exception as e:
            print("Erro ao fazer login:", e)
            return 3