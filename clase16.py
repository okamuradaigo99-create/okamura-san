import tkinter as tk

def grado():
    grados=float(entrada.get())
    far = grados *9/5 +32
    print (far)

ventana = tk.Tk()
ventana.title("celsius a fahrenheit")
ventana.geometry("300x300")

tk.Label(ventana , text="celsius a fharenheit:") .pack()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana , text="grados",command=grado).pack()
resultado = tk.Label(ventana , text="Escribe y pulsa probar")
resultado.pack()

tk.mainloop()


