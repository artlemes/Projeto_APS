from connection import get_database
from users_crud import criar_usuario, listar_usuarios
from controller.users_controller import UserController

db = get_database()
print("Coleções disponíveis no banco:", db.list_collection_names())

print(UserController.cadastrar_usuario('teste pelo controlador 01', '01293812930', '1234798348', 'controlador@gmail.com', 'personal', 'adkjhfkjadhsfkjahd'))

listaDeUsuarios = listar_usuarios()

for user in listaDeUsuarios:
    print(user['nome'])