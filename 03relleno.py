from tkinter import *
import ast
from utilitarios import TextWithVar, cifrado_relleno_una_vez

window = Tk()
window.title("Seguridad informática | Relleno")
window.geometry("600x600")

frame = Frame(window)
frame.pack()

texto1 = StringVar()
salto1 = StringVar()
codificado = StringVar()

texto2 = StringVar()
salto2 = StringVar()
decodificado = StringVar()


def boton_codificar():
    r1, r2, r3 = cifrado_relleno_una_vez(texto1.get(), salto1.get())
    codificado.set(f"{r1} \n{r2} \n{r3}")


def boton_decodificar():
    r1, r2, r3 = cifrado_relleno_una_vez(texto2.get(), salto2.get())
    decodificado.set(f"{r1} \n{r2} \n{r3}")


# Cifrado
l1 = Label(frame, text="Texto a cifrar").grid(row=0, column=0)
i1 = TextWithVar(frame, height=5, width=50, textvariable=texto1).grid(row=0, column=1)

l2 = Label(frame, text="Relleno").grid(row=1, column=0)
i2 = Entry(frame, textvariable=salto1, width=30).grid(row=1, column=1)

button_cifrar = Button(frame, text="Primera vez", width=10, command=lambda: boton_codificar()).grid(row=3, column=1)

l3 = Label(frame, text="Resultado cifrado").grid(row=4, column=0)
r1 = TextWithVar(frame, height=3, width=50, textvariable=codificado).grid(row=4, column=1)

divisor = "***"
e2 = Label(frame, text=f"{divisor*20}").grid(row=5, column=0, columnspan=2, pady=80)


# Descifrado
l4 = Label(frame, text="Texto a descifrar").grid(row=6, column=0)
i4 = TextWithVar(frame, height=5, width=50, textvariable=texto2).grid(row=6, column=1)

l5 = Label(frame, text="Salto").grid(row=7, column=0)
i5 = Entry(frame, textvariable=salto2, width=30).grid(row=7, column=1)

button_descifrar = Button(frame, text="Segunda vez", width=10, command=lambda: boton_decodificar()).grid(
    row=8, column=1
)

l6 = Label(frame, text="Resultado descrifrado").grid(row=9, column=0)
r2 = TextWithVar(frame, height=3, width=50, textvariable=decodificado).grid(row=9, column=1)

window.mainloop()

# Ejemplo
# "I love you."
# "RKrURcc*Wf+"
