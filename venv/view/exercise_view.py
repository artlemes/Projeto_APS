from tkinter import *
from tkinter import messagebox


class ExerciseView:
    def __init__(self, root, exercise_controller):
            self.root = root
            self.__exercise_controller = exercise_controller
    
    def create_exercise_view(self, workout):
            container = Frame(self.root, bg="#212121")
            container.pack(expand=True)


            Label(container, text="Create new exercise", font=("Arial", 25, "bold"), bg="#212121", fg="White").pack(pady=10)

            # Nome do Exercicio
            Label(container, text="Name", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.name_entry = Entry(container, width=50)
            self.name_entry.pack(pady=5)
            self.name_error = Label(container, text="", fg="red", bg="#212121")
            self.name_error.pack()
            # Peso do Exercicio
            Label(container, text="Weight", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.weight_entry = Entry(container, width=50)
            self.weight_entry.pack(pady=5)
            self.weight_error = Label(container, text="", fg="red", bg="#212121")
            self.weight_error.pack()
            # Sets do Exercicio
            Label(container, text="Sets", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.sets_entry = Entry(container, width=50)
            self.sets_entry.pack(pady=5)
            self.sets_error = Label(container, text="", fg="red", bg="#212121")
            self.sets_error.pack()
            

            # Botão de criar
            Button(container, text="Create", font=("Arial", 12), bg="#4CAF50", fg="black", command=lambda: self.on_create_click(workout), width=50, height=2).pack(pady=(20, 10))

            Button(container, text="Cancel", font=("Arial", 12), bg="#dcdcdc", fg="black", command=lambda: self.__exercise_controller.workout_screen(workout),
                width=50, height=2).pack(pady=(0, 10))
            
    def update_exercise_view(self, exercise, workout):
            container = Frame(self.root, bg="#212121")
            container.pack(expand=True)


            Label(container, text="Update exercise", font=("Arial", 25, "bold"), bg="#212121", fg="White").pack(pady=10)

            # Nome do Exercicio
            Label(container, text=f"Name:  {exercise["name"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.name_update_entry = Entry(container, width=50)
            self.name_update_entry.pack(pady=5)
            self.name_update_error = Label(container, text="", fg="red", bg="#212121")
            self.name_update_error.pack()
            # Peso do Exercicio
            Label(container, text=f"Weight:  {exercise["weight"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.weight_update_entry = Entry(container, width=50)
            self.weight_update_entry.pack(pady=5)
            self.weight_update_error = Label(container, text="", fg="red", bg="#212121")
            self.weight_update_error.pack()
            # Sets do Exercicio
            Label(container, text=f"Sets:  {exercise["sets"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
            self.sets_update_entry = Entry(container, width=50)
            self.sets_update_entry.pack(pady=5)
            self.sets_update_error = Label(container, text="", fg="red", bg="#212121")
            self.sets_update_error.pack()
            

            # Botão de criar
            Button(container, text="Save", font=("Arial", 12), bg="#4CAF50", fg="black", command=lambda: self.on_update_click(workout, exercise), width=50, height=2).pack(pady=(20, 10))

            Button(container, text="Cancel", font=("Arial", 12), bg="#dcdcdc", fg="black", command=lambda: self.__exercise_controller.workout_screen(workout),
                width=50, height=2).pack(pady=(0, 10))
            

    def on_create_click(self, workout):
        name = self.name_entry.get().strip()
        weight = self.weight_entry.get().strip()
        sets = self.sets_entry.get().strip()
        
        if not name:
            self.name_error.config(text="Name is required.")
            return
        if not weight:
             weight = "0"
        if not weight.isdigit():
             self.weight_error.config(text="Invalid value.")
             return
        if not sets:
             sets = "0"
        if not sets.isdigit():
             self.sets_error.config(text="Invalid value.")
             return

        updated_data = {"name": name, "weight": weight, "sets": sets}
        self.__exercise_controller.create_exercise(updated_data, workout)
    
    def on_update_click(self, workout, exercise):
        name = self.name_update_entry.get().strip()
        weight = self.weight_update_entry.get().strip()
        sets = self.sets_update_entry.get().strip()
        print(name ,weight, sets)
        if not name:
            name = exercise["name"]
        if not weight:
             weight = exercise["weight"]
        if not weight.isdigit():
             self.weight_update_error.config(text="Invalid value.")
             return
        if not sets:
             sets = exercise["sets"]
        if not sets.isdigit():
             self.sets_update_error.config(text="Invalid value.")
             return

        updated_data = {"id": exercise["id"], "name": name, "weight": weight, "sets": sets}
        self.__exercise_controller.update_exercise(updated_data, workout)

    @classmethod
    def throw_message(type, text):
        match type:
            case "Info":
                messagebox.showinfo(type, text)
            case "Error":
                messagebox.showerror(type, text)
            case "warning":
                messagebox.showwarning(type, text)