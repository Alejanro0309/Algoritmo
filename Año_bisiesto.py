#Pedir año bisiesto
año=input("Escriba un año entre 1900 y 2199: ")
while not año.isnumeric():
    print("Error,ha escrito una letra")
    año=input("Escriba un año entre 1900 y 2199: ")
    
año=int(año)
while año<1900 or año>2199:
    print("Error,ha escrito un año que no esta entre 1900 y 2199")
    año=input("Escriba un año entre 1900 y 2199: ")
    año=int(año)

#Dar año bisiesto sin ciclos
if año % 4==0 and (año % 100==0 or not año % 400==0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

#Año bisiesto con ciclo
bisiesto=0
no_bisiesto=0
for i in range(1900,año,1):
    if i % 4==0 and (i % 100==0 or not i % 400==0):
        bisiesto+=1

print("Año bisiesto desde 1900 hasta",año,'son',bisiesto)