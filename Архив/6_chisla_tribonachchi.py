n=int(input('Количество числе Трибоначчи '))
list1=[]

for i in range(n):
    if i<=2:
        list1.append(1)
    else:
        list1.append(list1[i-3]+list1[i-2]+list1[i-1])

list1=tuple(list1)

print(' '.join(str(i) for i in list1))
