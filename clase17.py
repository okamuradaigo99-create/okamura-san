import tkinter as tk

edades = 18
def edad():
    edad = int (entrada.get())
    if edad < edades:
        print("eres menor de edad")
    else:
        print("eres mayor de edad")

ventana = tk.Tk()
ventana.title("eres mayor de edad?")
ventana.geometry("300x300")

tk.Label(ventana , text="escribe tu edad:") .pack()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana , text="pulsa aqui",command=edad).pack()
resultado = tk.Label(ventana , text="Escribe tu edad")
resultado.pack()

tk.mainloop()
