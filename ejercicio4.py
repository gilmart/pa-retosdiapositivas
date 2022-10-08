# ---------- RETOS DIAPOSITIVA 1 ----------
#4. Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de
#lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?
juan=int(input('digite la cantidad de dinero que posee Juan: '))
camila=juan/2
ricardo=juan/2+camila/2

print(f'Juan tiene: {juan}')
print(f'Camila tiene: {camila}')
print(f'Ricardo tiene: {ricardo}')