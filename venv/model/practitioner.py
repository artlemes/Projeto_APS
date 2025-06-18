from model.user import User

class Practitioner(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.user_type = "Praticante"
        self.password = password
    
    
