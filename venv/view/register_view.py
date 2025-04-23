from tkinter import Frame, Button, Label, Entry, ttk, StringVar
from controller.users_controller import UserController

class RegisterView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.userController = UserController
    
    def register_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, text="Register", font=("Arial", 25), bg="#212121", fg="white").pack(pady=10)

        Label(frame, text="Nome:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(frame, width=50)
        self.name_entry.pack(pady=5)

        Label(frame, text="Número do telefone:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.cellNumber_entry = Entry(frame, width=50)
        self.cellNumber_entry.pack()

        Label(frame, text="Email:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)

        Label(frame, text="CPF:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.cpf_entry = Entry(frame, width=50)
        self.cpf_entry.pack(pady=5)

        Label(frame, text="Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.senha_entry = Entry(frame, width=50, show="*")
        self.senha_entry.pack()

        Label(frame, text="Tipo de usuário:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.type_var = StringVar()
        type_combobox = ttk.Combobox(
            frame,
            textvariable=self.type_var,
            values=["Praticante", "Personal"],
            state="readonly",
            width=47
        )
        type_combobox.pack(pady=5)

        Button(frame, text="Create Account", font=("Arial", 12), bg="#212121", fg="white",
            width=50, height=2, command=self.create_account).pack(pady=10)

        Button(frame, text="Back", font=("Arial", 12), bg="#212121", fg="white",
            width=50, height=2, command=self.controller.show_main).pack()


    def create_account(self):
        name = self.name_entry.get()
        cellNumber = self.cellNumber_entry.get()
        cpf = self.cpf_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        type = self.type_var.get()
        # Aqui depois chamaremos o model para validar
        print(f"Tentando criar conta com {name} / {cellNumber} / {cpf} / {email} / {senha} / {type}")

        print(self.userController.cadastrar_usuario(name, cpf, cellNumber, email, type, senha))

    def tests(self):
        pass
