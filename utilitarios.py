import tkinter as tk
from string import ascii_lowercase
import math


class TextWithVar(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        try:
            self._textvariable = kwargs.pop("textvariable")
        except KeyError:
            self._textvariable = None

        tk.Text.__init__(self, parent, *args, **kwargs)

        # if the variable has data in it, use it to initialize
        # the widget
        if self._textvariable is not None:
            self.insert("1.0", self._textvariable.get())

        # this defines an internal proxy which generates a
        # virtual event whenever text is inserted or deleted
        self.tk.eval(
            """
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                # return the result from the real widget command
                return $result
            }
            """
        )

        # this replaces the underlying widget with the proxy
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        """.format(
                widget=str(self)
            )
        )

        # set up a binding to update the variable whenever
        # the widget changes
        self.bind("<<Change>>", self._on_widget_change)

        # set up a trace to update the text widget when the
        # variable changes
        if self._textvariable is not None:
            self._textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *args):
        """Change the text widget when the associated textvariable changes"""

        # only change the widget if something actually
        # changed, otherwise we'll get into an endless
        # loop
        text_current = self.get("1.0", "end-1c")
        var_current = self._textvariable.get()
        if text_current != var_current:
            self.delete("1.0", "end")
            self.insert("1.0", var_current)

    def _on_widget_change(self, event=None):
        """Change the variable when the widget changes"""
        if self._textvariable is not None:
            self._textvariable.set(self.get("1.0", "end-1c"))


# Sustitución
def codificar_sustitucion(texto: str, salto: int):
    mensaje = texto.lower()
    alfabeto = ascii_lowercase
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == "ñ":
            codificado += letra
            continue
        valor_letra = ord(letra)
        limite = 97
        posicion = (valor_letra - limite + salto) % longitud_alfabeto
        codificado += alfabeto[posicion]
    return codificado.upper()


def decodificar_sustitucion(texto: str, salto: int):
    mensaje = texto.lower()
    alfabeto = ascii_lowercase
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == "ñ":
            decodificado += letra
            continue
        valor_letra = ord(letra)
        limite = 97
        posicion = (valor_letra - limite - salto) % longitud_alfabeto
        decodificado += alfabeto[posicion]
    return decodificado


# Transposición
def codificar_transposicion(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    # calculate column of the matrix
    col = len(key)
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
    # add the padding character '?' in empty
    # the empty cell of the matix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend("?" * fill_null)
    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i : i + col] for i in range(0, len(msg_lst), col)]
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += "".join([row[curr_idx] for row in matrix])
        k_indx += 1
    lista_texto_plano = [(msg[i : i + col]) for i in range(0, len(msg), col)]
    for ltp in lista_texto_plano:
        print(ltp)
    return cipher


def decodificar_transposicion(cipher, key):
    msg = ""
    # track key indices
    k_indx = 0
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    # calculate column of the matrix
    col = len(key)
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    # convert decrypted msg matrix into a string
    try:
        msg = "".join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")
    null_count = msg.count("?")
    if null_count > 0:
        return msg[:-null_count]
    return msg


# Relleno
def text_to_array_number(text: str):
    lista_char = [char for char in text]
    return [ord(num) for num in lista_char]


def cifrado_relleno_una_vez(text: str, relleno: str):
    len_txt = len(text)
    n_txt_base = text_to_array_number(text)
    n_txt_relleno = text_to_array_number(relleno)
    resultado_int = []
    print("binarios texto", [bin(num) for num in n_txt_base])
    print("binarios relleno", [bin(num) for num in n_txt_relleno])
    for i in range(len_txt):
        resultado_int.append(n_txt_base[i] ^ n_txt_relleno[i])
    resultado_bin = [bin(num) for num in resultado_int]
    print("binarios resultado", resultado_bin)
    print("\n")
    resultado_lista = [chr(num) for num in resultado_int]
    resultado_str = "".join(resultado_lista)
    return resultado_str, resultado_int, resultado_bin


# Polialfabético
def cifrado_polialfabetico(texto: str, k1: int, k2: int, orden: list):
    if len(texto) % len(orden) == 0:
        orden *= len(texto) // len(orden)
        id_orden = 0
        resultado = []
        for char in texto:
            k = k1 if orden[id_orden] == 1 else k2
            resultado.append(codificar_sustitucion(char, k))
            id_orden += 1
        return "".join(var for var in resultado)
    else:
        raise Exception("orden no divisible por el texto")


def descifrado_polialfabetico(texto: str, k1: int, k2: int, orden: list):
    if len(texto) % len(orden) == 0:
        orden *= len(texto) // len(orden)
        id_orden = 0
        resultado = []
        for char in texto:
            k = k1 if orden[id_orden] == 1 else k2
            resultado.append(decodificar_sustitucion(char, k))
            id_orden += 1
        return "".join(var for var in resultado)
    else:
        raise Exception("orden no divisible por el texto")