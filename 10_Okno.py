n=int(input("Введите количество бутылок: "))
list1=[]
minim=95
maxim=105

for i in range(n):
    list1.append(int(input()))
list1=tuple(list1)

for j in list1:
    if j<=maxim and j>=minim:
        print(j)




