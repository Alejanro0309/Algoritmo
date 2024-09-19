#Perfil de entrenador
print("************Menu*************")
print()
sexo=input("Eres hombre o mujer: \n1- hombre \n2- mujer \nrespuesta: ")

while sexo!="1" and sexo!="2":
    print("Hemos obtenido un error")
    sexo=input("Puedes decirnos si eres hombre o mujer: \n1- hombre \n2- mujer \nrespuesta: ")

if sexo=="1":
    print("Hola bienvenido !!!")

elif sexo=="2":
    print("Hola bienvenida!!!")

nombre=input("Ingresa el nombre de entrenador pokemon: ")
edad=input("Cuantos años tienes: ")

while not edad.isnumeric():
    print("Lo sentimos tuvimos un error")
    edad=input("Cuantos años tienes: ")

edad=int(edad)
#verificación
if edad<10:
    if sexo=="1":
        print("No tienes edad para ser un entrenador pokemon")
    else:
        print("No tienes edad para ser un entrenadora pokemon")
    exit()

if sexo=="1":
    print("Listo para comenzar esta aventura")
else:
     print("Lista para comenzar esta aventura")

region=input("En que region te encuentras\n1-Kanto\n2-Johto\n3-Hoenn\n4-Sinnoh\n5-Teselia\n6-Alola\nrespuesta: ")
pokemon=input("Que tipo de pokemon quieres:\n1-Aire \n2-Fuego \n3-Agua \n4-Rocca \n respuesta: ")

while pokemon!='1' and pokemon!='2' and pokemon!='3' and pokemon!='4':
    print("Hemos obtenido un error")
    pokemon=input("Puedes decirnos si quieres un pokemon tipo: \n1-Aire \n2-Fuego \n3-Agua \n4-Rocca \n respuesta: ")

#pokemon
if pokemon=='1':
    if sexo=='1':
        print("Hola",nombre,'te ha tocado de pokemon principal Lugia,ya oficialmente eres un entrenador pokemon')
    else:
        print("Hola",nombre,'te ha tocado de pokemon principal Lugia,ya oficialmente eres una entrenadora pokemon')
elif pokemon=='2':
    if sexo=='1':
        print("Hola",nombre,'te ha tocado de pokemon principal Charizard,ya oficialmente eres un entrenador pokemon')
    else:
        print("Hola",nombre,'te ha tocado de pokemon principal Charizard,ya oficialmente eres una entrenadora pokemon')
elif pokemon=='3':
    if sexo=='1':
        print("Hola",nombre,'te ha tocado de pokemon principal Vaporeon,ya oficialmente eres un entrenador pokemon')
    else:
        print("Hola",nombre,'te ha tocado de pokemon principal Vaporeon,ya oficialmente eres una entrenadora pokemon')
else:
    if sexo=='1':
        print("Hola",nombre,'te ha tocado de pokemon principal Regirock,ya oficialmente eres un entrenador pokemon')
    else:
        print("Hola",nombre,'te ha tocado de pokemon principal Regirock,ya oficialmente eres una entrenadora pokemon')