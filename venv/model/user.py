from db.connection import users_collection
import bcrypt

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    ### Arrumar
    @classmethod
    def update_user(self, logged_user, new_data):
        try:
            collection = users_collection()
            collection.update_one(
                {"email": logged_user},
                {"$set": new_data}
            )
            return True
        except Exception as e:
            print(e)
            raise Exception

    @classmethod
    def delete_user(self, email):
        try:
            collection = users_collection()
            collection.delete_one({"email":email})
            return True 
        except Exception as e:
            print(f"Erro: {e}")

    def auth_user(email, password):
        try:
            collection = users_collection()
            user = collection.find_one({"email": email})
            if not user:
                return "Email não encontrado." 
            # Corrected password field access (removed square brackets)
            if bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                return user
            else:
                return "Senha incorreta."
                
        except Exception as e:
            return "Erro durante a autenticação."
    
    @classmethod
    def password_crypt(password):
        password_bytes = password.encode('utf-8')
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return password_hash.decode('utf-8')
    
    def get_user_by_email(email):
        try:
            collection = users_collection()
            user = collection.find_one({"email": email})
            return user
        except Exception as e:
            return 'Erro durante a busca.'
    