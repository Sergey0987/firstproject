def transpose(matrix):
    b=[]

    for i in range(len(matrix[0])):
        b.append([])
        for j in range(len(matrix)):
            b[i].append(matrix[j][i])

    matrix.clear()
    
    for i in range(len(b)):
        matrix.append([])
        for j in b[i]:
            matrix[i].append(j)

    for i in range(len(matrix)):
        print(matrix[i])


transpose([[1, 2 ,3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]])

print()

transpose([[2, 3 ,4],
           [5, 6, 7],
           [8, 9, 10]])


