# ---------- RETOS DIAPOSITIVA 4 ----------

lista=[] 
tupla=(50,45,20,30,40,87,40)
for num in tupla:
    res=num
    if res >= 40:
        lista.append(res)
print(lista)




### test !!
listaP=[] 
tuplaP=(50,45,20,30,40,87,40)
for num in tuplaP:
    resP=num
    resP=resP%2
    if resP ==0:
        listaP.append(num)
print(resP)