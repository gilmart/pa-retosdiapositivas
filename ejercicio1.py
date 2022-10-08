# ---------- RETOS DIAPOSITIVA 1 ----------
#1. Recibir un numero en teclado y determinar si este es múltiplo de 5
numero=int(input('Digite un numero: '))
resultado=numero%5

if(resultado == 0):
    print(f'El numero {numero} es multiplo de 5' )
elif(resultado != 0):
    print(f'El numero {numero} no es multiplo de 5')
