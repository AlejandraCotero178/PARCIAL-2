import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario")
ventana.config(bg="light green")
ventana.geometry("500x500")

#glucosa:

def verificar_niveles_glucosa(nivel):
    if nivel < 70:
        return "Bajos"
    elif nivel >= 70 and nivel <= 100:
        return "Normales"
    else:
        return "Altos"



#presion:
        
def verificar_niveles_presion(nivel1):
    if nivel1 < 120:
        return "Bajos"
    elif nivel1 >= 120 and nivel1 < 140:
        return "Normales"
    elif nivel1 >= 140 and nivel1 < 180:
        return "Elevada"
    else:
        return "Hipertencion"
    


#Temperatura
    
def verificar_niveles_temperatura(nivel2):
    if nivel2 < 33.5:
        return "Bajo"
    elif nivel2 >= 33.5 and nivel2 <=37:
        return "Normal"
    elif nivel2 >= 38:
        return "Alta"
       

#HemoglobinaHom
def verificar_niveles_hemoglobinaH(nivel3):
    if nivel3 < 13.2:
        return "Bajo"
    elif nivel3 >= 13.2 and nivel3 <=16.6:
        return "Normal"
    elif nivel3 > 16.6:
        return "Alta"
       
#HemoglobinaMu
def verificar_niveles_hemoglobinaM(nivel4):
    if nivel4 < 11.6:
        return "Bajo"
    elif nivel4 >= 11.6 and nivel4 <=15:
        return "Normal"
    elif nivel4 > 15:
        return "Alta"
       










#glucosa
def mostrar_resultado():
    try:
        nivel_glucosa = float(entry.get())
        resultado = verificar_niveles_glucosa(nivel_glucosa)
        label_resultado.config(text="Sus niveles de glucosa son: " + resultado)
    except ValueError:
        label_resultado.config(text="Por favor, ingrese un número válido.")
label_instrucciones = tk.Label(ventana, text="Ingrese su nivel de glucosa en mg/dL:")
label_instrucciones.pack(pady=5)


entry = tk.Entry(ventana)
entry.pack(pady=5)


boton_verificar = tk.Button(ventana, text="Verificar", command=mostrar_resultado)
boton_verificar.pack(pady=5)


label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=5)

#presion

def mostrar_resultado2():
    try:
        nivel_presion = float(entry2.get())
        resultado2 = verificar_niveles_presion(nivel_presion)
        label_resultado2.config(text="Su nivel de presion es: " + resultado2)
    except ValueError:
        label_resultado2.config(text="Por favor, ingrese un número válido.")

label_instrucciones2 = tk.Label(ventana, text="Ingrese su nivel de presion:")
label_instrucciones2.pack(pady=5)


entry2 = tk.Entry(ventana)
entry2.pack(pady=5)


boton_verificar2 = tk.Button(ventana, text="Verificar", command=mostrar_resultado2)
boton_verificar2.pack(pady=5)


label_resultado2 = tk.Label(ventana, text="")
label_resultado2.pack(pady=5)

#Temperatura
def mostrar_resultado3():
    try:
        nivel_temp = float(entry3.get())
        resultado3 = verificar_niveles_temperatura(nivel_temp)
        label_resultado3.config(text="Su Temperatura es: " + resultado3)
    except ValueError:
        label_resultado3.config(text="Por favor, ingrese un número válido.")

label_instrucciones3 = tk.Label(ventana, text="Ingrese su Temperatura:")
label_instrucciones3.pack(pady=5)


entry3 = tk.Entry(ventana)
entry3.pack(pady=5)


boton_verificar3 = tk.Button(ventana, text="Verificar", command=mostrar_resultado3)
boton_verificar3.pack(pady=5)


label_resultado3 = tk.Label(ventana, text="")
label_resultado3.pack(pady=5)

#HemoloblinaH
def mostrar_resultadoH():
    try:
        nivel_hom = float(entryh.get())
        resultadoh = verificar_niveles_hemoglobinaH(nivel_hom)
        label_resultadoh.config(text="Su hemoloblina es: " + resultadoh)
    except ValueError:
        label_resultadoh.config(text="Por favor, ingrese un número válido.")

label_instruccionesh = tk.Label(ventana, text="Ingrese su hemolobilna(para hombres):")
label_instruccionesh.pack(pady=5)


entryh = tk.Entry(ventana)
entryh.pack(pady=5)


boton_verificarh = tk.Button(ventana, text="Verificar", command=mostrar_resultadoH)
boton_verificarh.pack(pady=5)


label_resultadoh = tk.Label(ventana, text="")
label_resultadoh.pack(pady=5)

#HemoloblinaM
def mostrar_resultadoM():
    try:
        nivel_M = float(entrym.get())
        resultadom= verificar_niveles_hemoglobinaM(nivel_M)
        label_resultadom.config(text="Su hemoloblina es: " + resultadom)
    except ValueError:
        label_resultadoh.config(text="Por favor, ingrese un número válido.")

label_instruccionesm = tk.Label(ventana, text="Ingrese su hemolobilna(para mujeres):")
label_instruccionesm.pack(pady=5)


entrym = tk.Entry(ventana)
entrym.pack(pady=5)


boton_verificarm = tk.Button(ventana, text="Verificar", command=mostrar_resultadoM)
boton_verificarm.pack(pady=5)


label_resultadom = tk.Label(ventana, text="")
label_resultadom.pack(pady=5)
ventana.mainloop()