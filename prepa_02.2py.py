#Diccionarios
numeros={"Primero":1,"Segundo":2,"Tercero":3}
print(numeros["Tercero"])

numeros["Primero"]=0
numeros["Segundo"]-1
print(numeros)

for clave,valor in numeros.items():
    print(clave,valor)
