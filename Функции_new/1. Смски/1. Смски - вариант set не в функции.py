a=set()
def printWithoutDuplicates(massage):
    global a
    if massage not in a:
        print(massage)
        a.add(massage)
    return a

        

printWithoutDuplicates('Привет')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Когда доедешь до дома')
printWithoutDuplicates('Ага, жду')
printWithoutDuplicates('Ага, жду')


