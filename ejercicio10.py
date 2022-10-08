# ---------- RETOS DIAPOSITIVA 3 ----------
#1.Construir un programa que reciba el tamaño de una lista y la llene con múltiplos de 7

import random
listas=[]
listaTamaño=int(input('Digite el tamaño de la lista: '))
for lista in range(listaTamaño):
    listas=[]
    listas.insert(lista, random.randrange(7,100,7))
    print(lista)
    print(listas)
