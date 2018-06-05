#def continueFibonacciSequence(sequence, n):
#    for i in range(n):
#        nextElement = sequence[-1] + sequence[-2]
#        sequence = sequence + [nextElement]
#    print(sequence)

#continueFibonacciSequence([13, 21], 10)
#continueFibonacciSequence([0, 1], 15)


#Предположил, что ошибка в том, что каждый раз создается новый список при сложении списков. Заменил на метод добавления append()

def continueFibonacciSequence(sequence, n):
    for i in range(n):
        nextElement = sequence[-1] + sequence[-2]
        sequence.append(nextElement)
        print(id(sequence))
    print(sequence)

continueFibonacciSequence([13, 21], 10)
continueFibonacciSequence([0, 1], 15)
