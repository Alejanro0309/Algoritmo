'''n=int(input("Que numero le quieres calcular el factorial: "))

resultado=1
for i in range(1,n+1):
    resultado=i*resultado
    print("factorial en",i,"es",resultado)
print("Y finalmente, el factorial de",n,"es",resultado)'''

'''n=int(input("Que numero le quieres calcular el factorial: "))

resultado=1
for i in range(n,0,-1):
    resultado=i*resultado
    print("factorial en",i,"es",resultado)
print("Y finalmente, el factorial de",n,"es",resultado)'''

'''ciudad=['caracas','valencia','maragarita']
ciudad[0]="aragua"

cuidad2=['bolivar','amazonas','barinas']
ciudad3=ciudad+cuidad2
del ciudad3[0]
ciudad3.sort()
print(ciudad3)
for i in range(len(ciudad3)):
    print("me voy a",i,"es",ciudad3[i])'''

'''x=('a','b','c')
v=('a','b','c')

t=1,"uno"
x,y=t
print(x,y)

r=([1,2,3],['uno','dos','tres'])
r[0][0]=4

for i in range(len(r)):
    for j in range(len(r[i])):
        print('i es',i,'y j es',j,':',r[i][j])'''

cesta={'fruta','manzana','pera','naranja'}
ciudad={'caracas','valencia','maragarita'}
y=cesta | {'fresa'}
print(y)

''''tel={'jack':3004,"maria":9002}
tel=list(tel)
print(tel)

for i in range(len(tel)):
    print(tel[i])'''

