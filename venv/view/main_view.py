from tkinter import Frame, Button, Label, Tk
import tkinter as tk
class MainView:
   def __init__(self, root, controller):
        self.root = root
        self.__controller = controller

   def first_screen(self):
        frame = Frame(self.root, bg="#212121")
        frame.pack(expand=True)

        Label(frame, bg="#212121", text="Bem-vindo ao FitTrack", fg="white", font=("Arial", 25)).pack(pady=20)

        Button(frame, text="Login", font=("Arial", 12), bg="#212121",fg="white", activebackground="#616161", width=50, height=2, command=self.__controller.main_login).pack(pady=10)
        Button(frame, text="Cadastro", font=("Arial", 12), bg="#212121",fg="white", activebackground="#616161", width=50,height=2, command=self.__controller.main_cadastro).pack(pady=10)

   def home_screen(self, email_atual):
         
      top_frame = Frame(self.root, bg="#BDBDBD", height=50)
      top_frame.pack(fill="x", side="top")

      profile_btn = Button(top_frame, text="Profile", command=lambda: self.__controller.main_profile(email_atual), width=10, bg="#9E9E9E", fg="white", font=("Arial", 10, "bold"))
      profile_btn.pack(side="left", padx=10, pady=10)

      logout_btn = Button(top_frame, text="Logout",command=self.__controller.main_logout, width=10, bg="#D32F2F", fg="white", font=("Arial", 10, "bold"))
      logout_btn.pack(side="right", padx=10, pady=10)

      # Container principal
      main_frame = Frame(self.root, bg="#424242")
      main_frame.pack(expand=True, fill="both", padx=20, pady=20)

      # Esquerda
      left_frame = Frame(main_frame, bg="#616161")
      left_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

      create_plan_btn = Button(left_frame, text="Create new\nworkout plan", font=("Arial", 16, "bold"), bg="#757575", fg="white", height=6, width=20)
      create_plan_btn.pack(pady=20)

      create_exercise_btn = Button(left_frame, text="Create new\nexercise", font=("Arial", 16, "bold"), bg="#757575", fg="white", height=6, width=20)
      create_exercise_btn.pack(pady=20)

      # Direita
      right_frame = Frame(main_frame, bg="#616161")
      right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

      info_label = Label(right_frame, text="My Workout Plan\nRemaining sessions:  12/40", font=("Arial", 14, "bold"), bg="#616161", fg="white", justify="left")
      info_label.pack(anchor="w", pady=(20, 10), padx=20)

      btn_width = 40
      btn_pad_y = 15

      workouts_btn = Button(right_frame, text="Workouts", font=("Arial", 14, "bold"), bg="#E0E0E0", height=2)
      workouts_btn.pack(pady=btn_pad_y)

      edit_plan_btn = Button(right_frame, text="Edit Workout Plan", font=("Arial", 14, "bold"), bg="#E0E0E0", height=2)
      edit_plan_btn.pack(pady=btn_pad_y)

      dashboard_btn = Button(right_frame, text="View Dashboard", font=("Arial", 14, "bold"), bg="#E0E0E0", height=2)
      dashboard_btn.pack(pady=btn_pad_y)