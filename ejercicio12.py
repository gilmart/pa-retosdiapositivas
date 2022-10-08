# ---------- RETOS DIAPOSITIVA 3 ----------
#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en #orden inverso los datos ingresados

listaCiudades=[]
suma=1

for lista in range(8):
    listaCiudades.append(input(f'ingrese la ciudad #{suma}: '))
    suma+=1
for lista in listaCiudades[::-1]:  
    print(lista)