# ---------- RETOS DIAPOSITIVA 3 ----------

#Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso

listaNum=[]
suma=1
for num in range (4):
    listaNum.append(int(input(f'digite el numero #{suma}: ')))
    suma+=1
buscarNumero=int(input('digite el numero q quiere buscar: '))
if(listaNum.index(buscarNumero)):
    print(f'encontrado en la posicion'.format(buscarNumero))
else:
    print(f'numero no encontrado')
    
    
listaNum=[]
suma=1
for num in range (4):
    listaNum.append(int(input(f'digite el numero #{suma}: ')))
    suma+=1
buscarNumero=int(input('digite el numero q quiere buscar: '))
if(buscarNumero in listaNum):
    print(f'encontrado en la posicion {listaNum.index(buscarNumero)}' )
else:
    print(f'numero no encontrado')