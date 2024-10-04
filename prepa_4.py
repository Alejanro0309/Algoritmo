numeros = [1634, 225, 490, 9926315, 800, 93084, 313, 216, 864, 757, 243, 301, 833, 200, 54748, 32, 787,  536, 343, 353, 24678050, 16, 370, 181, 131, 818, 24678051, 153, 196, 400, 784, 31, 371, 9474, 10301, 729, 648, 973, 256, 548834,  9800817, 9, 289, 302, 81, 101, 36, 716, 968,  100, 49, 432, 169, 484, 128, 125, 961, 1000,  608, 219, 739, 529, 797, 931, 27, 108, 379, 727, 324, 121, 841, 288, 373, 919, 92727, 8208, 64, 632, 625, 4210818, 144, 1741725, 72, 151, 929, 675, 790, 655, 11, 407, 512, 25, 262, 900, 383,  441, 392, 576, 7, 361, 972, 88593477, 500, 676,  191, 1597, 7951] 
resultado=[]

for numero in numeros:
    es_primo=True
    for i in range(2,numero):
        if numero%i==0:
            es_primo=False
            break
    alreves_esprimo=True
    numero_volteado=str(numero)[::-1]
    numero_volteado=int(numero_volteado)
    for i in range(2,numero_volteado):
        if numero_volteado%i==0:
            alreves_esprimo=False
            break
    if es_primo and alreves_esprimo and numero!=1 and numero!=numero_volteado:
        resultado.append(numero)
print(resultado)