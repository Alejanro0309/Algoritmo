def letra_unica(lista,k):
    letras_lista=[]
    dic={}
    for i in range(len(lista)):
        conteo=lista.count(lista[i]) 
        if conteo==1:
            letras_lista.append(lista[i])
    l=len(letras_lista)
    if l<k:
        r=''
    else:
        r=letras_lista[k-1]

    return r


print(letra_unica(["d","b","c","b","c","a"],2))