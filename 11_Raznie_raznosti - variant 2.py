#Решение с использованием циклов

N=int(input())
list1=[]
list2=[]

for i in range(N): #подготовили список, с которым будем работать
    list1.append(int(input()))


for i in range(len(list1)): # Добавили в список все возможные разности чисел (тут есть повторения)
    for j in range(len(list1)-1):
        list2.append(list1[i]-list1[j])
        list2.append(list1[j]-list1[i])

list2.sort() # отсортировали для последующего поочередного сравнения

list1=[] # обнулили первый список

for i in range(len(list2)-1): #стали сравнивать поочередно элементы отсортированного списка
    if list2[i]!=list2[i+1]:
        list1.append(list2[i])
        if i==(len(list2)-2):
            list1.append(list2[i+1])

print(list1)
