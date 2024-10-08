def heights_diferente(heights,expected):
    diferentes=0
    indice=[]
    for i in range(len(heights)):
        if heights[i]!=expected[i]:
            diferentes+=1
            indice.append(i)
    for i in range(len(indice)):
        print('Expected es diferente a heights en la posición {0}'.format(indice[i]))
    x=print('Hay',diferentes,'diferentes')
    return x

print(heights_diferente([1,0,4,2,1,3],[1,1,1,2,3,9]))

