from model.user import User
from db.connection import users_collection
import bcrypt

class Personal(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.user_type = "Personal"
        self.password = password
    
    @classmethod
    def register_personal(self, nome, email, password):
        try:
            collection = users_collection()
            new_pass = self.password_crypt(password)
            usuario = {
                "name": nome,
                "email": email,
                "password": new_pass,
                "type": "Personal",
            }
            collection.insert_one(usuario)
            return True
        except:
            return Exception

    def password_crypt(password):
        password_bytes = password.encode('utf-8')
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return password_hash.decode('utf-8')