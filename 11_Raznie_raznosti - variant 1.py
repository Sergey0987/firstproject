#Решение с использованием множест для удаления повторений чисел

N=int(input())
list1=[]
set1=set()

for i in range(N): #подготовили список, с которым будем работать
    list1.append(int(input()))


for i in range(len(list1)): #собрали множество уникальных разностей
    for j in range(len(list1)-1):
        set1.add(list1[i]-list1[j])
        set1.add(list1[j]-list1[i])

list1=sorted(list(set1)) #превратили множество в список и отсортировали его

for i in list1: # Вывели результат
    print(i)
