# ---------- RETOS DIAPOSITIVA 2 ----------
#1. Construir un programa que reciba números enteros y los sume mientras estos sean positivos, si se digita un número negativo el programa debe terminar

numero=int(input('Digite un numero: '))
suma=0
while (numero >= 0):
    suma=suma+numero
    numero=int(input('Digite el siguiente numero: '))
else:
    print(f'la suma de los numeros fue {suma}')