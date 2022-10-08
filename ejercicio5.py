# ---------- RETOS DIAPOSITIVA 1 ----------
#5. Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 
# por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. 
# Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas

salarioMensual=3500000
comisionLicSoftware=1500000
numLicVendidas=int(input('Ingrese el numero de licencias vendidas en este mes: '))

resultado= (salarioMensual + (comisionLicSoftware*numLicVendidas))*0.95
print(f'El numero de licencias vendidas fue: {numLicVendidas} y su salario mensual es de: {resultado}')