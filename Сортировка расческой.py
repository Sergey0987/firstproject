n=int(input('Введите количество чисел: '))
list1=[]
m=0 #нужен, чтобы уменьшить k, когда дойдет до 2-х, т.к. срабатывает округление и все время 2 получается
t=1 # коэффициент, который позволяет при k=1 и отсутствию обменов местами чисел остановить цикл

for i in range(n):
    list1.append(int(input('Введите число: ')))

k=round(len(list1)/1.247)

print('введенный список: ', list1)


for i in range(len(list1)): 
    for i in range(0,len(list1)-k):
            if list1[i]>list1[k+i]:
                list1[i],list1[k+i]=list1[k+i],list1[i]
                t=1
    k=round(k/1.247)
    if k==2:
        m=m+1
        if m==2:
            k=1
    if k==1 and t==0:
        break
    t=0

print('Отсортированный список', list1)
  
