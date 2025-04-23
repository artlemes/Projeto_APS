from tkinter import Tk
from controller.main_controller import MainController

if __name__ == "__main__":
    root = Tk()
    root.title("FitTrack Desktop")
    root.geometry("1200x600")
    root.configure(bg="#212121")
    app = MainController(root)
    root.mainloop()