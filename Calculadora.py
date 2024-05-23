import tkinter as tk
from tkinter import PhotoImage

class CalculadoraPorcentaje(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Porcentaje")
        self.geometry("400x700")
        self.config(bg="light green")
        # Header con botones de aumento, disminución y borrar una cifra
        self.header_frame = tk.Frame(self, bg="#16a085")  # Verde oscuro
        self.header_frame.pack(fill=tk.BOTH, pady=(10, 5), padx=10)


        self.disminucion_button = tk.Button(self.header_frame, text="Disminuir", command=self.calcular_disminucion, width=10, height=2, bg="#1abc9c", fg="white", font=("Arial", 10, "bold"))  # Verde claro
        self.disminucion_button.pack(side="left", padx=(0, 5))

        self.aumento_button = tk.Button(self.header_frame, text="Aumentar", command=self.calcular_aumento, width=10, height=2, bg="#27ae60", fg="white", font=("Arial", 10, "bold"))  # Verde
        self.aumento_button.pack(side="right")

        # Campos de entrada
        self.campos_frame = tk.Frame(self, bg="#2ecc71")  # Verde más claro
        self.campos_frame.pack(fill=tk.BOTH, padx=10)

        self.valor_inicial_label = tk.Label(self.campos_frame, text="Valor Inicial:", bg="#2ecc71", fg="white", font=("Arial", 12))
        self.valor_inicial_label.pack(anchor="w", pady=(10, 5))

        self.valor_inicial_entry = tk.Entry(self.campos_frame, font=("Arial", 12))
        self.valor_inicial_entry.pack(fill=tk.X)

        self.porcentaje_label = tk.Label(self.campos_frame, text="Porcentaje (%):", bg="#2ecc71", fg="white", font=("Arial", 12))
        self.porcentaje_label.pack(anchor="w", pady=(10, 5))

        self.porcentaje_entry = tk.Entry(self.campos_frame, font=("Arial", 12))
        self.porcentaje_entry.pack(fill=tk.X)

        self.cambio_label = tk.Label(self.campos_frame, text="Cambio:", bg="#2ecc71", fg="white", font=("Arial", 12))
        self.cambio_label.pack(anchor="w", pady=(10, 5))

        self.cambio_entry = tk.Entry(self.campos_frame, font=("Arial", 12), state="readonly")
        self.cambio_entry.pack(fill=tk.X)

        self.suma_resta_label = tk.Label(self.campos_frame, text="Valor final:", bg="#2ecc71", fg="white", font=("Arial", 12))
        self.suma_resta_label.pack(anchor="w", pady=(10, 5))

        self.suma_resta_entry = tk.Entry(self.campos_frame, font=("Arial", 12), state="readonly")
        self.suma_resta_entry.pack(fill=tk.X)

        # Teclado numérico
        self.teclado_frame = tk.Frame(self, bg="#2ecc71")  # Verde más claro
        self.teclado_frame.pack(fill=tk.BOTH, padx=10, pady=(20, 10))

        teclas = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0", "Clear",
            "←", "→", "Borrar" # Flechas para navegar entre cifras
        ]

        r = 0
        c = 0
        for tecla in teclas:
            if tecla == "←":
                tk.Button(self.teclado_frame, text=tecla, width=8, height=2, command=self.mover_cursor_izquierda, bg="#2ecc71", fg="white", font=("Arial", 10, "bold")).grid(row=r, column=c, padx=5, pady=5)  # Verde más claro
            elif tecla == "→":
                tk.Button(self.teclado_frame, text=tecla, width=8, height=2, command=self.mover_cursor_derecha, bg="#2ecc71", fg="white", font=("Arial", 10, "bold")).grid(row=r, column=c, padx=5, pady=5)  # Verde más claro
            elif tecla == "Clear":
                tk.Button(self.teclado_frame, text=tecla, width=8, height=2, command=self.borrar_todo, bg="#e67e22", fg="white", font=("Arial", 10, "bold")).grid(row=r, column=c, padx=5, pady=5)
            elif tecla == "Borrar":
                tk.Button(self.teclado_frame,text= tecla, width=8,height=2, command=self.borrar_una_cifra, bg="#e74c3c", fg="white", font=("Arial", 10, "bold")).grid(row=r,column=5,pady=5) 

            else:
                tk.Button(self.teclado_frame, text=tecla, width=8, height=2, command=lambda t=tecla: self.insertar_texto(t), bg="#3498db", fg="white", font=("Arial", 10, "bold")).grid(row=r, column=c, padx=5, pady=5)  # Azul
            c += 1
            if c > 2:
                c = 0
                r += 1

        self.cursor_pos = 0 

    def calcular_cambio(self):
        try:
            valor_inicial = float(self.valor_inicial_entry.get())
            porcentaje = float(self.porcentaje_entry.get())
            cambio = valor_inicial * (porcentaje / 100)
            self.cambio_entry.config(state="normal")
            self.cambio_entry.delete(0, tk.END)
            self.cambio_entry.insert(0, cambio)
            self.cambio_entry.config(state="readonly")
        except ValueError:
            pass

    def calcular_aumento(self):
        self.calcular_cambio()
        try:
            valor_inicial = float(self.valor_inicial_entry.get())
            porcentaje = float(self.porcentaje_entry.get())
            resultado = valor_inicial + (valor_inicial * (porcentaje / 100))
            self.suma_resta_entry.config(state="normal")
            self.suma_resta_entry.delete(0, tk.END)
            self.suma_resta_entry.insert(0, resultado)
            self.suma_resta_entry.config(state="readonly")
        except ValueError:
            pass

    def calcular_disminucion(self):
        self.calcular_cambio()
        try:
            valor_inicial = float(self.valor_inicial_entry.get())
            porcentaje = float(self.porcentaje_entry.get())
            resultado = valor_inicial - (valor_inicial * (porcentaje / 100))
            self.suma_resta_entry.config(state="normal")
            self.suma_resta_entry.delete(0, tk.END)
            self.suma_resta_entry.insert(0, resultado)
            self.suma_resta_entry.config(state="readonly")
        except ValueError:
            pass

    def borrar_una_cifra(self):
        current_entry = self.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_index = current_entry.index("insert")
            if current_index > 0:
                new_index = int(current_index) - 1
                current_entry.delete(new_index, current_index)

    def insertar_texto(self, texto):
        current_entry = self.focus_get() 
        if current_entry in (self.valor_inicial_entry, self.porcentaje_entry):
            current_entry.insert(tk.END, texto)

    def mover_cursor_izquierda(self):
        current_entry = self.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_index = current_entry.index("insert")
            if current_index > 0:
                new_index = int(current_index) - 1
                self.cursor_pos = new_index 
                current_entry.icursor(new_index)

    def mover_cursor_derecha(self):
        current_entry = self.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_index = current_entry.index("insert")
            if current_index < len(current_entry.get()):
                new_index = int(current_index) + 1
                self.cursor_pos = new_index 
                current_entry.icursor(new_index)

    def borrar_todo(self):
        self.valor_inicial_entry.delete(0, tk.END)
        self.porcentaje_entry.delete(0, tk.END)
        self.cambio_entry.delete(0, tk.END)
        self.suma_resta_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = CalculadoraPorcentaje()
    app.mainloop()
