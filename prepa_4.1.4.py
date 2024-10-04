dic={}
palabra1='fowow'
palabra2='bapaq'

isomorfo=True

for i in range(len(palabra1)):
    if palabra1[i] in dic:
        if palabra2[i]!=dic[palabra1[i]]:
            isomorfo=False
    else:
        dic[palabra1[i]]=palabra2[i]
print(isomorfo)