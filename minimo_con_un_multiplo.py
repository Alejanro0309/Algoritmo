#minimo con un multiplon

n1=input('escriba un numero: ')
n2=input('escriba un numero: ')
list=[]
ciclo=0
while not n1.isnumeric() and n2.isnumeric():
    print('error')
    n1=input('escriba un numero: ')
    n2=input('escriba un numero: ')
n1=int(n1)
n2=int(n2)

n3=n1*n2

temporal = 0
while n2 != 0:
    temporal = n2
    n2 = n1 % n2
    n1 = temporal


x=int(n3 / n1)

print(x)