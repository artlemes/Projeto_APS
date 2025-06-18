from model.user import User

class Personal(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.user_type = "Personal"
        self.password = password
        
