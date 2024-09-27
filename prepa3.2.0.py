numeros=[-4,-5,-3,-2,4,6,7,4,-10,8,-15,6,-5,-10,-11]
out=[]

if numeros[0]>numeros[1]:
    out.append([numeros[0],0])

for i in range(1,len(numeros)-1):
    if numeros[i+1]< numeros[i] and numeros[i-1]<numeros[i]:
        out.append([numeros[i],i])

if numeros[-1]>numeros[-2]:
    out.append([numeros[-1],len(numeros)-1])
print(out)