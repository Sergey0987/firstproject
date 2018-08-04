def arithmeticOperation(operation):
    if operation == '*':
        return lambda x,y: x * y
    elif operation == '/':
        return lambda x,y: x / y
    elif operation == '+':
        return lambda x,y : x + y
    else:
        return lambda x,y : x - y

func = arithmeticOperation('*')
print(func(5,6))
