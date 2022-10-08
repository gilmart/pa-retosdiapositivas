def calcularArea(ancho, largo):
    area=ancho*largo
    return area

def calcularPerimetro(ancho, largo):
    perimetro=ancho*2 + largo*2
    return perimetro

def graficarRectangulo(ancho,largo):
    ancho*'*'
    largo*'*'

ancho=int(input(f"ingrese el ancho: "))
largo=int(input(f"ingrese el largo: "))

print(calcularArea(ancho,largo))
print(calcularPerimetro(ancho,largo))
print(graficarRectangulo(ancho,largo))

