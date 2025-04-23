from tkinter import Frame, Button, Label, Entry, Tk
from tkinter import messagebox
from controller.users_controller import UserController


class ProfileView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.userController = UserController

    def profile_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True, fill="both")

        Label(frame, text="Profile", font=("Arial", 25), bg="#212121", fg="white").pack(pady=20)

        Label(frame, text="Nome:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(frame, width=50)
        self.name_entry.pack(pady=5)

        Label(frame, text="E-mail:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)

        Button(frame, text="Change Password", font=("Arial", 12), bg="#555555", fg="white",
               width=50, height=2, command=self.change_password).pack(pady=10)

        Button(frame, text="Delete Account", font=("Arial", 12), bg="#a83232", fg="white",
               width=50, height=2, command=self.delete_account).pack(pady=5)

        Button(frame, text="Save", font=("Arial", 12), bg="#dcdcdc",
               width=50, height=2, command=self.save_profile).pack(pady=10)

        Button(frame, text="Cancel", font=("Arial", 12), bg="#dcdcdc",
               width=50, height=2, command=self.controller.show_main).pack()

    def change_password(self):
        pw_window = Tk.Toplevel(self.root)
        pw_window.title("Change Password")
        pw_window.configure(bg="#212121")
        pw_window.geometry("350x200")
        pw_window.grab_set()  # impede interação com a janela principal enquanto essa estiver aberta

        Label(pw_window, text="Nova Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=(15, 5))
        new_pw_entry = Entry(pw_window, show="*", width=35)
        new_pw_entry.pack()

        Label(pw_window, text="Confirmar Senha:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=(10, 5))
        confirm_pw_entry = Entry(pw_window, show="*", width=35)
        confirm_pw_entry.pack()

    def save_new_password():
        new_pw = new_pw_entry.get()
        confirm_pw = confirm_pw_entry.get()
        if new_pw != confirm_pw:
            messagebox.showerror("Erro", "As senhas não coincidem.")
        elif not new_pw:
            messagebox.showerror("Erro", "A senha não pode ser vazia.")
        else:
            # Aqui você pode chamar o controller para salvar a senha
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
            pw_window.destroy()

        Button(pw_window, text="Salvar", font=("Arial", 12), bg="#dcdcdc", width=25, height=1, command=save_new_password).pack(pady=20)

    def delete_account(self):
        result = messagebox.askyesno("Delete Account", "Tem certeza que deseja deletar sua conta?")
        if result:
            messagebox.showinfo("Deleted", "Sua conta foi deletada.")

    def save_new_password(self):
        pass

    def save_profile(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        usuario_atualizado = UserController.buscar_usuario_por_email(email)
    

