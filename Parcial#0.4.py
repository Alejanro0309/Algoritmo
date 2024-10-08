def valor_obj(lista,num):
    lista.sort()
    contantador=0
    r=-1
    for i in range(len(lista)):
        if lista[i]==num:
            return i
    lista.append(num)
    lista.sort()

    for j in range(len(lista)):
        if lista[j]==num:
            return j
     


print(valor_obj([1,3,5,6],7))