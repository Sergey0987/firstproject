def printMultiplicationTebale():
    list1=[1,2,3,4,5,6,7,8,9]
    for i in range(1,len(list1)+1):
        for j in range(len(list1)):
            list1[j]=list1[j]*i
        print(' '.join(str(k) for k in list1))
        for j in range(len(list1)):
            list1[j]=int(list1[j]/i)
            
printMultiplicationTebale()
