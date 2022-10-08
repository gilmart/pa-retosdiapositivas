#Construir un programa para ir de compras a un supermercado que permita la construccion del siguiente menu:
# 1. Digitar 1 para recibir codigo, nombre y precio de un producto
# 2. Digitar 2 para mostrar los productos
# 3. Digitar 3 para buscar y editar un producto por codigo
# 4. Digitar 4 para buscar y eliminar producto por codigo

print("***MENU***")
print("1. Recibir codigo, nombre y precio de un producto")
print("2. Mostrar los productos")
print("3. Buscar y editar un producto por codigo")
print("4. Buscar y eliminar producto por codigo")
print("5. SALIR")

opcion=100

class Producto: 
    codigo=None
    nombre=None
    precio=None

while(opcion !=5):
    opcion=int(input('Digite una opcion: '))
    if(opcion ==1):  
        codigo=int(input(f'Digite el codigo del producto :'))
        nombre=(input(f'Digite el nombre del producto: '))
        precio=int(input(f'Digite el precio del producto: '))
        articulo=Producto(codigo,nombre,precio)
print(Producto)