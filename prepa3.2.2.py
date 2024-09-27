numero=371
acumulador=0
for i in str(numero):
    acumulador+=int(i)**len(str(numero))

if acumulador==numero:
    print("es narcisita")
else:
    print("no es narcisita")
    