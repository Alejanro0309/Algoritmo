numero="11001"
numero_volteado=numero[::-1]
resultado=0
for i in range(len(numero)):
    if numero_volteado[i]=="1":
        resultado+=2**i
print(resultado)