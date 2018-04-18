def printAverage(arr):
    a=0
    if len(arr)==0:
        print('Среднее значение =', len(arr))
    else:
        for i in arr:
            a=a+i
        print('Среднее значение =', a/len(arr))

printAverage([3,5,10,4])
printAverage([1,5,5,4])
printAverage([14,5,12,4])
