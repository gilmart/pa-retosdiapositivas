# ---------- RETOS DIAPOSITIVA 1 ----------
#2. Recibir un numero en teclado y determinar si este es múltiplo de 3
numero=int(input('Digite un numero: '))
resultado=numero%3

if(resultado == 0):
    print(f'El numero {numero} es multiplo de 3' )
elif(resultado != 0):
    print(f'El numero {numero} no es multiplo de 3')