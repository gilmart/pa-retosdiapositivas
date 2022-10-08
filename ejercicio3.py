# ---------- RETOS DIAPOSITIVA 1 ----------
#3. Recibir dos números y determinar cual es mayor
numero1=int(input('Digite el numero 1: '))
numero2=int(input('Digite el numero 2: '))

if(numero1==numero2):
    print(f'El numeros {numero1} y {numero2} son iguales')
elif(numero1>numero2):
    print(f'El numero {numero1} es mayor que numero {numero2}')
elif(numero2>numero1):
    print(f'Numero {numero2} es mayor que numero {numero1}')
else:
   print('digite un numero correcto')