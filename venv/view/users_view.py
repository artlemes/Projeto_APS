from tkinter import Frame, Button, Label, Entry, StringVar, ttk, messagebox
import re

class UsersView:
    def __init__(self, root, user_controller):
        self.root = root
        self.__user_controller = user_controller

    def login_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, text="Login", font=("Arial", 25), bg="#212121", fg="white").pack(pady=10)

        Label(frame, text="Email:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)

        Label(frame, text="Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.senha_entry = Entry(frame, width=50, show="*")
        self.senha_entry.pack()

        Button(frame, text="Entrar", font=("Arial", 12), bg="#212121", fg="white", width=50, height=2, command=self.login).pack(pady=10)
        Button(frame, text="Voltar", font=("Arial", 12), bg="#212121", fg="white", width=50, height=2, command=self.__user_controller.main_screen).pack()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.__user_controller.login_user(email, senha)  # <-- Usa a instância real
        print(f"Tentando login com {email} / {senha}")

    def logout_confirmation_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, text="Deseja realmente sair?", bg="#212121", fg="white",
                font=("Arial", 20, "bold")).pack(pady=40)

        # Botões
        btn_style = {"font": ("Arial", 12, "bold"), "bg": "#212121", "fg": "white",
                    "activebackground": "#616161", "width": 30, "height": 2}

        Button(frame, text="Sim, sair", command=self.__user_controller.logout_user, **btn_style).pack(pady=10)
        Button(frame, text="Cancelar", command=self.__user_controller.main_home, **btn_style).pack(pady=10)

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
            width=50, height=2, command=self.__user_controller.main_screen).pack()


    def create_account(self):
        name = self.name_entry.get()
        cellNumber = self.cellNumber_entry.get()
        cpf = self.cpf_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        type = self.type_var.get()

        if not name or not cellNumber or not cpf or not email or not senha or not type:
            messagebox.showerror("Erro no registro", 'É necessário preencher todos os campos!')
            return

        erros = self.validacoes_registro(name, cellNumber, cpf, email, senha)

        if not erros:

            print(self.__user_controller.cadastrar_usuario(name, cpf, cellNumber, email, type, senha))
            self.__user_controller.main_screen()

        else: 
            mensagem = '\n'.join(f"{campo}: {mensagem}" for campo, mensagem in erros.items())
            messagebox.showerror("Erros de Validação", mensagem)

    def validacoes_registro(self, name, cellNumber, cpf, email, senha):
        erros = {}

        # Nome: pelo menos uma letra (ignorando espaços)
        if not name or not re.search(r'[A-Za-z]', name):
            erros['name'] = 'Nome deve conter pelo menos uma letra.'

        # Celular: exatamente 11 dígitos, sem pontos ou outros caracteres
        if not re.fullmatch(r'\d{11}', cellNumber):
            erros['celular'] = 'Número de celular deve conter exatamente 11 dígitos (somente números).'

        # CPF: exatamente 11 dígitos, sem pontos ou traços
        if not re.fullmatch(r'\d{11}', cpf):
            erros['cpf'] = 'CPF deve conter exatamente 11 dígitos (somente números).'

        # Email: deve conter pelo menos um "@"
        if '@' not in email:
            erros['email'] = 'Email deve conter pelo menos um "@".'

        # Senha: verificar se não está vazia
        if not senha:
            erros['senha'] = 'Senha é obrigatória.'

        return erros

