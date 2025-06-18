from tkinter import Frame, Button, Label, Tk

class PractitionerView:
    def __init__(self, root, practitioner_controller):
        self.root = root
        self.__practitioner_controller = practitioner_controller

    def home_practitioner_screen(self, workout_plan):
         
        top_frame = Frame(self.root, bg="#BDBDBD", height=50)
        top_frame.pack(fill="x", side="top")

        profile_btn = Button(top_frame, text="Profile", command=self.__practitioner_controller.main_profile, width=10, bg="#9E9E9E", fg="white", font=("Arial", 10, "bold"))
        profile_btn.pack(side="left", padx=10, pady=10)

        logout_btn = Button(top_frame, text="Logout",command=self.__practitioner_controller.main_logout, width=10, bg="#D32F2F", fg="white", font=("Arial", 10, "bold"))
        logout_btn.pack(side="right", padx=10, pady=10)

        # Container principal
        main_frame = Frame(self.root, bg="#424242")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Esquerda
        left_frame = Frame(main_frame, bg="#616161")
        left_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        create_plan_btn = Button(left_frame, text="Create new\nworkout plan", command=self.__practitioner_controller.create_workout_plan, font=("Arial", 16, "bold"), bg="#757575", fg="white", height=6, width=20)
        create_plan_btn.place(relx=0.5, rely=0.5, anchor="center")


        # Direita
        right_frame = Frame(main_frame, bg="#616161")
        right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        info_label = Label(right_frame, text=f"Name: {workout_plan["name"]}\nSessions: {workout_plan["sessions"]}", font=("Arial", 14, "bold"), bg="#616161", fg="white", justify="left")
        info_label.pack(anchor="w", pady=(20, 10), padx=20)

        btn_width = 40
        btn_pad_y = 15

        workouts_btn = Button(right_frame, text="Workouts", command=self.__practitioner_controller.workouts_screen, font=("Arial", 14, "bold"), bg="#E0E0E0", width=30, height=2)
        workouts_btn.pack(pady=btn_pad_y)

        edit_plan_btn = Button(right_frame, text="Edit Workout Plan", font=("Arial", 14, "bold"), bg="#E0E0E0", command=self.__practitioner_controller.update_workout_plan, width=30, height=2)
        edit_plan_btn.pack(pady=btn_pad_y)

        dashboard_btn = Button(right_frame, text="View Dashboard", font=("Arial", 14, "bold"), bg="#E0E0E0", width=30, height=2)
        dashboard_btn.pack(pady=btn_pad_y)