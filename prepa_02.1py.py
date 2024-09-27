n=input("escribe un numero: ")

while not n.isnumeric():
    print("error")
    n=input("escribe un numero: ")


if n=="0":
    print("La sucesion Fibonacci es: 0")
elif n=="1":
    print("La sucesion Fibonacci es: 0,1 ")
else:
    sucesion=[0,1]
    str_sucesion="0,1,"
    for i,num in enumerate(sucesion):
        fx=num+sucesion[i+1]
        
        print(fx)
        print(sucesion)
        if fx<=int(n):
            sucesion.append(fx)
            str_sucesion+=f"{fx},"
        else:
            break
    str_sucesion=str_sucesion[0:-1]
    print(str_sucesion)


    
