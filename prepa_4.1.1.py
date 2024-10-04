pares = [2, 3, 4, 7, 3, 5]
m1=pares[:int(len(pares)/2)]
m2=pares[int(len(pares)/2):][::-1]
resultados=[]

for i in range(len(m1)):
    x=m1[i]+m2[i]
    resultados.append(x)
print(resultados)