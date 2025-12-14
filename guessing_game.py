import customtkinter as ctk
import random

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class GuessingGameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game | SkillCraft Task 02")
        self.geometry("500x550")
        self.resizable(False, False)

        self.secret_number = None
        self.attempts = 0
        self.max_range = 100
        self.game_over = False  

        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self, 
            text="Guess the Number!", 
            font=("Arial", 26, "bold"),
            text_color="#2C3E50"
        )
        self.title_label.pack(pady=20)

        self.diff_label = ctk.CTkLabel(self, text="Select Difficulty:", text_color="gray40")
        self.diff_label.pack(pady=(10, 5))
        
        self.difficulty_menu = ctk.CTkOptionMenu(
            self,
            values=["Easy (1-10)", "Medium (1-50)", "Hard (1-100)"],
            command=self.change_difficulty,
            fg_color="#3B8ED0",
            button_color="#36719F"
        )
        self.difficulty_menu.pack(pady=5)
        self.difficulty_menu.set("Hard (1-100)")

        self.status_label = ctk.CTkLabel(
            self, 
            text="I'm thinking of a number...", 
            font=("Arial", 18),
            text_color="#E67E22"
        )
        self.status_label.pack(pady=30)

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=10)

        self.guess_entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="#",
            width=100,
            justify="center",
            font=("Arial", 20)
        )
        self.guess_entry.pack(side="left", padx=10)

        self.guess_btn = ctk.CTkButton(
            self.input_frame, 
            text="Guess", 
            command=self.check_guess,
            width=100,
            font=("Arial", 14, "bold")
        )
        self.guess_btn.pack(side="left", padx=10)

        self.attempts_label = ctk.CTkLabel(self, text="Attempts: 0", text_color="gray50")
        self.attempts_label.pack(pady=20)

        self.reset_btn = ctk.CTkButton(
            self, 
            text="Play Again", 
            command=self.start_new_game,
            fg_color="transparent",
            border_width=2,
            border_color="#3B8ED0",
            text_color="#3B8ED0",
            hover_color="#EBF5FB"
        )
        self.reset_btn.pack(pady=20)

        self.bind('<Return>', lambda event: self.check_guess())

    def change_difficulty(self, choice):
        if "Easy" in choice:
            self.max_range = 10
        elif "Medium" in choice:
            self.max_range = 50
        else:
            self.max_range = 100
        self.start_new_game()

    def start_new_game(self):
        self.secret_number = random.randint(1, self.max_range)
        self.attempts = 0
        self.game_over = False
        
        self.attempts_label.configure(text="Attempts: 0")
        self.status_label.configure(text=f"Range: 1 to {self.max_range}", text_color="gray40")
        self.guess_entry.delete(0, "end")
        self.guess_btn.configure(state="normal", fg_color="#3B8ED0")

    def check_guess(self):
        if self.game_over:
            return  

        try:
            user_guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.configure(text=f"Attempts: {self.attempts}")

            if user_guess < self.secret_number:
                self.status_label.configure(text="Too Low! Try Higher ⬆️", text_color="#2980B9")
            elif user_guess > self.secret_number:
                self.status_label.configure(text="Too High! Try Lower ⬇️", text_color="#C0392B")
            else:
                self.status_label.configure(text=f"🎉 Correct! The number was {self.secret_number}", text_color="#27AE60")
                self.guess_btn.configure(state="disabled", fg_color="gray")
                self.game_over = True 
        
        except ValueError:
            self.status_label.configure(text="Please enter a valid number!", text_color="#E74C3C")

if __name__ == "__main__":
    app = GuessingGameApp()
    app.mainloop()