from model.exercise import Exercise
from view.exercise_view import ExerciseView

class ExerciseController:
    def __init__(self, root, main_controller):
        self.root = root
        self.__main_controller = main_controller
        self.__exercise_view = ExerciseView(self.root, self)

    def create_exercise(self, data, workout):
        reps_range = self.__main_controller.get_rest_and_reps_range("Reps")
        data["reps_range"] = reps_range
        try:
            res = Exercise(data["name"], data["reps_range"], data["weight"], data["sets"])
            existing_ids = [ex.get("id", 0) for ex in workout.get("exercises", [])]
            next_id = max(existing_ids, default=0) + 1

            exercise = {
                "id": next_id,
                "name": res.name,
                "reps_range": res.reps_range,
                "weight": res.weight,
                "sets": res.sets
            }
            self.handle_creat(exercise, workout)
            return exercise
        except Exception as e: 
            print(e)
            return e
    
    def remove_exercise(self, email, workout, exercise_to_remove):
        try:
            exercises = workout.get("exercises", [])

            if exercise_to_remove not in exercises:
                raise Exception("Exercício não encontrado na lista.")

            # Remove in-place (sem retornar)
            exercises.remove(exercise_to_remove)

            # Atualiza a lista no banco
            workout["exercises"] = exercises
            Exercise.handle_create(email, workout["day"], exercises)

            # Mensagem de sucesso
            type = "Info"
            text = "Exercício removido com sucesso."
            ExerciseView.throw_message(type, text)

        except Exception as e:
            print("Erro ao remover exercício:", e)
            type = "Erro"
            text = "Não foi possível remover o exercício."
            ExerciseView.throw_message(type, text)

    def handle_creat(self, exercise, workout):
        try:
            exercises = workout["exercises"]
            exercises.append(exercise)
            email = self.__main_controller.get_logged_user()
            res = Exercise.update_exercise(email, workout["day"], exercises)
            if res == True:
                type = "Info"
                text = "Exercicio atualizado com exito!"
                ExerciseView.throw_message(type, text)
                self.workout_screen(workout)
            else: raise Exception
        except Exception as e:
            print("Erro:", e)
            type = "Error"
            text = "Erro ao atualizar o treino!"
            ExerciseView.throw_message(type, text)

    def update_exercise(self, exercise, workout):
        try:
            if not exercise.get("reps_range"):
                reps_range = self.__main_controller.get_rest_and_reps_range("Reps")
                exercise["reps_range"] = reps_range

            # Substituir o exercício correspondente
            exercises = workout["exercises"]
            updated = False

            for idx, ex in enumerate(exercises):
                if ex["id"] == exercise["id"]:  # ou use outro identificador único
                    exercises[idx] = exercise
                    updated = True
                    break

            if not updated:
                raise Exception("Exercício não encontrado para atualização")
            # Atualizar no banco
            email = self.__main_controller.get_logged_user()
            res = Exercise.update_exercise(email, workout["day"], exercises)

            if res is True:
                ExerciseView.throw_message("Info", "Exercício atualizado com êxito!")
                self.workout_screen(workout)
            else:
                raise Exception("Falha ao atualizar no banco.")

        except Exception as e:
            print("Erro:", e)
            ExerciseView.throw_message("Error", "Erro ao atualizar o exercício!")

    def create_exercise_screen(self, workout):
        self.__exercise_view.create_exercise_view(workout)
    
    def update_exercise_screen(self, exercise, workout):
        self.__exercise_view.update_exercise_view(exercise, workout)

    
    def workout_screen(self, workout):
        self.__main_controller.main_workout_screen(workout)