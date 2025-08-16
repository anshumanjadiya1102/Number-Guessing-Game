import tkinter as tk
import random
import winsound  # Works only on Windows

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game with Sound")
        self.root.geometry("400x250")

        self.number_to_guess = random.randint(1, 100)
        self.tries = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.reset_button.pack(pady=5)
        self.reset_button.config(state=tk.DISABLED)

    def play_success_sound(self):
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

    def play_error_sound(self):
        winsound.MessageBeep(winsound.MB_ICONHAND)

    def check_guess(self):
        guess = self.entry.get().strip()

        if not guess.isdigit():
            self.result_label.config(text="❌ Please enter a valid number.")
            self.play_error_sound()
            return

        guess = int(guess)
        if not 1 <= guess <= 100:
            self.result_label.config(text="⚠️ Number out of range (1–100).")
            self.play_error_sound()
            return

        self.tries += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"🎉 Correct! You guessed it in {self.tries} tries.")
            self.play_success_sound()
            self.submit_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.tries = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGameGUI(root)
    root.mainloop()
