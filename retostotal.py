# ---------- RETOS DIAPOSITIVA 1 ----------
#1. Recibir un numero en teclado y determinar si este es múltiplo de 5
'''
numero=int(input('Digite un numero: '))
resultado=numero%5

if(resultado == 0):
    print(f'El numero {numero} es multiplo de 5' )
elif(resultado != 0):
    print(f'El numero {numero} no es multiplo de 5')
'''
#2. Recibir un numero en teclado y determinar si este es múltiplo de 3
'''
numero=int(input('Digite un numero: '))
resultado=numero%3

if(resultado == 0):
    print(f'El numero {numero} es multiplo de 3' )
elif(resultado != 0):
    print(f'El numero {numero} no es multiplo de 3')
'''
#3. Recibir dos números y determinar cual es mayor
'''
numero1=int(input('Digite el numero 1: '))
numero2=int(input('Digite el numero 2: '))

if(numero1==numero2):
    print(f'El numeros {numero1} y {numero2} son iguales')
elif(numero1>numero2):
    print(f'El numero {numero1} es mayor que numero {numero2}')
elif(numero2>numero1):
    print(f'Numero {numero2} es mayor que numero {numero1}')
else:
    'digite un numero correcto'
'''
#4. Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de
#lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?
'''
juan=int(input('digite la cantidad de dinero que posee Juan: '))
camila=juan/2
ricardo=juan/2+camila/2

print(f'Juan tiene: {juan}')
print(f'Camila tiene: {camila}')
print(f'Ricardo tiene: {ricardo}')
'''
#5. Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 
# por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. 
# Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas
'''
salarioMensual=3500000
comisionLicSoftware=1500000
numLicVendidas=int(input('Ingrese el numero de licencias vendidas en este mes: '))

resultado= (salarioMensual + (comisionLicSoftware*numLicVendidas))*0.95
print(f'El numero de licencias vendidas fue: {numLicVendidas} y su salario mensual es de: {resultado}')
'''
# ---------- RETOS DIAPOSITIVA 2 ----------
#1. Construir un programa que reciba números enteros y los sume mientras estos sean positivos, si se digita un número negativo el programa debe terminar
'''
numero=int(input('Digite un numero: '))
suma=0
while (numero >= 0):
    suma=suma+numero
    numero=int(input('Digite el siguiente numero: '))
else:
    print(f'la suma de los numeros fue {suma}')
'''

#2. Codificar un programa que presente un menú de 4 opciones y reciba un numero natural para realizar las siguientes operaciones:
#0: Salida
#1: Encuentre si el número es múltiplo de 2
#2: Encuentre la raíz cuadrada del número
#3: Sume 100 al número ingresado
#4: Eleve a la 2 el número ingresado
'''
numeroOpcion= None
resultado=None

print('**MENU**')
print('0: SALIR')
print('1: Encuentre si el número es múltiplo de 2')
print('2: Encuentre la raíz cuadrada del número')
print('3: Sume 100 al número ingresado')
print('4: Eleve a la 2 el número ingresado')


while(numeroOpcion !=0):
   numeroOpcion=int(input('Digite una opcion:'))
   if(numeroOpcion == 0):
        break
   elif(numeroOpcion==1):
    resultado=int(input('Ingrese el numero al que desea encontrar el multiplo: '))
    resultado=resultado%2
    if(resultado==0):
        print(f'El numero ingresado es multiplo de 2')
    else:
        print(f'El numero no es multiplo de 2')
   elif(numeroOpcion==2):
    resultado=int(input('Ingrese el numero al que desea calcular la raiz cuadrada: '))
    resultado=resultado**(1/3)
    print(f'La raiz cuadrada es: {resultado}')
   elif(numeroOpcion==3):
    resultado=int(input('Ingrese el numero al que desea suma 100: '))
    resultado=resultado+100
    print(f'El resultado fue {resultado}')
   elif(numeroOpcion==4):
    resultado=int(input('Ingrese el numero al que desea elevar a la 2: '))
    resultado=resultado**2
    print(f'El resultado del numero elevado a la 2 es: {resultado}')
   elif(numeroOpcion >= 5 or numeroOpcion<0):
    print('Opcion invalide, digite un numero correcto')
else:
    ('Terminado')
'''
#3. Mostrar los números del 1 al 200 saltando de 12 en 12(12,24,36…)
'''
for tabla12 in range(0,205,12):
    print(tabla12)
'''
#4. Pedir 20 números y contar cuantos de los ingresados fueron negativos
'''
dato=1
numerosNeg=0

while(dato <= 20):
    numero = int(input(f'Ingrese el numero {dato}: '))
    dato=dato+1
    if(numero <0 ):
        numerosNeg= numerosNeg+1
else:
    print(f'La cantidad de numeros negativos es: {numerosNeg}')
    print('Terminado')
'''
# ---------- RETOS DIAPOSITIVA 3 ----------
#1.Construir un programa que reciba el tamaño de una lista y la llene con múltiplos de 7
'''
import random
listas=[]
listaTamaño=int(input('Digite el tamaño de la lista: '))
for lista in range(listaTamaño):
    listas=[]
    listas.insert(lista, random.randrange(7,100,7))
    print(lista)
    print(listas)
'''
#Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario
'''
suma=1
listas=[]
sizeLista=int(input('digite el tamaño de la lista: '))
for lista in range(sizeLista):
    listas.append(input(f"numero {suma}: "))
    suma+=1

print(listas)
'''
#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en #orden inverso los datos ingresados
'''
listaCiudades=[]
suma=1

for lista in range(8):
    listaCiudades.append(input(f'ingrese la ciudad #{suma}: '))
    suma+=1
for lista in listaCiudades[::-1]:  
    print(lista)
'''
#Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso
'''
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
    '''
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


lista=[] 
tupla=(50,45,20,30,40,87,40)
for num in tupla:
    res=num
    if res >= 40:
        lista.append(res)
print(lista)

listaP=[] 
tuplaP=(50,45,20,30,40,87,40)
for num in tuplaP:
    resP=num
    resP=resP%2
    if resP ==0:
        listaP.append(num)
print(resP)

lista1=[] 
tupla1=(50,45,20,30,40,87,40)
for num in tupla:
    res=num
    if res >= 40:
        lista.append(res)
print(lista1)

