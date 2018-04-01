n=int(input('Количетво строк = '))
list1=[]
k=0
f=0

for i in range(n):
    list1.append(int(input('Введите строку ')))

n=len(list1)-1
m=0

while n!=0:
    k=0
    f=0
    for i in range(m,n):
        if list1[i]>list1[i+1]: # делает обмен двух элементов
            list1[i],list1[i+1]=list1[i+1],list1[i]
            k=1
    if k==0:
        break
    for j in range(n,m,-1):
        if list1[j]<list1[j-1]:
            list1[j],list1[j-1]=list1[j-1],list1[j]
            f=1
    n=n-1 
    m=m+1
    if f==0:
        n=0
print(list1)



  
