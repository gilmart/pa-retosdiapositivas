# ---------- RETOS DIAPOSITIVA 2 ----------

#4. Pedir 20 números y contar cuantos de los ingresados fueron negativos

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
