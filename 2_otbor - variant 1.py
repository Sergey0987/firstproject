n=int(input('Введите количество швольников: '))
list1=[]

for i in range(n):
    a,b=input().split()
    list1.append(a)
    list1.append(b)

list1=tuple(list1)
    
for j in range(0,len(list1),2):
    print(list1[j],list1[j+1])

print()

for k in range(0,len(list1),2):
    if int(list1[k+1])>3:
        print(list1[k],list1[k+1])

               

