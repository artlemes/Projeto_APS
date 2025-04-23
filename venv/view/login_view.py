from tkinter import Frame, Button, Label, Entry

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
    
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

        Button(frame, text="Entrar", font=("Arial", 12),bg="#212121",fg="white", width=50, height=2, command=self.login).pack(pady=10)
        Button(frame, text="Voltar", font=("Arial", 12), bg="#212121",fg="white", width=50, height=2, command=self.controller.show_main).pack()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        # Aqui depois chamaremos o model para validar
        print(f"Tentando login com {email} / {senha}")
