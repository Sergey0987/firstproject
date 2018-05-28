n=int(input("Введите количество бутылок: "))
list1=[]

for i in range(n): # Создали список из бутылок
    list1.append(int(input()))
list1=tuple(list1)

minim,maxim=int(input()),int(input())

for j in list1:
    if j<=maxim and j>=minim:
        print(j)




