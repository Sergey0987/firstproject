row=int(input())
column=int(input())
list1=[]
list2=[]
for i in range(row):
    list2.append(input())
    list2.append(input())
    list1.append(tuple(list2))
    list2=[]
for i in list1:
    print(' '.join(j for j in i))



