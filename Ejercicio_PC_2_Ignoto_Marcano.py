#Ejecicios de programación competitiva

#Algoritmos y Programación Sección #2

#Luis Ignoto y Alejandro Marcano

def horas(hours, target):
    cumple = 0
    lista = []
    for i in range(len(hours)):
        if hours[i] >= target:
            condicion = 'El empleado {} trabajó {} y cumplió el objetivo'.format(i, hours[i])
            lista.append(condicion)
            cumple +=1
        else:
            condicion = 'El empleado {} trabajó {} y no cumplió el objetivo'.format(i, hours[i])
            lista.append(condicion)
    return cumple

hours = [0, 1, 2, 3, 4]

target = 2

resultados = horas(hours, target)

print('Hay {} empleados que cumplieron el objetivo'.format(resultados))