from tkinter import *
from tkinter import ttk, messagebox


class WorkoutPlanView:
    def __init__(self, root, workout_plan_controller):
            self.root = root
            self.__workout_plan_controller = workout_plan_controller
    
    def create_workout_plan_screen(self, email):
        container = Frame(self.root, bg="#212121")
        container.pack(expand=True)


        Label(container, text="New Workout Plan", font=("Arial", 25, "bold"), bg="#212121", fg="White").pack(pady=10)

        # Nome do plano
        Label(container, text="Name:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_entry = Entry(container, width=50)
        self.name_entry.pack(pady=5)
        self.name_error = Label(container, text="", fg="red", bg="#212121")
        self.name_error.pack()

        # Objetivo
        Label(container, text="Set the goal:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.goal_var = StringVar()
        type_combobox = ttk.Combobox(
            container,
            textvariable=self.goal_var,
            values=["Strengthening", "Weight Loss", "Hypertrophy"],
            state="readonly",
            width=47
        )
        type_combobox.pack(pady=5)
        self.type_error = Label(container, text="", fg="red", bg="#212121")
        self.type_error.pack()

        # Sessões
        Label(container, text="Amount of Sessions:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.sessions_entry = Entry(container, width=50)
        self.sessions_entry.pack(pady=5)
        self.sessions_error = Label(container, text="", fg="red", bg="#212121")
        self.sessions_error.pack()

        # Botão Days on the week (apenas visual por enquanto)
        Button(container, text="Days on the week", font=("Arial", 12, "bold"), bg="#dcdcdc", width=25, relief=FLAT, command=lambda: self.on_days_click()).pack(pady=15)
        self.days_status_label = Label(container, text="", fg="green", bg="#212121")
        self.days_status_label.pack()

        # Botão de criar
        Button(container, text="Create", font=("Arial", 12), bg="#4CAF50", fg="black", command=lambda: self.on_create_click(email), width=50, height=2).pack(pady=20)

        Button(container, text="Back", font=("Arial", 12), bg="#dcdcdc", fg="black", command=self.__workout_plan_controller.home_screen,
            width=50, height=2).pack()
        
    def update_workout_plan_screen(self, workout_plan_data):
        container = Frame(self.root, bg="#212121")
        container.pack(expand=True)


        Label(container, text="Edit Workout Plan", font=("Arial", 25, "bold"), bg="#212121", fg="White").pack(pady=10)

        # Nome do plano
        Label(container, text=f"Name: {workout_plan_data["name"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_update_entry = Entry(container, width=50)
        self.name_update_entry.pack(pady=5)
        self.name_update_error = Label(container, text="", fg="red", bg="#212121")
        self.name_update_error.pack()

        # Objetivo
        Label(container, text="Set the goal:", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.goal_update_var = StringVar()
        goal_combobox = ttk.Combobox(
            container,
            textvariable=self.goal_update_var,
            values=["Strengthening", "Weight Loss", "Hypertrophy"],
            state="readonly",
            width=47,
        )
        goal_combobox.set(workout_plan_data["goal"])
        goal_combobox.pack(pady=5)
        self.type_update_error = Label(container, text="", fg="red", bg="#212121")
        self.type_update_error.pack()

        # Sessões
        Label(container, text=f"Amount of Sessions: {workout_plan_data["sessions"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.sessions_update_entry = Entry(container, width=50)
        self.sessions_update_entry.pack(pady=5)
        self.sessions_update_error = Label(container, text="", fg="red", bg="#212121")
        self.sessions_update_error.pack()

        # Botão Days on the week (apenas visual por enquanto)
        self.days_status_label = Label(container, text="", fg="green", bg="#212121")
        self.days_status_label.pack()
        Button(container, text="Delete Workout Plan", font=("Arial", 12, "bold"), bg="#a83232", width=25, relief=FLAT, command=lambda: self.delete_workout_plan(workout_plan_data["email"])).pack(pady=(5, 10))

        # Botão de criar
        Button(container, text="Update", font=("Arial", 12), bg="#4CAF50", fg="black", command=lambda: self.on_update_click(workout_plan_data), width=50, height=2).pack(pady=(20, 10))

        Button(container, text="Back", font=("Arial", 12), bg="#dcdcdc", fg="black", command=self.__workout_plan_controller.home_screen,
            width=50, height=2).pack(pady=(0, 10))
        
    def on_update_click(self, data):
        name = self.name_update_entry.get().strip()
        goal = self.goal_update_var.get().strip()
        sessions = self.sessions_update_entry.get().strip()

        # Atualiza somente os campos preenchidos
        if not name:
            name = data["name"]
        if not goal:
             goal = data["goal"]
        if not sessions:
            sessions = data["sessions"]
        elif sessions.isdigit():
            pass
        else:
            self.sessions_update_error.config(text="Enter a valid number")
            return
        
        updated_data = {"name": name,
                        "goal": goal,
                        "sessions": sessions,
                        "days": data["workouts"]
                        }
        def check_updated_data():
            if updated_data["name"] == data["name"] and \
            updated_data["goal"] == data["goal"] and \
            updated_data["sessions"] == data["sessions"]:
                return True
            return False
            
        if check_updated_data():
            messagebox.showinfo("Info", "No changes to update.")
            return

        print(updated_data)
        self.__workout_plan_controller.update_workout_plan(updated_data)
        


    def on_days_click(self):
        self.days_selected = {i: False for i in range(7)}  # 0 = Domingo, ..., 6 = Sábado
        self.open_days_selection_window()

    def open_days_selection_window(self):
        days_window = Toplevel(self.root)
        days_window.title("Select Days of the Week")
        days_window.configure(bg="#212121")

        self.days_map = {
            0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday"
        }

        self.day_vars = {}

        Label(days_window, text="Select the days for your workout", fg="white", font=("Arial", 14, "bold"), bg="#212121").pack(pady=10, padx=5)

        for i in range(7):
            var = BooleanVar(value=self.days_selected[i])
            cb = Checkbutton(
                days_window,
                text=self.days_map[i],
                fg="white",
                variable=var,
                font=("Arial", 12),
                bg="#212121",
                selectcolor="#424242",  # Cor visível do check marcado
                activebackground="#212121",  # remove o "highlight" do botão
                activeforeground="white"
                )
            cb.pack(anchor="w", padx=20)
            self.day_vars[i] = var

        def save_days():
            self.days_selected = {i: var.get() for i, var in self.day_vars.items()}
            print(self.days_selected)
            
            if any(self.days_selected.values()):
                self.days_status_label.config(text="Days selected!", fg="green")
            else:
                self.days_status_label.config(text="Select at least one day.", fg="red")
            
            days_window.destroy()
        Button(days_window, text="Save", command=save_days, font=("Arial", 12, "bold"), bg="#4CAF50", width= 16, fg="white").pack(pady=(20, 10))
    


    def delete_workout_plan(self, email):
        result = messagebox.askyesno("Delete Workout Plan", "Tem certeza que deseja deletar seu plano de treino?")
        if result:
            self.__workout_plan_controller.delete_workout_plan(email)
    
    def on_create_click(self, email):
        name = self.name_entry.get().strip()
        goal = self.goal_var.get().strip()
        sessions = self.sessions_entry.get().strip()
        days = self.days_selected if hasattr(self, 'days_selected') else {}

        # Limpa mensagens anteriores
        self.name_error.config(text="")
        self.type_error.config(text="")
        self.sessions_error.config(text="")
        self.days_status_label.config(text="")

        # Validações
        valid = self.validation(name, goal, sessions, days)

        if not valid:
            return

        # Se tudo estiver válido, chama o controller (exemplo)
        workout_data = {
            "email": email,
            "name": name,
            "goal": goal,
            "sessions": int(sessions),
            "days": [self.days_map[day] for day, selected in days.items() if selected]
        }
        print("Saindo do Viwe", workout_data)
        self.__workout_plan_controller.create_workout_plan(workout_data)

    def throw_error(type, text):
        match type:
            case "Info":
                messagebox.showinfo(type, text)
            case "Error":
                messagebox.showerror(type, text)
            case "warning":
                messagebox.showwarning(type, text)


    #coloquei a validação dos campos aqui
    def validation(self, name, goal, sessions, days): 

        print("numero de sessoes assim q cliquei create: ", sessions)
        valid = True

        if not name:
            self.name_error.config(text="Name is required.")
            valid = False

        if not goal:
            self.type_error.config(text="Goal is required.")
            valid = False

        if not sessions.isdigit(): 
            self.sessions_error.config(text="Enter a valid number of sessions.")
            valid = False

        if (sessions == "0"):
            self.sessions_error.config(text="The number of sessions can't be zero")
            valid = False

        print(days.values())

        if not any(days.values()):
            self.days_status_label.config(text="Select at least one day.", fg="red")
            valid = False
        else:
            self.days_status_label.config(text="Days selected!", fg="green")

        return valid