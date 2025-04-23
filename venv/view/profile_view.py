from tkinter import Frame, Button, Label, Entry, Tk, Toplevel
from tkinter import messagebox

class ProfileView:
    def __init__(self, root, controller):
        self.root = root
        self.__user_controller = controller
        
    def profile_screen(self, email_atual):

        user_atual = self.__user_controller.buscar_usuario_por_email(email_atual) 

        print("usuario atualizado: ", user_atual)

        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True, fill="both")

        Label(frame, text="Profile", font=("Arial", 25), bg="#212121", fg="white").pack(pady=20)

        Label(frame, text=user_atual['nome'], font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(frame, width=50)
        self.name_entry.pack(pady=5)

        Label(frame, text=user_atual['email'], font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.email_entry = Entry(frame, width=50)
        self.email_entry.pack(pady=5)

        Button(frame, text="Change Password", font=("Arial", 12), bg="#555555", fg="white",
               width=50, height=2, command=lambda:self.change_password(user_atual)).pack(pady=10)

        Button(frame, text="Delete Account", font=("Arial", 12), bg="#a83232", fg="white",
               width=50, height=2, command=lambda:self.delete_account(user_atual)).pack(pady=5)

        Button(frame, text="Save", font=("Arial", 12), bg="#dcdcdc",
               width=50, height=2, command=lambda:self.save_profile(user_atual)).pack(pady=10)

        Button(frame, text="Cancel", font=("Arial", 12), bg="#dcdcdc",
               width=50, height=2, command=lambda: self.__user_controller.main_home(user_atual['email'])).pack()

    def change_password(self, user_atual):
        pw_window = Toplevel(self.root)
        pw_window.title("Change Password")
        pw_window.configure(bg="#212121")
        pw_window.geometry("350x200")
        pw_window.grab_set()  # impede interação com a janela principal enquanto essa estiver aberta
        
        # Criando o frame dentro da janela de senha
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
            width=20, height=2, command=lambda: self.save_new_password(user_atual, pw_window, new_pw_entry, confirm_pw_entry)).pack()


    #Só isso que ta faltando!!!!
    def save_new_password(self, user_atual, pw_window, new_pw, confirm_pw):
        new_pw = new_pw.get()
        confirm_pw = confirm_pw.get()

        if new_pw != confirm_pw:
            messagebox.showerror("Erro", "As senhas não coincidem.")
        elif not new_pw:
            messagebox.showerror("Erro", "A senha não pode ser vazia.")
        else:
            # Cria nova instância de usuário com a nova senha e dados antigos
            usuario = self.__user_controller.usuario(
                nome=user_atual['nome'],
                cpf=user_atual['cpf'],
                celular=user_atual['celular'],
                email=user_atual['email'],
                senha=new_pw,  # nova senha será criptografada no __init__
                type=user_atual['type'],
                usuario_id=user_atual.get('_id')
            )

            sucesso = self.__user_controller.atualizar_usuario(
                usuario.email, 
                usuario.nome,
                usuario.cpf,
                usuario.celular,
                usuario.email,
                usuario.type,
                usuario.senha  # senha já está criptografada corretamente
            )

            if sucesso:
                messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
                pw_window.destroy()
            else:
                messagebox.showerror("Erro", "Erro ao alterar a senha.")



    #funcionando perfect
    def delete_account(self, user_atual):
        result = messagebox.askyesno("Delete Account", "Tem certeza que deseja deletar sua conta?")
        if result:
            self.__user_controller.excluir_usuario(user_atual['email'])
            self.__user_controller.main_screen()

    #funcionando perfect
    def save_profile(self, user_atual):
        name = self.name_entry.get()
        email = self.email_entry.get()

        print("email do usuario antes da atualização: ", user_atual['email'])

        if name and not email: 
            print(self.__user_controller.atualizar_usuario(user_atual['email'], name, user_atual['cpf'], user_atual['celular'], user_atual['email'], user_atual['type'], user_atual['senha']))
            self.__user_controller.main_home(user_atual['email'])      
        if email and not name: 
            self.__user_controller.atualizar_usuario(user_atual['email'], user_atual['nome'], user_atual['cpf'], user_atual['celular'], email, user_atual['type'], user_atual['senha'])
            self.__user_controller.main_home(email)      
        if email and name:
            self.__user_controller.atualizar_usuario(user_atual['email'], name, user_atual['cpf'], user_atual['celular'], email, user_atual['type'], user_atual['senha'])
            self.__user_controller.main_home(email)

