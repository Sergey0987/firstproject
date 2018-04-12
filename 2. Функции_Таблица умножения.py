def printMultiplicationTebale():
    list1=[1,2,3,4,5,6,7,8,9]
    list2=[]
    for j in range(1,len(list1)+1):
        for i in list1:
            list2.append(i*j)
        print(' '.join(str(n) for n in list2))
        list2.clear()

printMultiplicationTebale()
