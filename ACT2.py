import tkinter as tk
from tkinter import messagebox
import random
from math import sqrt


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Matemático")
        self.root.geometry("300x150")

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.check_button = tk.Button(root, text="Comprobar", command=self.check_answer)
        self.check_button.pack()

        self.score = 0
        self.questions_answered = 0
        self.generate_question()

    def generate_question(self):
        self.num1 = random.randint(1, 5)
        self.num2 = random.randint(1, 5)
        self.operator = random.choice(['+', '-', '*',"/","^","√"])
        self.question = f"{self.num1} {self.operator} {self.num2}"
        self.question_label.config(text=self.question)

    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get())
            if self.operator == '+':
                correct_answer = self.num1 + self.num2
            elif self.operator == '-':
                correct_answer = self.num1 - self.num2
            elif self.operator == '*':
                correct_answer = self.num1 * self.num2
            elif self.operator == '/':
                correct_answer = self.num1 / self.num2
            elif self.operator == '^':
                correct_answer = pow(self.num1,self.num2)
            elif self.operator == '√':
                correct_answer = sqrt(self.num1)

            if user_answer == correct_answer:
                messagebox.showinfo("Correcto", "¡Respuesta correcta!")
                self.score += 1
            else:
                messagebox.showerror("Incorrecto", "Respuesta incorrecta.")
            self.questions_answered += 1
            self.generate_question()
            self.answer_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

        self.root.title(f"Puntuación: {self.score}/{self.questions_answered}")
if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
