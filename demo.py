tt = "pleasetransferonemilliondollarstomyswissbankaccountsixtwotwo"
pss = "MEGABUCK"
import random
from string import ascii_letters


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
    print("binarios resultado", [bin(num) for num in resultado_int])
    resultado_lista = [chr(num) for num in resultado_int]
    resultado_str = "".join(resultado_lista)
    return resultado_int, resultado_str


def cifrado_relleno_segunda_vez(lista_n: list, relleno: str):
    len_txt = len(lista_n)
    n_txt_base = lista_n
    n_txt_relleno = text_to_array_number(relleno)
    resultado_int = []
    print("binarios texto", [bin(num) for num in n_txt_base])
    print("binarios segundo relleno", [bin(num) for num in n_txt_relleno])
    for i in range(len_txt):
        resultado_int.append(n_txt_base[i] ^ n_txt_relleno[i])
    print([bin(num) for num in resultado_int])
    resultado_lista = [chr(num) for num in resultado_int]
    resultado_str = "".join(resultado_lista)
    return resultado_int, resultado_str


r1, r2 = cifrado_relleno_una_vez("I love you.", "RKrURcc*Wf+")

p1, p2 = cifrado_relleno_segunda_vez(r1, "RKrURcc*Wf+")

print(p2)