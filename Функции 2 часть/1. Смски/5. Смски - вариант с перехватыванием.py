def printWithoutDuplicates(massage):
    global a
    try:
        if massage not in a:
            print(massage)
            a.add(massage)
    except NameError:
        a=set()
        a.add(massage)
        print(massage)
    return a

        

printWithoutDuplicates('Привет')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Когда доедешь до дома')
printWithoutDuplicates('Ага, жду')
printWithoutDuplicates('Ага, жду')


