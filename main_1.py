palabra1="jdsd509"
palabra2="atrft"
palabra3=""
ciclo=""

if len(palabra1)>len(palabra2):
    ciclo=len(palabra1)
else:
    ciclo=len(palabra2)
    
for i in range(ciclo):
    if i < len(palabra1):
        palabra3+=palabra1[i]
    if i < len(palabra2):
        palabra3+=palabra2[i]
print(palabra3,'listo')