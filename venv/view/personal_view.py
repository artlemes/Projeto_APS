from tkinter import *

class PersonalView:
    def __init__(self, root, personal_controller):
        self.root = root
        self.__personal_controller = personal_controller
    

    def home_personal_screen(self):
        # Top bar
        top_frame = Frame(self.root, bg="#BDBDBD", height=50)
        top_frame.pack(fill="x", side="top")

        profile_btn = Button(top_frame, text="Profile",command=self.__personal_controller.main_profile, width=10, bg="#9E9E9E", fg="white", font=("Arial", 10, "bold"))
        profile_btn.pack(side="left", padx=10, pady=10)

        logout_btn = Button(top_frame, text="Logout", command=self.__personal_controller.main_logout, width=10, bg="#D32F2F", fg="white", font=("Arial", 10, "bold"))
        logout_btn.pack(side="right", padx=10, pady=10)

        # Main container
        main_frame = Frame(self.root, bg="#E0E0E0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Title and Add button
        header_frame = Frame(main_frame, bg="#E0E0E0")
        header_frame.pack(fill="x", pady=(10, 20))

        title = Label(header_frame, text="Practitioners", font=("Arial", 18, "bold"), bg="#E0E0E0")
        title.pack(side="left", padx=10)

        add_btn = Button(header_frame, text="Add practitioners", bg="#424242", fg="white", font=("Arial", 10, "bold"))
        add_btn.pack(side="right", padx=10)

        # Mockup list of practitioners
        practitioners = ["Practitioner 1", "Practitioner 2"]
        for name in practitioners:
            row_frame = Frame(main_frame, bg="#757575")
            row_frame.pack(fill="x", padx=10, pady=10)

            name_label = Label(row_frame, text=name, bg="#757575", fg="white", font=("Arial", 12, "bold"))
            name_label.pack(side="left", padx=20, pady=10, expand=True, fill="x")

            dashboard_btn = Button(row_frame, text="View Dashboard", bg="#9E9E9E", fg="white", font=("Arial", 10, "bold"), width=15)
            dashboard_btn.pack(side="left", padx=10)

            remove_btn = Button(row_frame, text="Remove", bg="#B71C1C", fg="white", font=("Arial", 10, "bold"), width=15)
            remove_btn.pack(side="right", padx=10)
