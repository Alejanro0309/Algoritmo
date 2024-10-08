def metro_encoding(lista):
    i=0
    if len(lista)%2==0:
        lista2=[]
        while i<len(lista):
            f=lista[i]
            v=lista[i+1]
            for i in range(f):
                lista2.append(v)
            i+=2
    else:
        r=('error')
        return r
    return lista2
print(metro_encoding([1,2,3,4]))