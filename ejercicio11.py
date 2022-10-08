# ---------- RETOS DIAPOSITIVA 3 ----------

#Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

suma=1
listas=[]
sizeLista=int(input('digite el tamaño de la lista: '))
for lista in range(sizeLista):
    listas.append(input(f"numero {suma}: "))
    suma+=1

print(listas)