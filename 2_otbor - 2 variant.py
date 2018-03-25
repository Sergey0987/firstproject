n=int(input('Введите количество школьников: '))
list1=[]
list2=[]

for i in range(n): #создаем массив, каждый i-ый элемент в массиве = кортежу из имени и оценки
    a,b=input().split()
    list1.append(a)
    list1.append(int(b))
    list1=tuple(list1)
    list2.append(list1)
    list1=[]
list2=tuple(list2)

for i in range(len(list2)):
    print(list2[i][0],list2[i][1])

print()

for i in range(len(list2)):
    if list2[i][1]>3:
        print(list2[i][0],list2[i][1])
        


               

