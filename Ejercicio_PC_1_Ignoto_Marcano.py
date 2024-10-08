#Ejecicios de programación competitiva

#Algoritmos y Programación Sección #2

#Luis Ignoto y Alejandro Marcano

word_1 = ["ab", "c"]

word_2 = ["a", "bc"]

completo_1 = ''; completo_2 = ''

for i in word_1:
    completo_1 += i

for i in word_2:
    completo_2 += i

if completo_1 == completo_2:
    print(True)
else:
    print(False)
