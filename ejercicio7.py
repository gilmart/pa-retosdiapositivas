# ---------- RETOS DIAPOSITIVA 2 ----------

#2. Codificar un programa que presente un menú de 4 opciones y reciba un numero natural para realizar las siguientes operaciones:
#0: Salida
#1: Encuentre si el número es múltiplo de 2
#2: Encuentre la raíz cuadrada del número
#3: Sume 100 al número ingresado
#4: Eleve a la 2 el número ingresado

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