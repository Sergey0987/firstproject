def matrix(N='default', M='default', a=0):
    if N == 'default' and M == 'default':
        N=1
        M=1
    elif N != 'default' and M == 'default':
        M=N

    matrix_list=[]
    for row in range(N):
        matrix_list.append([])
        for column in range(M):
            matrix_list[row].append(a)
    print(matrix_list)

matrix()
matrix(2)
matrix(2,5)
matrix(3,4,'win')
