#Ejecicios de programación competitiva

#Algoritmos y Programación Sección #2

#Luis Ignoto y Alejandro Marcano


def invertir(palabra, cond):
    salida =''
    for i in range(len(palabra)):
        if palabra[i] == cond:
            salida = salida[::-1]
        else:
            salida += palabra[i]
    return  salida          


s = 'sring'
cond = 'i'

print(invertir(s, cond))

