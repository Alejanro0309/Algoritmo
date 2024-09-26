'''deporte={"futbol":"Messi","basquet":"Lebro","padel":"Juan","tenis":"Nadal",}
print(list(deporte))
print("Bienvenido")
for i in list(deporte):
    print(deporte[i])

lugares=[{"Caracas":["metro","parque","restaurante"],"Margarita":["playa","hoteles","montaña"],"Miami":["torre","tienda","casa"]}]

for i in lugares:
    for j in i:
        for k in i[j]:
            print(j,"tiene",k)

elementos=[
    {
    "nombre":"hidrogeno",
    "numero":1,
    "peso":1.00794,
    "simbolo":"H"
    },
    {
    "nombre":"helio",
    "numero":2,
    "peso":4.000,
    "simbolo":"He"
    }
    ]

for e in elementos:
    print("NOmbre: {}--Simbolo: {}--Peso: {}".format(e["nombre"],["simbolo"],["peso"]))'''

a=input("escribir un numero: ")
b=input("escribir un numero: ")

while not a.isnumeric():
    print("error")
    a=input("escribir un numero")

while not b.isnumeric():
    print("error")
    b=input("escribir un numero")
a=int(a)
b=int(b)

#convertir a binario
a=bin(a)
b=bin(b)

dicA={"0":0,"1":1}
dicB={"0":0,"1":1}
#cesosA=0
#unosA=0
#cerosB=0
#unosB=0

for i in range(2,len(a)):
    dicA[a[i]]=dicA[a[i]]+1
    '''if a[i]=="0":
        continue
        cesosA=cesosA+1
    elif a[i]=="1":
        unosA=unosA+1'''

for i in range(2,len(b)):
    dicB[b[i]]=dicB[b[i]]+1
    '''if b[i]=="0":
        continue
        cesosB=cesosB+1
    elif a[i]=="1":
        unosB=unosB+1'''

if dicA["1"]==dicB["1"]:
    print(a,"es anagrama de",b)
else:
    print(a,'y',b,"no son anagrama")