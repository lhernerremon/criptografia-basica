from tkinter import *
import ast
from utilitarios import TextWithVar, cifrado_polialfabetico, descifrado_polialfabetico

window = Tk()
window.title("Seguridad informática | Polialfabético")
window.geometry("600x700")

frame = Frame(window)
frame.pack()

texto1 = StringVar()
k1 = IntVar()
k2 = IntVar()
lista1 = StringVar()
codificado = StringVar()

texto2 = StringVar()
k3 = IntVar()
k4 = IntVar()
lista2 = StringVar()
decodificado = StringVar()


def boton_codificar():
    resultado_str = cifrado_polialfabetico(texto1.get(), k1.get(), k2.get(), ast.literal_eval(lista1.get()))
    codificado.set(resultado_str)


def boton_decodificar():
    resultado_str = descifrado_polialfabetico(texto2.get(), k3.get(), k4.get(), ast.literal_eval(lista2.get()))
    decodificado.set(resultado_str)


# Cifrado
l1 = Label(frame, text="Texto a cifrar").grid(row=0, column=0)
i1 = TextWithVar(frame, height=5, width=50, textvariable=texto1).grid(row=0, column=1)

l2 = Label(frame, text="k1").grid(row=1, column=0)
i2 = Entry(frame, textvariable=k1).grid(row=1, column=1)

l3 = Label(frame, text="k2").grid(row=2, column=0)
i3 = Entry(frame, textvariable=k2).grid(row=2, column=1)

l4 = Label(frame, text="Patron (lista)").grid(row=3, column=0)
i4 = Entry(frame, textvariable=lista1).grid(row=3, column=1)

button_cifrar = Button(frame, text="Cifrar", width=5, command=lambda: boton_codificar()).grid(
    row=4, column=0, columnspan=2
)

ll1 = Label(frame, text="Resultado cifrado").grid(row=5, column=0)
r1 = TextWithVar(frame, height=3, width=50, textvariable=codificado).grid(row=5, column=1)


divisor = "***"
e2 = Label(frame, text=f"{divisor*20}").grid(row=6, column=0, columnspan=2, pady=80)


# Descifrado
l5 = Label(frame, text="Texto a descifrar").grid(row=7, column=0)
i5 = TextWithVar(frame, height=5, width=50, textvariable=texto2).grid(row=7, column=1)

l6 = Label(frame, text="k1").grid(row=8, column=0)
i6 = Entry(frame, textvariable=k3).grid(row=8, column=1)

l7 = Label(frame, text="k2").grid(row=9, column=0)
i7 = Entry(frame, textvariable=k4).grid(row=9, column=1)

l8 = Label(frame, text="Patron (lista)").grid(row=10, column=0)
i8 = Entry(frame, textvariable=lista2).grid(row=10, column=1)

button_cifrar = Button(frame, text="Descifrar", width=5, command=lambda: boton_decodificar()).grid(
    row=11, column=0, columnspan=2
)

ll2 = Label(frame, text="Resultado descifrado").grid(row=12, column=0)
r1 = TextWithVar(frame, height=3, width=50, textvariable=decodificado).grid(row=12, column=1)

window.mainloop()

# Ejemplo
# "benito, te quiero."
# k1=5
# k2 = 19
# [1, 1, 2, 1, 2]
