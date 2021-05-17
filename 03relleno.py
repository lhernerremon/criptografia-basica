from tkinter import *
import ast
from utilitarios import TextWithVar, cifrado_relleno_una_vez, cifrado_relleno_segunda_vez

window = Tk()
window.title("Seguridad informática | Relleno")
window.geometry("800x600")

frame = Frame(window)
frame.pack()

texto1 = StringVar()
salto1 = StringVar()
codificado = StringVar()

texto2 = StringVar()
salto2 = StringVar()
decodificado = StringVar()


def boton_codificar():
    r1, r2 = cifrado_relleno_una_vez(texto1.get(), salto1.get())
    codificado.set(f"{r2} \n{r1}")


def boton_decodificar():
    r1, r2 = cifrado_relleno_segunda_vez(ast.literal_eval(texto2.get()), salto2.get())
    decodificado.set(r2)


# Cifrado

l1 = Label(frame, text="Texto a cifrar").grid(row=1, column=0)
i1 = TextWithVar(frame, height=5, width=50, textvariable=texto1).grid(row=1, column=2)

l2 = Label(frame, text="Relleno").grid(row=1, column=4)
i2 = Entry(frame, textvariable=salto1).grid(row=1, column=5)

button_cifrar = Button(frame, text="Primera vez", width=10, command=lambda: boton_codificar()).grid(row=3, column=2)

l3 = Label(frame, text="Resultado cifrado").grid(row=4, column=0)
r1 = TextWithVar(frame, height=3, width=50, textvariable=codificado).grid(row=4, column=2, columnspan=5)


e2 = Label(frame, text="-------------------------------------------------------------------").grid(
    row=5, column=0, columnspan=6, pady=80
)


# Descifrado
l4 = Label(frame, text="Texto a descifrar").grid(row=7, column=0)
i4 = TextWithVar(frame, height=5, width=50, textvariable=texto2).grid(row=7, column=2)

l5 = Label(frame, text="Salto").grid(row=7, column=4)
i5 = Entry(frame, textvariable=salto2).grid(row=7, column=5)

button_descifrar = Button(frame, text="Segunda vez", width=10, command=lambda: boton_decodificar()).grid(
    row=9, column=2
)

l6 = Label(frame, text="Resultado descrifrado").grid(row=10, column=0)
r2 = TextWithVar(frame, height=3, width=50, textvariable=decodificado).grid(row=10, column=2, columnspan=5)


window.mainloop()