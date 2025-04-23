from tkinter import Frame, Button, Label
class MainView:
     def __init__(self, root, controller):
        self.root = root
        self.controller = controller

     def first_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, bg="#212121", text="Bem-vindo ao FitTrack", fg="white", font=("Arial", 25)).pack(pady=20)

        Button(frame, text="Login", font=("Arial", 12), bg="#212121",fg="white", activebackground="#616161", width=50, height=2, command=self.controller.show_login).pack(pady=10)
        Button(frame, text="Cadastro", font=("Arial", 12), bg="#212121",fg="white", activebackground="#616161", width=50,height=2, command=self.controller.show_cadastro).pack(pady=10)
        