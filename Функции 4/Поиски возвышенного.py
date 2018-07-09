def findMountain(heightsMap):
    row = 0
    column = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > heightsMap[row][column]:
                row = i
                column = j
    return (row, column)

row, column = findMountain([[1,3,1],[3,2,5],[2,2,2]])

print(row, column)
