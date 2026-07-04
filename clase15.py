import tkinter as tk 
import random



secreto = random.randint(1,100)
intentos = 0



def adivinar():
    global intentos
    intentos = int(entrada.get())
    intentos+= 1


    intentos = int (entrada.get())
    if intentos <secreto:
        resultado["text"] = "muy bajo . MAS ALTO"
    elif intentos > secreto:
        resultado["text"] = "muy alto . MAS BAJO"
    else:
        resultado["text"] = f"correcto en {intentos}."
    entrada.delete(0,tk.END)


ventana = tk.Tk()
ventana.title("adivina el numero")
ventana.geometry("500x500")

tk.Label(ventana , text="Adivina (1-100):") .pack()

entrada = tk.Entry(ventana)
entrada.pack()
tk.Button(ventana, text="probar" , command=adivinar).pack()

resultado = tk.Label(ventana , text="Escribe y pulsa probar")
resultado.pack()

tk.mainloop()
