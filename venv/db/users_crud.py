from db.connection import get_database
from bson.objectid import ObjectId

db = get_database()
users_collection = db["users"]

def criar_usuario(nome, cpf, celular, email, type, senha):
    usuario = {
        "nome": nome,
        "email": email,
        "cpf":cpf,
        "celular":celular,
        "type":type,
        "senha": senha  #não apliquei hash ainda
    }
    resultado = users_collection.insert_one(usuario)
    return str(resultado.inserted_id)

def login_usuario(self):
    pass

def buscar_usuario_por_id(usuario_id):
    usuario = users_collection.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        usuario["_id"] = str(usuario["_id"]) 
    return usuario

def listar_usuarios():
    usuarios = []
    for u in users_collection.find():
        u["_id"] = str(u["_id"])
        usuarios.append(u)
    return usuarios

def atualizar_usuario(usuario_id, novos_dados: dict):
    resultado = users_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": novos_dados}
    )
    return resultado.modified_count > 0  #true se algo foi alterado

def deletar_usuario(usuario_id):
    resultado = users_collection.delete_one({"_id": ObjectId(usuario_id)})
    return resultado.deleted_count > 0
