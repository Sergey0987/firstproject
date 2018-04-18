def printMultiplicationTebale(row, cols):
    list1=[]

    for i in range(cols):
        list1.append(i+1)
        
    for i in range(1,row+1):
        for j in range(cols):
            list1[j]=list1[j]*i
        print(' '.join(str(k) for k in list1))
        for j in range(cols):
            list1[j]=int(list1[j]/i)
            
printMultiplicationTebale(4,5)
