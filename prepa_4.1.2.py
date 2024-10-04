numero=24
divisores_primos=[]

for divisor_numero in range(2,numero):
    if numero%divisor_numero==0:
        es_primo=True
        for j in range(2,divisor_numero):
            if divisor_numero%j==0:
                es_primo=False
                break
        if es_primo:
            divisores_primos.append(divisor_numero)
print(divisores_primos)