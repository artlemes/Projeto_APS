from tkinter import Frame, Button, Label, Entry, StringVar, ttk, messagebox, Toplevel
import re

class UserView:
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

        Button(frame, text="Entrar", font=("Arial", 12), bg="#212121", fg="white", 
            width=50, height=2, command=self.login).pack(pady=10)
        Button(frame, text="Back", font=("Arial", 12), bg="#212121", fg="white",
            width=50, height=2, command=self.__user_controller.first_screen).pack()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.__user_controller.login_user(email, senha)  # <-- Usa a instância real

    def logout_confirmation_screen(self, type):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, text="Deseja realmente sair?", bg="#212121", fg="white",
                font=("Arial", 20, "bold")).pack(pady=40)

        Button(frame, text="Logout",command=self.__user_controller.logout_user, width=30,height=2,  bg="#616161", fg="black", font=("Arial", 12, "bold")).pack(pady=10)
        Button(frame, text="Cancelar",command=lambda: self.__user_controller.home_screen(type), width=30,height=2,  bg="#616161", fg="black", font=("Arial", 12, "bold")).pack(pady=10)

    def register_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, text="Register", font=("Arial", 25), bg="#212121", fg="white").pack(pady=10)

        # Name field
        Label(frame, text="Nome:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(frame, width=50)
        self.name_entry.pack(pady=5)
        self.name_error = Label(frame, text="", fg="red", bg="#212121")
        self.name_error.pack()

        # Email field with validation
        Label(frame, text="Email:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)
        self.email_error = Label(frame, text="", fg="red", bg="#212121")
        self.email_error.pack()
        
        # Password field
        Label(frame, text="Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.senha_entry = Entry(frame, width=50, show="*")
        self.senha_entry.pack(pady=5)
        self.password_error = Label(frame, text="", fg="red", bg="#212121")
        self.password_error.pack()

        # User type
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
        self.type_error = Label(frame, text="", fg="red", bg="#212121")
        self.type_error.pack()
        
        Button(frame, text="Create Account", font=("Arial", 12), bg="#212121", fg="white",
            width=50, height=2, command=self.validate_and_register).pack(pady=10)

        Button(frame, text="Back", font=("Arial", 12), bg="#212121", fg="white",
            width=50, height=2, command=self.__user_controller.first_screen).pack()

    def validate_and_register(self):
        """Validate all fields before registration"""
        # Reset error messages
        self.name_error.config(text="")
        self.email_error.config(text="")
        self.password_error.config(text="")
        self.type_error.config(text="")
        
        # Get all values
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.senha_entry.get().strip()
        type = self.type_var.get()
        
        # Validate each field
        is_valid = True
        
        if not name:
            self.name_error.config(text="Name is required")
            is_valid = False
        
        if not email:
            self.email_error.config(text="Email is required")
            is_valid = False
        elif not self.is_valid_email(email):
            self.email_error.config(text="Invalid email format")
            is_valid = False
        
        if not password:
            self.password_error.config(text="Password is required")
            is_valid = False
        
        if not type:
            self.type_error.config(text="User type must be selected")
            is_valid = False
        
        # Only proceed if all validations pass
        if is_valid:
            self.perform_registration(name, email, password, type)
        else:
            messagebox.showerror("Error", "Há campos incorretos!")

    def is_valid_email(self, email):
        """Validate email format using regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def perform_registration(self, name, email, password, type):
        try:
            self.__user_controller.register_user(name, email, password, type)
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")

    @staticmethod
    def throw_message(type, text):
        match type:
            case "Info":
                messagebox.showinfo(type, text)
            case "Error":
                messagebox.showerror(type, text)
            case "warning":
                messagebox.showwarning(type, text)
 
    def profile_screen(self):

        user_atual = self.__user_controller.get_user_by_email() 

        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True, fill="both")

        Label(frame, text="Profile", font=("Arial", 25), bg="#212121", fg="white").pack(pady=20)

        Label(frame, text=user_atual['name'], font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(frame, width=50)
        self.name_entry.pack(pady=5)

        Label(frame, text=user_atual['email'], font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)

        Button(frame, text="Change Password", font=("Arial", 12), bg="#555555", fg="white",
               width=50, height=2, command=lambda:self.change_password(user_atual)).pack(pady=10)

        Button(frame, text="Delete Account", font=("Arial", 12), bg="#a83232", fg="white",
               width=50, height=2, command=lambda:self.delete_account(user_atual)).pack(pady=5)

        Button(frame, text="Save", font=("Arial", 12), bg="#4CAF50",
               width=50, height=2, command=lambda:self.save_profile(user_atual)).pack(pady=10)

        Button(frame, text="Cancel", font=("Arial", 12), bg="#dcdcdc",
               width=50, height=2, command=lambda: self.__user_controller.home_screen(user_atual["type"])).pack()

    def change_password(self, current_user):
        pw_window = Toplevel(self.root)
        pw_window.title("Change Password")
        pw_window.configure(bg="#212121")
        pw_window.geometry("350x200")
        pw_window.grab_set()  # impede interação com a janela principal enquanto essa estiver aberta
        
        frame = Frame(pw_window, bg="#212121")
        frame.pack(expand=True, fill="both")

        # Adicionando os campos de senha
        Label(pw_window, text="Nova Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=(15, 5))
        new_pw_entry = Entry(pw_window, show="*", width=35)
        new_pw_entry.pack()

        Label(pw_window, text="Confirmar Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=(10, 5))
        confirm_pw_entry = Entry(pw_window, show="*", width=35)
        confirm_pw_entry.pack()

        # Criando o botão na parte inferior, com uma largura menor
        button_frame = Frame(pw_window, bg="#212121")
        button_frame.pack(side="bottom", fill="x", padx=10, pady=10)  # Coloca o botão no fundo e ajusta margens
        Button(button_frame, text="Save new password", font=("Arial", 12), bg="#dcdcdc",
            width=20, height=2, command=lambda: self.save_new_password(current_user, pw_window, new_pw_entry, confirm_pw_entry)).pack()

    def save_new_password(self, current_user, pw_window, new_pw, confirm_pw):
        new_pw = new_pw.get()
        confirm_pw = confirm_pw.get()

        if new_pw != confirm_pw:
            messagebox.showerror("Erro", "As senhas não coincidem.")
        elif not new_pw:
            messagebox.showerror("Erro", "A senha não pode ser vazia.")
        else:
            sucesso = self.__user_controller.update_user(
                current_user['name'],
                current_user['email'],
                new_pw
            )

            if sucesso:
                pw_window.destroy()

    def delete_account(self, current_user):
        result = messagebox.askyesno("Delete Account", "Tem certeza que deseja deletar sua conta?")
        if result:
            self.__user_controller.delete_user(current_user['email'])
        
    def save_profile(self, current_user):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if email and not self.is_valid_email(email):
            messagebox.showerror("Erro na edição", 'Formato de e-mail inválido.')
            return
        
        # Only check email if it's different from current email
        if email and email != current_user["email"]:
            check_email = self.__user_controller.check_email(email)
            if not check_email:
                messagebox.showerror("Erro na edição", 'E-mail já cadastrado.')
                return

        if not email:
            email = current_user["email"]
        if not name:
            name = current_user["name"]

        self.__user_controller.update_user(name, email, current_user['password'])
        self.__user_controller.home_screen(current_user['type'])