def printOperationTable(operation, numRows = 9, numColumns = 9):

    rows = [int(x) for x in range(1,numRows + 1)]
    columns = [int(y) for y in range(1, numColumns +1)]
    
    list_of_numbers = list(map(lambda x: [x]*numRows, columns)) #сделан список списков с однотипными цифрами. Например, [[1,1,1], [2,2,2]]
    
    print(list_of_numbers)
    print(rows, columns)
    
    if operation == '*':
        if len(list_of_numbers) >= len(columns):
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '*' + str(y) + '=' + str(z*y)), x, rows)),list_of_numbers))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func))
        else:
#            print('list', list_of_numbers)
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '*' + str(y) + '=' + str(z*y)), x, rows)), list_of_numbers))
            func2 = list(map(lambda x: list(filter(lambda y: '=0' not in y , x)) , func))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func2))
    elif operation == '+':
        if len(list_of_numbers) >= len(columns):
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '+' + str(y) + '=' + str(z+y)), x, rows)),list_of_numbers))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func))
        else:
#            print('list', list_of_numbers)
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '+' + str(y) + '=' + str(z+y)), x, rows)), list_of_numbers))
            func2 = list(map(lambda x: list(filter(lambda y: '=0' not in y , x)) , func))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func2))
    elif operation == '**':
        if len(list_of_numbers) >= len(columns):
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '**' + str(y) + '=' + str(z**y)), x, rows)),list_of_numbers))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func))
        else:
#            print('list', list_of_numbers)
            func = list(map(lambda x: list(map(lambda z,y: (str(z) + '**' + str(y) + '=' + str(z**y)), x, rows)), list_of_numbers))
            func2 = list(map(lambda x: list(filter(lambda y: '=0' not in y , x)) , func))
            printIt = list(map(lambda x: list(map(lambda y: print(y), x)) , func2))        





printOperationTable('**', numRows = 2, numColumns = 5)
