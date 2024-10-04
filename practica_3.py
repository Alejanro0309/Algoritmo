# nums = [1, 2, 3, 4]

# n=1
# output=[]
# for i in range(0,len(nums),1):
#     #print(nums[i],'i')
#     # x*=i+n
#     # n=+1
#     print(i,'i')
#     x=1
#     for j in range(0,len(nums),1):
#         print(j,'j')
#         if j!=i:
#             x*=nums[j]
#     output.append(x)

#     print(x,'multiplicacion')

# print(output)

# palabra1='foo'
# palabra2='bar'

# if len(palabra1)==len(palabra2):
#     mapeo1 = [-1] * 256
#     mapeo2 = [-1] * 256
#     for letra in range(len(palabra1)):
#         print('m')
#         if mapeo1[ord(palabra1[letra])] != mapeo2[ord(palabra2[letra])]:
#             print('c')
#             print(False)
#         elif  mapeo1[ord(palabra1[letra])] == letra and mapeo2[ord(palabra2[letra])] == letra:
#             print('o')
#             print(True)

# pares = [2, 3, 4, 7, 3, 5]
# pares2=pares[::-1]
# list=[]
# x=0

# for i in range(len(pares)):
#     if i<len(pares)/2:
#         x+=pares[i]+pares2[i]
#         list.append(x)
# print(list)


nums = [1, 2, 3, 4]
x=1
multi=[]
for i in range(len(nums)):
    x=1
    for j in range(len(nums)):
        if i!=j:
            x*=nums[j]

    multi.append(x)
print(multi)