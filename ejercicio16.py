#El Valle de Aburra afronta altas temperaturas año tras año, cree una q perimta calcular la temperarua media de la tierra a partir de recibir 20 datos diarios de tempratura

def calcularTemperaturas(temperaturas):
    suma=0
    for num in range(len(temperaturas)):
        suma+=temperaturas[num]
        totalTemp=suma/4
    print(temperaturas)
    print(totalTemp)
    print(f'la temperatura del día fue: {suma}' )


i=1
temperaturas=[]
for i in range(4):
    temperatura=int(input(f'ingrese la temperatura {i+1} ' ))
    i=i+1
    temperaturas.append(temperatura)

calcularTemperaturas(temperaturas)
