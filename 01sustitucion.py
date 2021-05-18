from tkinter import *
from utilitarios import TextWithVar, codificar_sustitucion, decodificar_sustitucion

window = Tk()
window.title("Seguridad informática | Sustitución")
window.geometry("600x600")

frame = Frame(window)
frame.pack()

texto1 = StringVar()
salto1 = IntVar()
codificado = StringVar()

texto2 = StringVar()
salto2 = IntVar()
decodificado = StringVar()


def boton_codificar():
    codificado.set(codificar_sustitucion(texto1.get(), salto1.get()))


def boton_decodificar():
    decodificado.set(decodificar_sustitucion(texto2.get(), salto2.get()))


# Cifrado
l1 = Label(frame, text="Texto a cifrar").grid(row=1, column=0)
i1 = TextWithVar(frame, height=5, width=50, textvariable=texto1).grid(row=1, column=1)

l2 = Label(frame, text="Salto").grid(row=2, column=0)
i2 = Entry(frame, textvariable=salto1).grid(row=2, column=1)

button_cifrar = Button(frame, text="Cifrar", width=5, command=lambda: boton_codificar()).grid(row=3, column=1)

l3 = Label(frame, text="Resultado cifrado").grid(row=4, column=0)
r1 = TextWithVar(frame, height=3, width=50, textvariable=codificado).grid(row=4, column=1)


divisor = "***"
e2 = Label(frame, text=f"{divisor*20}").grid(row=5, column=0, columnspan=2, pady=80)


# Descifrado
l4 = Label(frame, text="Texto a descifrar").grid(row=6, column=0)
i4 = TextWithVar(frame, height=5, width=50, textvariable=texto2).grid(row=6, column=1)

l5 = Label(frame, text="Salto").grid(row=7, column=0)
i5 = Entry(frame, textvariable=salto2).grid(row=7, column=1)

button_descifrar = Button(frame, text="Desifrar", width=5, command=lambda: boton_decodificar()).grid(row=8, column=1)

l6 = Label(frame, text="Resultado descrifrado").grid(row=9, column=0)
r2 = TextWithVar(frame, height=3, width=50, textvariable=decodificado).grid(row=9, column=1)

window.mainloop()

# Ejemplo
# "ataque"
# 3