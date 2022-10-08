# ---------- RETOS EN CLASES ----------

#DATOS EMPANADA
#Sabor
#Ingredientes (x3)
#Precio Fabircación
#Precio venta

print("***MENU***")
print("1. Agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. SALIR")
opcion=100

empanadas=[]
suma=1

while(opcion != 3):
    empanada={}
    opcion=int(input('Digite una opcion: '))
    if(opcion == 1):
        empanada['sabor']=input('digite el sabor: ')
        empanada['ingredientes']=[]
        for centinela in range(3):
            empanada['ingredientes'].append(input(f'digite el ingrediente: {suma} '))
            suma+=1
        empanada['precioF']=int(input('digite el precio de fabricacion: '))
        empanada['precioV']=int(input('digite el precio de venta: '))
        empanadas.append(empanada)
    if(opcion == 2):
        print(empanadas)
