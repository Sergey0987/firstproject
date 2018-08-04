def printOperationTable(operation, numRows=9, numColumns=9):
    list_of_rows = [x for x in range(1,numRows + 1)]
    list_of_columns = [y for y in range(1,numColumns + 1)]
    if operation == '*':
        pass
    elif operation == '+':
        pass
    elif operation == '**':
        print(list_of_rows, list_of_columns)
                





printOperationTable('**', numRows=9, numColumns=9)
