tamañoLista=int(input(f'Digite la cantidad de numeros que deseas ingresar: '))

listaNumeros=[]
for i in range(tamañoLista):
   numerosParaLaLista=int(input(f'Digite el numero {i+1}:'))
   listaNumeros.append(numerosParaLaLista)
   i+=1
print(tamañoLista)
print(listaNumeros)


#Crea una funcion que reciba una lista con valores numericos y devuelva el valor maximo y el minimo ingresados

def calcularValor(listaNumeros):
    min = max = listaNumeros[0]
    for valor in listaNumeros:
        if valor<min:
            min=valor
        elif valor > max:
            max = valor
    print(min)
    print(max)

calcularValor(listaNumeros)

