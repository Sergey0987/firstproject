n=int(input('Введите число значение: '))
list1=[]
k=1
f=1
for i in range(n):
    list1.append(int(input()))

#print(list1)

while k!=0 and f!=0:
    k=0
    f=0
    for i in range(0,len(list1)-1,2): #Бегает по нечетным индексам
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            k=1
    for j in range(1,len(list1)-1,2): #Бегает по четным индексам
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            f=1
print(list1)

  
