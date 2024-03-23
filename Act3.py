import tkinter as tk
from tkinter import messagebox, Label
import random
from tkinter import simpledialog

# Lista de preguntas y respuestas
preguntas = [
    ("¿Cuál es la capital de Francia?", "París"),
    ("¿En qué año llegó Cristóbal Colón a América?", "1492"),
    ("¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes"),
    ("¿Qué planeta es conocido como 'el planeta rojo'?", "Marte"),
    ("¿Quién pintó la 'Mona Lisa'?", "Leonardo da Vinci"),
    ("¿Quien canta la cancion '...baby one more time'","Britney Spears")
]

# Función para mostrar una pregunta aleatoria
def mostrar():
    preg, res = random.choice(preguntas)
    messagebox.showinfo("Pregunta", preg)
    usuario = simpledialog.askstring("Respuesta", "Escribe tu respuesta:")
    if usuario.lower() == res.lower():
        messagebox.showinfo("Andale", "¡Le sabes mucho!")
    else:
        messagebox.showerror("Jaja q wey", f"La respuesta correcta es: {res}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cultura General")
root.config(bg="light green")
root.geometry("200x100")

lbltexto=Label(text="Si no respondes sos nuv")
# Botón para mostrar la pregunta
question_button = tk.Button(root, text="Mostrar Pregunta", command=mostrar)
question_button.pack(pady=20)

# Ejecutar la ventana
root.mainloop()