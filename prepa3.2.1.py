numero1=220
numero2=284
divisores1=[]
divisores2=[]

for divisor in range(1,numero1):
    if numero1 % divisor==0:
        divisores1.append(divisor)

for divisor in range(1,numero2):
    if numero2 % divisor==0:
        divisores2.append(divisor)
    
if sum(divisores1)==numero2 and sum(divisores2)==numero1:
    print("Son amigos")

else:
    print("No son amigos")