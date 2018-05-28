n=int(input('Количетво строк = '))
list1=[]
k=1 #коэффициент, который будет служить ориентиром продолжать или нет

for i in range(n):
    list1.append(input('Введите строку '))

#print(list1)

while k!=0:
    k=0
    for i in range(len(list1)-1):
        if ord(list1[i][0])>ord(list1[i+1][0]):
            list1[i],list1[i+1]=list1[i+1],list1[i]
            k=1
print(list1)    
