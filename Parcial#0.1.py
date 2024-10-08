def ordenar (list1,list2):
    list3=list1+list2
    list4=[]
    indice=0
    menor=0
    i=0
    while i<len(list3):
        menor=list3[i]
        indice=i
        for j in range(len(list3)):
            if list3[j]<menor:
                menor=list3[j]
                indice=j
        list4.append(menor)
        del list3[indice]
        i=0
                
    return list4

print(ordenar([1,2,4,5,0],[1,3,4,9]))