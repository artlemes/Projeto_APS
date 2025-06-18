from tkinter import *
from tkinter import messagebox


class WorkoutView:
    def __init__(self, root, workout_controller):
            self.root = root
            self.__workout_controller = workout_controller
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def workout_home_view(self, workouts, rest_time):
        self.clear_window()
        container = Frame(self.root, bg="#212121")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        Label(container, text="Workouts", font=("Arial", 25, "bold"),
            bg="#424242", fg="white", pady=10, padx=20).pack(fill="x", pady=(10, 20))

        if len(workouts) > 5:
            # Scroll ativado
            scroll_frame = Frame(container, bg="#212121")
            scroll_frame.pack(fill="x")

            canvas = Canvas(scroll_frame, bg="#212121", highlightthickness=0, height=250)
            canvas.pack(side="top", fill="x")

            scroll_x = Scrollbar(scroll_frame, orient="horizontal", command=canvas.xview)
            scroll_x.pack(side="top", fill="x")
            canvas.configure(xscrollcommand=scroll_x.set)

            cards_frame = Frame(canvas, bg="#212121")
            canvas.create_window((0, 0), window=cards_frame, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            cards_frame.bind("<Configure>", on_configure)

            for i, workout in enumerate(workouts):
                card = Frame(cards_frame, bg="#d3d3d3", padx=15, pady=15)
                card.grid(row=0, column=i, padx=10, pady=10)

                Label(card, text=workout['day'], font=("Arial", 14, "bold"), bg="#d3d3d3", fg="black").pack(pady=(0, 5))
                Label(card, text=workout['name'], font=("Arial", 12), bg="#d3d3d3", fg="black").pack(pady=(0, 10))

                Button(card, text="View", font=("Arial", 12), bg="#505050", fg="white",
                    width=15, command=lambda w=workout: self.view_workout(w, rest_time)).pack(pady=(0, 10))
                Button(card, text="Edit", font=("Arial", 12), bg="#505050", fg="white",
                    width=15, command=lambda w=workout: self.update_workout(w)).pack(pady=(0, 10))
                Button(card, text="Done", font=("Arial", 12), bg="#4CAF50", fg="white",
                    width=15).pack(pady=(10))

        else:
            # Scroll desativado
            cards_frame = Frame(container, bg="#212121")
            cards_frame.pack()

            for workout in workouts:
                card = Frame(cards_frame, bg="#d3d3d3", height=40, padx=15, pady=15)
                card.pack(side="left", padx=10, pady=10)

                Label(card, text=workout['day'], font=("Arial", 14, "bold"), bg="#d3d3d3", fg="black").pack(pady=(0, 5))
                Label(card, text=workout['name'], font=("Arial", 12), bg="#d3d3d3", fg="black").pack(pady=(0, 10))

                Button(card, text="View", font=("Arial", 12), bg="#505050", fg="white",
                    width=15, command=lambda w=workout: self.view_workout(w, rest_time)).pack(pady=(0, 10))
                Button(card, text="Edit", font=("Arial", 12), bg="#505050", fg="white",
                    width=15, command=lambda w=workout: self.update_workout(w)).pack(pady=(0, 10))
                Button(card, text="Done", font=("Arial", 12), bg="#4CAF50", fg="white",
                    width=15).pack(pady=(10))

                # ✅ Botão Back - deve aparecer
        Button(container, text="Back", font=("Arial", 12), command=lambda: self.__workout_controller.home_screen(), bg="#dcdcdc", fg="black", width=50, height=2).pack(pady=(40, 0))

    def update_workout(self, workout):
        self.clear_window()
        container = Frame(self.root, bg="#212121")
        container.pack(expand=True)


        Label(container, text="Edit Workout", font=("Arial", 25, "bold"), bg="#212121", fg="White").pack(pady=10)

        # Nome do plano
        Label(container, text=f"Name: {workout["name"]}", font=("Arial", 12), bg="#212121", fg="white").pack(pady=5)
        self.name_update_entry = Entry(container, width=50)
        self.name_update_entry.pack(pady=5)
        self.name_update_error = Label(container, text="", fg="red", bg="#212121")
        self.name_update_error.pack()

        # Botão de criar
        Button(container, text="Update", font=("Arial", 12), bg="#4CAF50", fg="black", command=lambda: self.on_update_click(workout), width=50, height=2).pack(pady=(20, 10))

        Button(container, text="Back", font=("Arial", 12), bg="#dcdcdc", fg="black", command=self.__workout_controller.workouts_screen,
            width=50, height=2).pack(pady=(0, 10))

    def on_update_click(self, workout):
        name = self.name_update_entry.get().strip()
        
        if not name:
            self.name_update_error.config(text="Name is required.")
            return

        updated_data = {"name": name}
        def check_updated_data():
            if updated_data["name"] == workout["name"]:
                return True
            return False
            
        if check_updated_data():
            messagebox.showinfo("Info", "No changes to update.")
            return
        self.__workout_controller.update_workout(workout["day"], updated_data)
    
    def view_workout(self, workout, rest_time):
        self.clear_window()
        container = Frame(self.root, bg="#212121")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        Label(container, text=workout["day"], font=("Arial", 25, "bold"), bg="#212121", fg="white").pack(pady=(10, 5))
        Label(container, text=workout["name"], font=("Arial", 18), bg="#212121", fg="white").pack(pady=(0, 10))
        Label(container, text=f"Rest time: {rest_time[0]} - {rest_time[1]} seconds", font=("Arial", 12), bg="#212121", fg="white").pack(anchor="e", padx=40)

        exercises_frame = Frame(container, bg="#424242")
        exercises_frame.pack(fill="both", expand=True, padx=40, pady=20)

        for exercise in workout.get("exercises", []):
            min_max = exercise.get("reps_range", "")
            row = Frame(exercises_frame, bg="#d3d3d3", pady=10)
            row.pack(fill="x", pady=5)

            Label(row, text=exercise.get("name", ""), width=20, anchor="w", bg="#d3d3d3").pack(side="left", padx=5)
            Label(row, text=(f"{min_max[0]}  -  {min_max[1]}"), width=20, anchor="w", bg="#d3d3d3").pack(side="left", padx=5)
            Label(row, text=exercise.get("weight", ""), width=10, anchor="w", bg="#d3d3d3").pack(side="left", padx=5)
            Label(row, text=exercise.get("sets", ""), width=10, anchor="w", bg="#d3d3d3").pack(side="left", padx=5)

        # Botões Edit e Back
        buttons_frame = Frame(container, bg="#212121")
        buttons_frame.pack(pady=20)

        Button(buttons_frame, text="Edit", font=("Arial", 12, "bold"), bg="#505050", fg="white", width=40, height=2,
            command=lambda: self.edit_workout_exercises_view(workout, rest_time)).pack(side="left", padx=20)
        Button(buttons_frame, text="Back", font=("Arial", 12, "bold"), bg="#dcdcdc", fg="black", width=40, height=2,
            command=self.__workout_controller.workouts_screen).pack(side="left", padx=20)
    
    def edit_workout_exercises_view(self, workout, rest_time):
        self.clear_window()
        self.workout = workout
        container = Frame(self.root, bg="#212121")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        Label(container, text=workout["day"], font=("Arial", 25, "bold"), bg="#212121", fg="white").pack(pady=(10, 5))
        Label(container, text=workout["name"], font=("Arial", 18), bg="#212121", fg="white").pack(pady=(0, 10))
        Label(container, text=f"Rest time: {rest_time[0]} - {rest_time[1]} seconds", font=("Arial", 12), bg="#212121", fg="white").pack(anchor="e", padx=40)

        exercises_frame = Frame(container, bg="#424242", padx=10, pady=10)
        exercises_frame.pack(fill="both", expand=True, padx=40, pady=20)

        self.exercise_entries = []

        for exercise in workout.get("exercises", []):
            self.add_editable_exercise_row(exercises_frame, exercise)


        # Confirm / Cancel
        buttons_frame = Frame(container, bg="#212121")
        buttons_frame.pack(pady=20)

        Button(buttons_frame, text="Confirm", font=("Arial", 12, "bold"), bg="#505050", fg="white", width=50,height=2,
            command=lambda: self.__workout_controller.workout_screen(workout)).pack(side="left", padx=20)
        Button(buttons_frame, text="Add exercise", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=50, height=2,
            command=lambda w=workout: self.__workout_controller.create_exercise(w)).pack(side="left",padx=20)
       
    def add_editable_exercise_row(self, parent, exercise=None):
        row = Frame(parent, bg="#d3d3d3", pady=10)
        row.pack(fill="x", pady=5)

        # Labels normais (sem Entry)
        Label(row, text=exercise.get("name", "nome"), bg="#d3d3d3", width=20, anchor="w").pack(side="left", padx=5)
        Label(row, text=exercise.get("reps_range", "repetições"), bg="#d3d3d3", width=20, anchor="w").pack(side="left", padx=5)
        Label(row, text=exercise.get("weight", "peso"), bg="#d3d3d3", width=10, anchor="w").pack(side="left", padx=5)
        Label(row, text=exercise.get("sets", "sets"), bg="#d3d3d3", width=10, anchor="w").pack(side="left", padx=5)

        # Botões de Editar e Deletar
        buttons_frame = Frame(row, bg="#d3d3d3")
        buttons_frame.pack(side="right", padx=10)  # <-- margem da borda direita

        Button(buttons_frame, text="Edit", font=("Arial", 10), bg="#065095", fg="white", width=12,
            command=lambda e=exercise: self.__workout_controller.update_exercise_screen(exercise, self.workout)).pack(side="left", padx=5)
        Button(buttons_frame, text="Delete", font=("Arial", 10), bg="#b22222", fg="white", width=12,
            command=lambda: self.remove_exercise_row(row, exercise)).pack(side="left", padx=5)

    def remove_exercise_row(self, row, exercise):
        self.__workout_controller.delete_exercise(exercise, self.workout)
        row.destroy()
        
    def throw_error(type, text): 
        match type:
            case "Info":
                messagebox.showinfo(type, text)
            case "Error":
                messagebox.showerror(type, text)
            case "warning":
                messagebox.showwarning(type, text)